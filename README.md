# ✅ Password Strength Checker
passwords are a part of everyday life and keeping them secure is extremely important so I created a python password strength checker. 

The checker utalises the [HaveIBeenPwned API](https://haveibeenpwned.com/) to check if the entered password has been in any databases. The checker also checks the basics that make up a strong password: length, special character, captial and number and provides a visual feedback via a tkinter GUI.

The app also features:
- A dynamic progress bar that updates based on password strength rating.

- Live feedback on password - Clear how password could be improved.

## ✨ Technologies
Python

Tkinter

hashLib

requests

## 🚀 Features

- progress bar - keeps the user motivated to make their password stronger

- keeps the password secure using hashing - never passes the full password

- toggle view - hide or view your password, keep it secure 



## 📍 The Process
With python being my strongest language, I decided to use it for my first project. After setting up the basic checker, takes input checks length, special characters, number and capitals sends feedback, I decided to add a more advanced feature that I hadn't done before - use an API. I learnt about the haveIbeenpwned API and decided to implement it, and after many attempts and countless errors I got it working. The last issue I faced was, that it wasnt that user friendly - it needed an interface. I decided to go with tkinter to create a simple clear userface which worked out quite well. Even though this was a basic project, I feel I have learnt alot from it - knowledge that will definetly be useful in future projects.

## 🚦 Running the Project
Clone the repository

If `requests` isn't installed yet:

```bash
pip install requests
```
run the code from an editor

## 🎞️ Preview

![password-strength-checker-recording](https://github.com/user-attachments/assets/13d14566-f822-4820-be27-144777a172bb)


  
