import tkinter as tk
from tkinter import ttk
import hashlib
import requests


def calculate_strength(password):
    score = 0
    cap = any(c.isupper() for c in password)
    num = any(c.isdigit() for c in password)
    sym = any(not c.isalnum() for c in password)
    length = len(password)

    if cap: score += 1
    if num: score += 1
    if sym: score += 1
    if length >= 16: score += 1

    return score, num, cap, sym, length

def check_password_strength(event=None):
    T.delete('1.0', tk.END)
    password = entry.get()
    if not password:
        progress["value"] = 0
        T.config(fg="black")
        return
    
    score, num, cap, sym, length = calculate_strength(password)
    update_colour(score)
    update_progress(score)
    check_pwned(password, score, num, cap, sym, length)


def check_pwned(password, score, num, cap, sym, length):
    found = False

    sha1 = hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    hash_hex = sha1.hexdigest().upper()
    prefix, suffix = hash_hex[:5], hash_hex[5:]

    PWNEDURL = "https://api.pwnedpasswords.com/range/{}"

    r = requests.get(PWNEDURL.format(prefix))

    hashes = (line.split(":") for line in r.text.splitlines())

    for i, count in hashes:
        if i == suffix:
            
            found = True
            
            print_feedback(score, found, count, cap, num, sym, length)
            return int(count)
    
    score += 1
    print_feedback(score, found, count, cap, num, sym, length)
    update_progress(score)
    update_colour(score)
    


def print_feedback(score, found, count, cap, num, sym, length):
    messages = [
        "( ˶°ㅁ°) !! Very weak password!",
        "(,,>﹏<,,) Weak password!",
        "( • ᴖ • ｡) Needs improvement.",
        "(,,•᷄‎ࡇ•᷅ ,,)? Decent, but could be better.",
        "(˶ᵔ ᵕ ᵔ˶) Strong password!",
        "ദ്ദി(ᵔᗜᵔ) Very strong and unique!"
    ]
    
    T.insert(tk.END, f" {messages[score]}\n\n")

    if found:
        T.insert(tk.END, f"⚠️ found in data breaches {count} times \n")
    else:
        T.insert(tk.END, f"✅ not found in data breaches \n")

    
    if not cap: T.insert(tk.END, f"★ add a capital letter \n")
    if not num: T.insert(tk.END, f"★ add a number \n")
    if not sym: T.insert(tk.END, f"★ add a symbol \n")
    if length < 16: T.insert(tk.END, f"★ use atleast 16 characters \n")

def update_progress(score):
    progress["value"] = score * 20

def update_colour(score):
    if score <= 2:
        T.config(fg="#C94343")
    elif score == 3 or score == 4:
        T.config(fg="#D68132")
    else:
        T.config(fg="#96AA55")

show_password = False
def toggle_password():
    global show_password
    show_password = not show_password
    entry.config(show = "" if show_password else "*")
    toggle_btn.config(text = "🔒" if show_password else "🔑")




#################################### GUI SETUP #################################################

root = tk.Tk()
root.title("mini password strength checker")
root.geometry("450x400")
root.resizable(False,False)
root.config(bg = "#FAEDCD")


tk.Label(root, text = "★ ENTER PASSWORD ★", font = ("Comic Sans", 14), bg ="#FAEDCD", fg = "#9A6D40" ).pack(pady = 5)
frame = tk.Frame(root)
frame.pack()
frame.config(bg = "#FAEDCD")
entry = tk.Entry(frame, show = "*", font = ("Kristen ITC", 12))
entry.pack(side = tk.LEFT, padx=(10,5))
entry.bind("<KeyRelease>", check_password_strength)
entry.config(bg = "#FEFAE0", fg = "#583E24")

toggle_btn = tk.Button(frame, text = "🔑", command=toggle_password, relief="groove")
toggle_btn.pack(side = tk.LEFT)
toggle_btn.config(bg = "#D4A373", fg = "#583E24")

style = ttk.Style()
style.theme_use('default')  

style.configure("Custom.Horizontal.TProgressbar",
                troughcolor='#E2AD7B',     
                background='#96AA55')  


progress = ttk.Progressbar(root, style = "Custom.Horizontal.TProgressbar", orient = "horizontal", length = 300, mode = "determinate", maximum=100)
progress.pack(pady=10)

T = tk.Text(root, height = 10, width=50, font = ("Kristen ITC", 10), relief= "groove")
T.pack(pady = 5)
T.config(bg =  "#FEFAE0")

root.mainloop()