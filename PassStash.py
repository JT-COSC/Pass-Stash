# ====================================== Imports for front end and backend =============================================

import tkinter
from PIL import ImageTk, Image

# ======================================================================================================================

# ================================= Root Window: Pass-Stash Password Manager & Vault ===================================

pass_stash_window = tkinter.Tk()
pass_stash_window.title("Pass-Stash: Manager and Vault")
pass_stash_window.geometry("800x600")
pass_stash_window.configure(bg="#708090")
pass_stash_window.resizable(False, False)
pass_stash_window.eval('tk::PlaceWindow . center')
pass_stash_icon = tkinter.Image("photo", file="temp_icon.png")
pass_stash_window.iconphoto(True, pass_stash_icon)
pass_stash_window.wm_iconphoto(True, pass_stash_icon)

# ======================================================================================================================

# ========================================== All Pass-Stash Operation Frames ===========================================

pass_stash_welcome_frame = tkinter.Frame(pass_stash_window, bg="#708090")
home_options_frame = tkinter.Frame(pass_stash_window, bg="#708090")
add_entry_frame = tkinter.Frame(pass_stash_window, bg="#708090")
update_entry_frame = tkinter.Frame(pass_stash_window, bg="#708090")
delete_entry_frame = tkinter.Frame(pass_stash_window, bg="#708090")
search_entry_frame = tkinter.Frame(pass_stash_window, bg="#708090")
generate_password_frame = tkinter.Frame(pass_stash_window, bg="#708090")


# ======================================================================================================================

# ======================================== Functions for switching Frames ==============================================


def change_frame_intro():
    home_options_frame.pack_forget()
    pass_stash_label.grid(row=0, column=0, sticky="news", pady=50)
    pass_stash_slogan.grid(row=1, column=0)
    enter_button.grid(row=3, column=0, pady=10)
    pass_stash_welcome_frame.pack()
    logo_label.pack(pady=24)


def change_frame_home():
    logo_label.pack_forget()
    pass_stash_welcome_frame.pack_forget()
    add_entry_frame.pack_forget()
    update_entry_frame.pack_forget()
    delete_entry_frame.pack_forget()
    search_entry_frame.pack_forget()
    generate_password_frame.pack_forget()
    home_options_frame.pack(fill='both', expand=1)


def change_frame_add():
    home_options_frame.pack_forget()
    add_entry_frame.pack(fill='both', expand=1)


def change_frame_update():
    home_options_frame.pack_forget()
    update_entry_frame.pack(fill='both', expand=1)


def change_frame_delete():
    home_options_frame.pack_forget()
    delete_entry_frame.pack(fill='both', expand=1)


def change_frame_search():
    home_options_frame.pack_forget()
    search_entry_frame.pack(fill='both', expand=1)


def change_frame_generate():
    home_options_frame.pack_forget()
    generate_password_frame.pack(fill='both', expand=1)


# ======================================================================================================================

# =========================================== Pass-Stash Intro Screen Frame ============================================

