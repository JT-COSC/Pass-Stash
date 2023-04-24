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
PassStashWindow.eval('tk::PlaceWindow . center')
PassStashIcon = tkinter.Image("photo", file="temp_icon.png")
PassStashWindow.iconphoto(True, PassStashIcon)
PassStashWindow.wm_iconphoto(True, PassStashIcon)

# ======================================================================================================================

# ========================================== All Pash-Stash Operation Frames ===========================================

PassStashWelcomeFrame = tkinter.Frame(PassStashWindow, bg="#708090")
HomeOptionsFrame = tkinter.Frame(PassStashWindow, bg="#708090")
AddEntryFrame = tkinter.Frame(PassStashWindow, bg="#708090")
UpdateEntryFrame = tkinter.Frame(PassStashWindow, bg="#708090")
DeleteEntryFrame = tkinter.Frame(PassStashWindow, bg="#708090")
SearchEntryFrame = tkinter.Frame(PassStashWindow, bg="#708090")
GeneratePasswordFrame = tkinter.Frame(PassStashWindow, bg="#708090")


# ======================================================================================================================

# ======================================== Functions for switching Frames ==============================================


def change_frame_intro():
    HomeOptionsFrame.pack_forget()
    PashStash_Label.grid(row=0, column=0, sticky="news", pady=50)
    PassStash_Slogan.grid(row=1, column=0)
    Enter_Button.grid(row=3, column=0, pady=10)
    PassStashWelcomeFrame.pack()
    Logo_Label.pack(pady=24)


def change_frame_home():
    Logo_Label.pack_forget()
    PassStashWelcomeFrame.pack_forget()
    AddEntryFrame.pack_forget()
    UpdateEntryFrame.pack_forget()
    DeleteEntryFrame.pack_forget()
    SearchEntryFrame.pack_forget()
    GeneratePasswordFrame.pack_forget()
    HomeOptionsFrame.pack(fill='both', expand=1)


def change_frame_add():
    HomeOptionsFrame.pack_forget()
    AddEntryFrame.pack(fill='both', expand=1)


def change_frame_update():
    HomeOptionsFrame.pack_forget()
    UpdateEntryFrame.pack(fill='both', expand=1)


def change_frame_delete():
    HomeOptionsFrame.pack_forget()
    DeleteEntryFrame.pack(fill='both', expand=1)


def change_frame_search():
    HomeOptionsFrame.pack_forget()
    SearchEntryFrame.pack(fill='both', expand=1)


def change_frame_generate():
    HomeOptionsFrame.pack_forget()
    GeneratePasswordFrame.pack(fill='both', expand=1)


# ======================================================================================================================

# =========================================== Pass-Stash Intro Screen Frame ============================================

# Creating Pass-Stash Intro Related Widgets and Fields
PashStash_Label = tkinter.Label(
    PassStashWelcomeFrame, text="Pass-Stash: Manager & Vault",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"))
PassStash_Slogan = tkinter.Label(
    PassStashWelcomeFrame, text="Password Peace of Mind All in One Place",
    bg="#708090", fg="#FFFFFF", font=("Times New Roman", 24, "italic"))
Enter_Button = tkinter.Button(
    PassStashWelcomeFrame, text="Enter The Vault",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)
PashStash_Logo = Image.open("temp_icon.png")
Resize_Logo = PashStash_Logo.resize((200, 200))
nPashStash_Logo = ImageTk.PhotoImage(Resize_Logo)
Logo_Label = tkinter.Label(image=nPashStash_Logo, bg="#708090")

# Placing Pass-Stash Intro Related Widgets and Fields
PashStash_Label.grid(row=0, column=0, sticky="news", pady=50)
PassStash_Slogan.grid(row=1, column=0)
Enter_Button.grid(row=3, column=0, pady=50)
PassStashWelcomeFrame.pack()
Logo_Label.pack(pady=24)

# ======================================================================================================================

# =========================================== Home Screen Options Frame ================================================

# Creating Home Screen Options Related Widgets and Fields
Options_Label = tkinter.Label(
    HomeOptionsFrame, text="Select An Option",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 60, "bold"), pady=50)
