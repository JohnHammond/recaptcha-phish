# reCAPTCHA Phish

> John Hammond | September 13, 2024

------------------------------

![Verify You Are Human](https://github.com/user-attachments/assets/56be51b9-e58d-40e9-bdb1-54bcc11d4180)

This is small harness to recreate the social engineering and phishing lure recently seen in the wild around August/September 2024.

## 🪝 The Lure In The Wild

Originally seen with the guise **"Verify you are human"**, the attack vector being _**copy and paste**_. 

It literally instructs the user to open the Windows Run dialog box with the hotkey `Win+R`, and have them paste in a malicious command with `Ctrl+V` that the web browser has premptively copied into their clipboard.

![Verification Steps](https://github.com/user-attachments/assets/77e9adcb-672e-4a45-845d-58a90ba22935)

Despite this being... **_dumb_**... sure, it probably works. 😅

Following some chatter on [Twitter](https://x.com/_JohnHammond/status/1834292759320297534), these are apparently called ["ClickFix"](https://x.com/ex_raritas/status/1834399472371016084), or [Emmenhtal](https://x.com/SquiblydooBlog/status/1834292295224475648), used in [LummaStealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.lumma) campaigns observed by [Unit42](https://x.com/Unit42_Intel/status/1829178013423992948), [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide), [Huntress](https://www.huntress.com/), and others. 

Tonmoy Jitu also wrote a [sweet article](https://denwp.com/anatomy-of-a-lumma-stealer/) covering the original lure. 🔥

----------

## 🎨 Recreation

> [!CAUTION]
> The code is bad because I am a bad programmer.

Considering the original is meant to emulate a [reCAPTCHA](https://www.google.com/recaptcha/about/) form, I thought this _"tradecraft"_ (if you dare to call it that) could be improved. 😈

Why not make it look as close to the real reCAPTCHA button as possible?

![reCAPTCHA](https://github.com/user-attachments/assets/3967e15b-0717-4db4-afa1-62394e47f3b2)

![New Steps](https://github.com/user-attachments/assets/2fac92b1-fdff-4a67-883b-b8c1b8ae4aa7)

This repository includes some of my code playing with that idea.

Really all you need is `index.html`. It includes the CSS and JavaScript in a single file for ease of use, but might need further customization to change the command that is ran (see the JavaScript at the end of the `showVerifyWindow` function). This can be used as a standalone file and a run any local command, but to get a bit more flexibility with code execution, this repository includes a sample HTA file `recaptcha-verify` for an innocent proof of concept of popping open the Windows calculator application. This secondary HTA file would mean it needs to be hosted server-side, or have some other backing infrastructure to offer the payload. 

For quick local testing, I literally just used `python -m http.server 8000`. 

The HTA file also gives you an opportunity for more convincing charade, too, potentially with a window that pops up to "try and connect to the reCAPTCHA servers", but state that it fails and prompt the user to do it all over again. 🤪 _(Extra callbacks, anybody?)_

![Fail to connect](https://github.com/user-attachments/assets/b3e062a5-eb2a-4c43-9b6f-411625e7f740)

So this recreation has some extra perks:

* Looks and feels like "real" reCAPTCHA (_image from the official Google site_)
* Validation in the Run box to "hide" the command (✅ _"I am not a robot - reCAPTCHA Verification ID: 7624"_)
* Disabled "Verify" button to further encourage users to complete the copy-paste steps. 🚫
* Fleshed out phish with the follow-up windows "failed to verify"
* Clears the clipboard so the payload command is removed.

Some code is reused from https://github.com/75a/fake-captcha

-------------

## 🤔 Other Musings

* Perhaps this could be used within an `iframe` element, or easily embedded as a widget _anywhere_.
* Perhaps this could have a bit more server-side control to check the client's user-agent and do things differently, or adjust the payload appropriately.

**Also, _EdyUkAYshuNaL PoRpoiSes only!!!11_** 🐬
