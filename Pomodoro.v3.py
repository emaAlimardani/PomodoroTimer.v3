import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import winsound

def update_timer():
    global duration
    global on_break
    if running:
        if duration > 0:
            mins, secs = divmod(duration, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=timer)
            duration -= 1
            root.after(1000, update_timer)
        else:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            if not on_break:
                messagebox.showinfo("Pomodoro Timer", "Time is up! Take a break.")
                duration = 5 * 60 # set break time to 5 minutes
                on_break = True
                root.after(1000, update_timer)
            else:
                messagebox.showinfo("Pomodoro Timer", "Break is over! Time to work.")
                reset_timer()
                on_break = False


def start_timer():
    global running
    running = True
    update_timer()

def stop_timer():
    global running
    running = False

def reset_timer():
    global duration
    duration = 25 * 60

def update_timer():
    global duration
    if running:
        if duration > 0:
            mins, secs = divmod(duration, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=timer)
            duration -= 1
            root.after(1000, update_timer)
        else:
            messagebox.showinfo("Pomodoro Timer", "Time is up! Take a break.")
            reset_timer()

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="black")
        label.config(bg="black", fg="white")
        start_button.config(bg="black", fg="white")
        stop_button.config(bg="black", fg="white")
        reset_button.config(bg="black", fg="white")
        dark_mode_button.config(bg="black", fg="white", text="Light Mode")
    else:
        root.config(bg="white")
        label.config(bg="white", fg="black")
        start_button.config(bg="white", fg="black")
        stop_button.config(bg="white", fg="black")
        reset_button.config(bg="white", fg="black")
        dark_mode_button.config(bg="white", fg="black", text="Dark Mode")

root = tk.Tk()
root.title("Pomodoro Timer")

style = ttk.Style()
style.theme_use('clam')

label = ttk.Label(root, text="25:00", font=("Calibri", 30))
label.pack(pady=10)

start_button = ttk.Button(root, text="Start", command=start_timer)
start_button.pack(pady=5)

stop_button = ttk.Button(root, text="Stop", command=stop_timer)
stop_button.pack(pady=5)

reset_button = ttk.Button(root, text="Reset", command=reset_timer)
reset_button.pack(pady=5)

dark_mode_button = ttk.Button(root, text="Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=5)

duration = 25 * 60
running = False
dark_mode = False

root.mainloop()