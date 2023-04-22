# ====================================== Imports for front end and backend =============================================

import tkinter
from PIL import ImageTk, Image

# ======================================================================================================================

# ================================= Root Window: Pass-Stash Password Manager & Vault ===================================

PassStashWindow = tkinter.Tk()
PassStashWindow.title("Pass-Stash: Manager and Vault")
PassStashWindow.geometry("800x600")
PassStashWindow.configure(bg="#708090")
PassStashWindow.resizable(False, False)

# ======================================================================================================================

# ========================================== All Pash-Stash Operation Frames ===========================================

mPasswordFrame = tkinter.Frame(PassStashWindow, bg="#708090")
HomeOptionsFrame = tkinter.Frame(PassStashWindow, bg="#708090")

# ======================================================================================================================

# ======================================== Functions for switching Frames ==============================================


def change_frame_login():
    HomeOptionsFrame.pack_forget()
    PashStash_Label.grid(row=0, column=0, sticky="news", pady=50)
    mPassword_Label.grid(row=1, column=0)
    mPassword_Entry.grid(row=2, column=0, pady=10)
    Login_Button.grid(row=3, column=0, pady=10)
    mPasswordFrame.pack()
    Logo_Label.pack(pady=24)


def change_frame_home():
    HomeOptionsFrame.pack(fill='both', expand=1)
    Logo_Label.pack_forget()
    mPasswordFrame.pack_forget()


# ======================================================================================================================

# ====================================== Master Password Login Screen Frame ============================================

# Creating Master Password Related Widgets and Fields
PashStash_Label = tkinter.Label(
    mPasswordFrame, text="Pass-Stash: Manager & Vault", bg="#708090", fg="#FFFFFF", font=("Quicksand", 50))
mPassword_Label = tkinter.Label(
    mPasswordFrame, text="Enter Master Password:", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24))
mPassword_Entry = tkinter.Entry(mPasswordFrame, show="*", bg="#181818", font=("Quicksand", 24))
Login_Button = tkinter.Button(
    mPasswordFrame, text="Enter Vault", bg="#FFFFFF", fg="#181818", font=("Quicksand", 18), command=change_frame_home)
PashStash_Logo = Image.open("temp_icon.png")
Resize_Logo = PashStash_Logo.resize((200, 200))
nPashStash_Logo = ImageTk.PhotoImage(Resize_Logo)
Logo_Label = tkinter.Label(image=nPashStash_Logo, bg="#708090")

# Placing Master Password Related Widgets and Fields
PashStash_Label.grid(row=0, column=0, sticky="news", pady=50)
mPassword_Label.grid(row=1, column=0)
mPassword_Entry.grid(row=2, column=0, pady=10)
Login_Button.grid(row=3, column=0, pady=10)
mPasswordFrame.pack()
Logo_Label.pack(pady=24)

# ======================================================================================================================

# =========================================== Home Screen Options Frame ================================================

# Creating Home Screen Options Related Widgets and Fields
Options_Label = tkinter.Label(HomeOptionsFrame, text="Please Select An Option", bg="#708090", fg="#FFFFFF", font=("Quicksand", 60), pady=50)
Create_Label = tkinter.Label(HomeOptionsFrame, text="Create Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Update_Label = tkinter.Label(HomeOptionsFrame, text="Update Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Delete_Label = tkinter.Label(HomeOptionsFrame, text="Delete Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Search_Label = tkinter.Label(HomeOptionsFrame, text="Search Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Generate_Label = tkinter.Label(HomeOptionsFrame, text="Generate Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Create_Button = tkinter.Button(HomeOptionsFrame, text="CREATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))
Update_Button = tkinter.Button(HomeOptionsFrame, text="UPDATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))
Delete_Button = tkinter.Button(HomeOptionsFrame, text="DELETE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))
Search_Button = tkinter.Button(HomeOptionsFrame, text="SEARCH", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))
Generate_Button = tkinter.Button(HomeOptionsFrame, text="GENERATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))

# Placing Home Screen Options Related Widgets and Fields
Options_Label.place(relx=0.5, rely=0.05, anchor="n")
Create_Label.place(relx=0.125, rely=0.425, anchor="center")
Create_Button.place(relx=0.125, rely=0.5, anchor="center")
Update_Button.place(relx=0.375, rely=0.5, anchor="center")
Update_Label.place(relx=0.375, rely=0.425, anchor="center")
Delete_Button.place(relx=0.625, rely=0.5, anchor="center")
Delete_Label.place(relx=0.625, rely=0.425, anchor="center")
Search_Button.place(relx=0.875, rely=0.5, anchor="center")
Search_Label.place(relx=0.875, rely=0.425, anchor="center")
Generate_Button.place(relx=0.5, rely=0.75, anchor="center")
Generate_Label.place(relx=0.5, rely=0.675, anchor="center")

# ======================================================================================================================

PassStashWindow.mainloop()