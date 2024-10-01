from flask import Flask, request,render_template,send_from_directory
import os

app = Flask(__name__)

@app.route('/config.txt')
def serve_config():
    return send_from_directory('.', 'config.txt')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def homes():
    return render_template('index.html')

@app.route('/recaptcha-verify', methods=['GET'])
def recaptcha_verify():
    # Get the 'id' parameter from the URL
    id_value = request.args.get('id', '')

    if id_value:
        

        # Save the modified id to config.txt
        with open('config.txt', 'a') as file:
            file.write("verification_id = "+ id_value + '\n')

        return f'ID saved: {id_value}', 200
    else:
        return 'ID not provided', 400


if __name__ == '__main__':
    # Ensure config.txt exists
    if not os.path.exists('config.txt'):
        with open('config.txt', 'w') as file:
            pass

    app.run(debug=True)