Create_Label = tkinter.Label(
    HomeOptionsFrame, text="Create Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Update_Label = tkinter.Label(
    HomeOptionsFrame, text="Update Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Delete_Label = tkinter.Label(
    HomeOptionsFrame, text="Delete Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Search_Label = tkinter.Label(
    HomeOptionsFrame, text="Search Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Generate_Label = tkinter.Label(
    HomeOptionsFrame, text="Generate Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)
Lock_Label = tkinter.Label(
    HomeOptionsFrame, text="Quit Pass-Stash", bg="#708090", fg="#FFFFFF", font=("Quicksand", 18), pady=5)
Create_Button = tkinter.Button(
    HomeOptionsFrame, text="CREATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_add)
Update_Button = tkinter.Button(
    HomeOptionsFrame, text="UPDATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_update)
Delete_Button = tkinter.Button(
    HomeOptionsFrame, text="DELETE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_delete)
Search_Button = tkinter.Button(
    HomeOptionsFrame, text="SEARCH", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_search)
Generate_Button = tkinter.Button(
    HomeOptionsFrame, text="GENERATE",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_generate)
Lock_Button = tkinter.Button(
    HomeOptionsFrame, text="QUIT",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 24), command=PassStashWindow.destroy)

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
Generate_Button.place(relx=0.5, rely=0.7, anchor="center")
Generate_Label.place(relx=0.5, rely=0.625, anchor="center")
Lock_Label.place(relx=0.5, rely=0.865, anchor="center")
Lock_Button.place(relx=0.5, rely=0.925, anchor="center", width=130)

# ======================================================================================================================

# ============================================== Add New Entry Frame ===================================================

# Creating Add Credential Entry Related Widgets and Fields
Add_Label = tkinter.Label(
    AddEntryFrame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)
Account_Label = tkinter.Label(
    AddEntryFrame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
Username_Label = tkinter.Label(
    AddEntryFrame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
Password_Label = tkinter.Label(
    AddEntryFrame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
Account_Entry = tkinter.Entry(AddEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
Username_Entry = tkinter.Entry(AddEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
Password_Entry = tkinter.Entry(AddEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
AddSave_Button = tkinter.Button(
    AddEntryFrame, text="Save Entry", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)
AddCancel_Button = tkinter.Button(
    AddEntryFrame, text="Cancel Entry", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Add Credential Entry Related Widgets and Fields
Add_Label.place(relx=0.5, rely=0.05, anchor="n")
Account_Label.place(relx=0.2, rely=0.475, anchor="s")
Account_Entry.place(relx=0.2, rely=0.55, anchor="s")
Username_Label.place(relx=0.5, rely=0.475, anchor="s")
Username_Entry.place(relx=0.5, rely=0.55, anchor="s")
Password_Label.place(relx=0.8, rely=0.475, anchor="s")
Password_Entry.place(relx=0.8, rely=0.55, anchor="s")
AddSave_Button.place(relx=0.5, rely=0.75, anchor="s")
AddCancel_Button.place(relx=0.5, rely=0.9, anchor="s")

# ======================================================================================================================

# =========================================== Update Existing Entry Frame ==============================================

# Creating Add Credential Entry Related Widgets and Fields
UpdateHeader_Label = tkinter.Label(
    UpdateEntryFrame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)
UpdateAccountVerify_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
UpdateUsernameVerify_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
UpdatePasswordVerify_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
VerifySelected_Button = tkinter.Button(UpdateEntryFrame, text="Verify Account",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))
UpdateAccountVerify_Label = tkinter.Label(
    UpdateEntryFrame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
UpdateUsernameVerify_Label = tkinter.Label(
    UpdateEntryFrame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
UpdatePasswordVerify_Label = tkinter.Label(
    UpdateEntryFrame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
VerifySelected_Label = tkinter.Label(
    UpdateEntryFrame, text="Selected Account", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)
VerifySelected_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=43)
UpdateAccount_Label = tkinter.Label(
    UpdateEntryFrame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
UpdateUsername_Label = tkinter.Label(
    UpdateEntryFrame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
UpdatePassword_Label = tkinter.Label(
    UpdateEntryFrame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
UpdateAccount_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
UpdateUsername_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
UpdatePassword_Entry = tkinter.Entry(UpdateEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
UpdateSave_Button = tkinter.Button(
    UpdateEntryFrame, text="Update Entry",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)
UpdateCancel_Button = tkinter.Button(
    UpdateEntryFrame, text="Cancel Update",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Add Credential Entry Related Widgets and Fields
UpdateHeader_Label.place(relx=0.5, rely=0.05, anchor="n")

UpdateAccountVerify_Label.place(relx=0.2, rely=0.25, anchor="n")
UpdateAccountVerify_Entry.place(relx=0.2, rely=0.35, anchor="n")
UpdateUsernameVerify_Label.place(relx=0.8, rely=0.25, anchor="n")
UpdateUsernameVerify_Entry.place(relx=0.8, rely=0.35, anchor="n")
VerifySelected_Button.place(relx=0.5, rely=0.325, anchor="n")
VerifySelected_Label.place(relx=0.5, rely=0.4125, anchor="n")
VerifySelected_Entry.place(relx=0.5, rely=0.5, anchor="n")

UpdateAccount_Label.place(relx=0.2, rely=0.675, anchor="s")
UpdateAccount_Entry.place(relx=0.2, rely=0.725, anchor="s")
UpdateUsername_Label.place(relx=0.5, rely=0.675, anchor="s")
UpdateUsername_Entry.place(relx=0.5, rely=0.725, anchor="s")
UpdatePassword_Label.place(relx=0.8, rely=0.675, anchor="s")
UpdatePassword_Entry.place(relx=0.8, rely=0.725, anchor="s")
UpdateSave_Button.place(relx=0.5, rely=0.825, anchor="s")
UpdateCancel_Button.place(relx=0.5, rely=0.975, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Delete Existing Entry Frame ==============================================

# Creating Delete Credential Entry Related Widgets and Fields
DeleteHeader_Label = tkinter.Label(
    DeleteEntryFrame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)
DeleteAccount_Label = tkinter.Label(
    DeleteEntryFrame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)
DeleteAccount_Entry = tkinter.Entry(DeleteEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=19)
DeleteUsername_Label = tkinter.Label(
    DeleteEntryFrame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)
DeleteUsername_Entry = tkinter.Entry(DeleteEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=19)
DeleteVerify_Button = tkinter.Button(
    DeleteEntryFrame, text="Verify Account", bg="#FFFFFF", fg="#181818", font=("Quicksand", 24))
DeleteSelected_Label = tkinter.Label(
    DeleteEntryFrame, text="Selected Account", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)
DeleteSelected_Entry = tkinter.Entry(DeleteEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=43)
DeleteEntry_Button = tkinter.Button(
    DeleteEntryFrame, text="Delete Account",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)
DeleteCancel_Button = tkinter.Button(
    DeleteEntryFrame, text="Cancel Delete",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Delete Credential Entry Related Widgets and Fields
DeleteHeader_Label.place(relx=0.5, rely=0.05, anchor="n")
DeleteAccount_Label.place(relx=0.275, rely=0.36, anchor="s")
DeleteAccount_Entry.place(relx=0.275, rely=0.42, anchor="s")
DeleteUsername_Label.place(relx=0.725, rely=0.36, anchor="s")
DeleteUsername_Entry.place(relx=0.725, rely=0.42, anchor="s")
DeleteVerify_Button.place(relx=0.5, rely=0.5, anchor="s")
DeleteSelected_Label.place(relx=0.5, rely=0.6425, anchor="s")
DeleteSelected_Entry.place(relx=0.5, rely=0.7, anchor="s")
DeleteEntry_Button.place(relx=0.5, rely=0.8, anchor="s")
DeleteCancel_Button.place(relx=0.5, rely=0.95, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Search Existing Entry Frame ==============================================

# Creating Search Credential Related Widgets and Fields
SearchHeader_Label = tkinter.Label(
    SearchEntryFrame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)
SearchEntry_Label = tkinter.Label(
    SearchEntryFrame, text="Account Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)
Search_Entry = tkinter.Entry(SearchEntryFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 30))
SearchEntry_Button = tkinter.Button(
    SearchEntryFrame, text="Search Account", bg="#FFFFFF", fg="#181818", font=("Quicksand", 18))
SearchEntryAll_Button = tkinter.Button(
    SearchEntryFrame, text="Show Accounts", bg="#FFFFFF", fg="#181818", font=("Quicksand", 18))
SearchResult_Text = tkinter.Text(
    SearchEntryFrame, height=10, width=65, bg="#181818", fg="#FFFFFF", font=("Quicksand", 18))
SearchCancel_Button = tkinter.Button(
    SearchEntryFrame, text="Close Search",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 18), command=change_frame_home)

# Placing Search Credential Related Widgets and Fields
SearchHeader_Label.place(relx=0.5, rely=0.05, anchor="n")
SearchEntry_Label.place(relx=0.5, rely=0.35, anchor="s")
Search_Entry.place(relx=0.5, rely=0.43, anchor="s")
SearchEntry_Button.place(relx=0.359, rely=0.5, anchor="s")
SearchEntryAll_Button.place(relx=0.645, rely=0.5, anchor="s")
SearchResult_Text.place(relx=0.5, rely=0.89, anchor="s")
SearchCancel_Button.place(relx=0.5, rely=0.975, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Generate New Password Frame ==============================================

# Creating Generate Password Related Widgets and Fields
GeneratePassword_Label = tkinter.Label(
    GeneratePasswordFrame, text="Generate New Password",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)
NewPassword_Label = tkinter.Label(
    GeneratePasswordFrame, text="New Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)
NewPassword_Entry = tkinter.Entry(GeneratePasswordFrame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 36))
GenerateNewPassword_Button = tkinter.Button(
    GeneratePasswordFrame, text="Generate Password", bg="#FFFFFF", fg="#181818", font=("Quicksand", 22))
CopyNewPassword_Button = tkinter.Button(
    GeneratePasswordFrame, text="Copy New Password", bg="#FFFFFF", fg="#181818", font=("Quicksand", 22))
GeneratePasswordCancel_Button = tkinter.Button(
    GeneratePasswordFrame, text="Close Password Generator",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Generate Password Related Widgets and Fields
GeneratePassword_Label.place(relx=0.5, rely=0.05, anchor="n")
NewPassword_Label.place(relx=0.5, rely=0.4, anchor="s")
NewPassword_Entry.place(relx=0.5, rely=0.5, anchor="s")
GenerateNewPassword_Button.place(relx=0.345, rely=0.625, anchor="s")
CopyNewPassword_Button.place(relx=0.65, rely=0.625, anchor="s")
GeneratePasswordCancel_Button.place(relx=0.5, rely=0.9, anchor="s")

# ======================================================================================================================

PassStashWindow.mainloop()