# Creating Pass-Stash Intro Related Widgets and Fields
pass_stash_label = tkinter.Label(
    pass_stash_welcome_frame, text="Pass-Stash: Manager & Vault",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"))

pass_stash_slogan = tkinter.Label(
    pass_stash_welcome_frame, text="Password Peace of Mind All in One Place",
    bg="#708090", fg="#FFFFFF", font=("Times New Roman", 24, "italic"))

enter_button = tkinter.Button(
    pass_stash_welcome_frame, text="Enter The Vault",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

pass_stash_logo = Image.open("temp_icon.png")
resize_logo = pass_stash_logo.resize((200, 200))
new_pass_stash_logo = ImageTk.PhotoImage(resize_logo)
logo_label = tkinter.Label(image=new_pass_stash_logo, bg="#708090")

# Placing Pass-Stash Intro Related Widgets and Fields
pass_stash_label.grid(row=0, column=0, sticky="news", pady=50)
pass_stash_slogan.grid(row=1, column=0)
enter_button.grid(row=3, column=0, pady=50)
pass_stash_welcome_frame.pack()
logo_label.pack(pady=24)

# ======================================================================================================================

# =========================================== Home Screen Options Frame ================================================

# Creating Home Screen Options Related Widgets and Fields
options_label = tkinter.Label(
    home_options_frame, text="Select An Option",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 60, "bold"), pady=50)

create_label = tkinter.Label(
    home_options_frame, text="Create Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)

update_label = tkinter.Label(
    home_options_frame, text="Update Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)

delete_label = tkinter.Label(
    home_options_frame, text="Delete Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)

search_label = tkinter.Label(
    home_options_frame, text="Search Entry", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)

generate_label = tkinter.Label(
    home_options_frame, text="Generate Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 24), pady=5)

lock_label = tkinter.Label(
    home_options_frame, text="Quit Pass-Stash", bg="#708090", fg="#FFFFFF", font=("Quicksand", 18), pady=5)

create_button = tkinter.Button(
    home_options_frame, text="CREATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_add)

update_button = tkinter.Button(
    home_options_frame, text="UPDATE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_update)

delete_button = tkinter.Button(
    home_options_frame, text="DELETE", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_delete)

search_button = tkinter.Button(
    home_options_frame, text="SEARCH", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_search)

generate_button = tkinter.Button(
    home_options_frame, text="GENERATE",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_generate)

lock_button = tkinter.Button(
    home_options_frame, text="QUIT",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 24), command=pass_stash_window.destroy)

# Placing Home Screen Options Related Widgets and Fields
options_label.place(relx=0.5, rely=0.05, anchor="n")
create_label.place(relx=0.125, rely=0.425, anchor="center")
create_button.place(relx=0.125, rely=0.5, anchor="center")
update_button.place(relx=0.375, rely=0.5, anchor="center")
update_label.place(relx=0.375, rely=0.425, anchor="center")
delete_button.place(relx=0.625, rely=0.5, anchor="center")
delete_label.place(relx=0.625, rely=0.425, anchor="center")
search_button.place(relx=0.875, rely=0.5, anchor="center")
search_label.place(relx=0.875, rely=0.425, anchor="center")
generate_button.place(relx=0.5, rely=0.7, anchor="center")
generate_label.place(relx=0.5, rely=0.625, anchor="center")
lock_label.place(relx=0.5, rely=0.865, anchor="center")
lock_button.place(relx=0.5, rely=0.925, anchor="center", width=130)

# ======================================================================================================================

# ============================================== Add New Entry Frame ===================================================

# Creating Add Credential Entry Related Widgets and Fields
add_label = tkinter.Label(
    add_entry_frame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)

account_label = tkinter.Label(
    add_entry_frame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

username_label = tkinter.Label(
    add_entry_frame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

password_label = tkinter.Label(
    add_entry_frame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

account_entry = tkinter.Entry(add_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
username_entry = tkinter.Entry(add_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
password_entry = tkinter.Entry(add_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))

add_save_button = tkinter.Button(
    add_entry_frame, text="Save Entry", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

add_cancel_button = tkinter.Button(
    add_entry_frame, text="Cancel Entry", bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Add Credential Entry Related Widgets and Fields
add_label.place(relx=0.5, rely=0.05, anchor="n")
account_label.place(relx=0.2, rely=0.475, anchor="s")
account_entry.place(relx=0.2, rely=0.55, anchor="s")
username_label.place(relx=0.5, rely=0.475, anchor="s")
username_entry.place(relx=0.5, rely=0.55, anchor="s")
password_label.place(relx=0.8, rely=0.475, anchor="s")
password_entry.place(relx=0.8, rely=0.55, anchor="s")
add_save_button.place(relx=0.5, rely=0.75, anchor="s")
add_cancel_button.place(relx=0.5, rely=0.9, anchor="s")

# ======================================================================================================================

# =========================================== Update Existing Entry Frame ==============================================

# Creating Add Credential Entry Related Widgets and Fields
update_header_label = tkinter.Label(
    update_entry_frame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)

update_account_verify_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
update_username_verify_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
update_password_verify_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))

verify_selected_button = tkinter.Button(update_entry_frame, text="Verify Account",
                                        bg="#FFFFFF", fg="#181818", font=("Quicksand", 30))

update_account_verify_label = tkinter.Label(
    update_entry_frame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

update_username_verify_label = tkinter.Label(
    update_entry_frame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

update_password_verify_label = tkinter.Label(
    update_entry_frame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

verify_selected_label = tkinter.Label(
    update_entry_frame, text="Selected Account", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)

verify_selected_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=43)

update_account_label = tkinter.Label(
    update_entry_frame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

update_username_label = tkinter.Label(
    update_entry_frame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

update_password_label = tkinter.Label(
    update_entry_frame, text="Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

update_account_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
update_username_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))
update_password_entry = tkinter.Entry(update_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 16))

update_save_button = tkinter.Button(
    update_entry_frame, text="Update Entry",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

update_cancel_button = tkinter.Button(
    update_entry_frame, text="Cancel Update",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Add Credential Entry Related Widgets and Fields
update_header_label.place(relx=0.5, rely=0.05, anchor="n")
update_account_verify_label.place(relx=0.2, rely=0.25, anchor="n")
update_account_verify_entry.place(relx=0.2, rely=0.35, anchor="n")
update_username_verify_label.place(relx=0.8, rely=0.25, anchor="n")
update_username_verify_entry.place(relx=0.8, rely=0.35, anchor="n")
verify_selected_button.place(relx=0.5, rely=0.325, anchor="n")
verify_selected_label.place(relx=0.5, rely=0.4125, anchor="n")
verify_selected_entry.place(relx=0.5, rely=0.5, anchor="n")
update_account_label.place(relx=0.2, rely=0.675, anchor="s")
update_account_entry.place(relx=0.2, rely=0.725, anchor="s")
update_username_label.place(relx=0.5, rely=0.675, anchor="s")
update_username_entry.place(relx=0.5, rely=0.725, anchor="s")
update_password_label.place(relx=0.8, rely=0.675, anchor="s")
update_password_entry.place(relx=0.8, rely=0.725, anchor="s")
update_save_button.place(relx=0.5, rely=0.825, anchor="s")
update_cancel_button.place(relx=0.5, rely=0.975, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Delete Existing Entry Frame ==============================================

# Creating Delete Credential Entry Related Widgets and Fields
delete_header_label = tkinter.Label(
    delete_entry_frame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)

delete_account_label = tkinter.Label(
    delete_entry_frame, text="Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)

delete_account_entry = tkinter.Entry(delete_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=19)

delete_username_label = tkinter.Label(
    delete_entry_frame, text="Username", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)

delete_username_entry = tkinter.Entry(delete_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=19)

delete_verify_button = tkinter.Button(
    delete_entry_frame, text="Verify Account", bg="#FFFFFF", fg="#181818", font=("Quicksand", 24))

delete_selected_label = tkinter.Label(
    delete_entry_frame, text="Selected Account", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)

delete_selected_entry = tkinter.Entry(delete_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 24), width=43)

delete_entry_button = tkinter.Button(
    delete_entry_frame, text="Delete Account",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

delete_cancel_button = tkinter.Button(
    delete_entry_frame, text="Cancel Delete",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Delete Credential Entry Related Widgets and Fields
delete_header_label.place(relx=0.5, rely=0.05, anchor="n")
delete_account_label.place(relx=0.275, rely=0.36, anchor="s")
delete_account_entry.place(relx=0.275, rely=0.42, anchor="s")
delete_username_label.place(relx=0.725, rely=0.36, anchor="s")
delete_username_entry.place(relx=0.725, rely=0.42, anchor="s")
delete_verify_button.place(relx=0.5, rely=0.5, anchor="s")
delete_selected_label.place(relx=0.5, rely=0.6425, anchor="s")
delete_selected_entry.place(relx=0.5, rely=0.7, anchor="s")
delete_entry_button.place(relx=0.5, rely=0.8, anchor="s")
delete_cancel_button.place(relx=0.5, rely=0.95, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Search Existing Entry Frame ==============================================

# Creating Search Credential Related Widgets and Fields
search_header_label = tkinter.Label(
    search_entry_frame, text="Enter Account Information",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)

search_entry_label = tkinter.Label(
    search_entry_frame, text="Account Nickname", bg="#708090", fg="#FFFFFF", font=("Quicksand", 30), pady=5)

search_entry = tkinter.Entry(search_entry_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 30))

search_entry_button = tkinter.Button(
    search_entry_frame, text="Search Account", bg="#FFFFFF", fg="#181818", font=("Quicksand", 18))

search_entry_all_button = tkinter.Button(
    search_entry_frame, text="Show Accounts", bg="#FFFFFF", fg="#181818", font=("Quicksand", 18))

search_result_text = tkinter.Text(
    search_entry_frame, height=10, width=65, bg="#181818", fg="#FFFFFF", font=("Quicksand", 18))

search_cancel_button = tkinter.Button(
    search_entry_frame, text="Close Search",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 18), command=change_frame_home)

# Placing Search Credential Related Widgets and Fields
search_header_label.place(relx=0.5, rely=0.05, anchor="n")
search_entry_label.place(relx=0.5, rely=0.35, anchor="s")
search_entry.place(relx=0.5, rely=0.43, anchor="s")
search_entry_button.place(relx=0.359, rely=0.5, anchor="s")
search_entry_all_button.place(relx=0.645, rely=0.5, anchor="s")
search_result_text.place(relx=0.5, rely=0.89, anchor="s")
search_cancel_button.place(relx=0.5, rely=0.975, anchor="s")

# ======================================================================================================================

# ======================================================================================================================

# =========================================== Generate New Password Frame ==============================================

# Creating Generate Password Related Widgets and Fields
generate_password_label = tkinter.Label(
    generate_password_frame, text="Generate New Password",
    bg="#708090", fg="#FFFFFF", font=("Quicksand", 50, "bold"), pady=50)

new_password_label = tkinter.Label(
    generate_password_frame, text="New Password", bg="#708090", fg="#FFFFFF", font=("Quicksand", 36), pady=5)

new_password_entry = tkinter.Entry(generate_password_frame, bg="#181818", fg="#FFFFFF", font=("Quicksand", 36))

generate_new_password_button = tkinter.Button(
    generate_password_frame, text="Generate Password", bg="#FFFFFF", fg="#181818", font=("Quicksand", 22))

copy_new_password_button = tkinter.Button(
    generate_password_frame, text="Copy New Password", bg="#FFFFFF", fg="#181818", font=("Quicksand", 22))

generate_password_cancel_button = tkinter.Button(
    generate_password_frame, text="Close Password Generator",
    bg="#FFFFFF", fg="#181818", font=("Quicksand", 30), command=change_frame_home)

# Placing Generate Password Related Widgets and Fields
generate_password_label.place(relx=0.5, rely=0.05, anchor="n")
new_password_label.place(relx=0.5, rely=0.4, anchor="s")
new_password_entry.place(relx=0.5, rely=0.5, anchor="s")
generate_new_password_button.place(relx=0.345, rely=0.625, anchor="s")
copy_new_password_button.place(relx=0.65, rely=0.625, anchor="s")
generate_password_cancel_button.place(relx=0.5, rely=0.9, anchor="s")

# ======================================================================================================================

pass_stash_window.mainloop()
