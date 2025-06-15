# Mini Password Strength Checker #

A colorful, friendly GUI-based password strength checker built with Python's `tkinter` that:
- Checks for common strength indicators (length, uppercase, numbers, symbols)
- Verifies if the password has been found in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords)
- Offers real-time feedback

---

## Features ##

-  Real-time password evaluation
-  Progress bar with strength levels
-  Feedback with actionable suggestions
-  Toggle to show/hide password input
-  Pwned Passwords API check
-  Styled UI with warm color palette and playful fonts (Kristen ITC, Comic Sans)

---

## Getting Started ##

### Requirements ###

- Python 3.6+
- Internet connection (for the pwned password check)
- Modules used:
  - `tkinter` (comes with Python)
  - `hashlib` (standard lib)
  - `requests`

### Install Dependencies ###

If `requests` isn't installed yet:

```bash
pip install requests
```

### Acknowledgments ###

- [Troy Hunt's Have I Been Pwned](https://haveibeenpwned.com/)

  
