import tkinter as tk
from tkinter import ttk
import signUpPage
import TkinterTemplate

# enter signUpPage
def get_signup():
    signUpPage.SignupPage()


# call to check id
def getlogin(username, password):
    # if your want to run the script as it is set validation = True
    validation = validate(username, password)
    if validation:
        tk.messagebox.showinfo("Login Successful",
                                   "Welcome {}".format(username))
        # 顯示隱藏的root window
        root.deiconify()
        # login window不會再用，銷毀
        login.destroy()
    else:
        tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")


# validator
def validate(username, password):
    # Checks the text file for a username/password combination.
    try:
        with open("credentials.txt", "r") as credentials:
            for line in credentials:
                line = line.split(",")
                if line[1] == username and line[3] == password:
                    return True
            return False
    except FileNotFoundError:
        print("You need to Register first or amend Line 71 to     if True:")
        return False

# LoginUI
class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#FFFFF0", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("800x600")  # Sets window size to 800w x 600h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "white"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "white",
                       "foreground": "#000000"}

        # this is the frame that holds all the login details and buttons
        frame_login = tk.Frame(main_frame, bg="white", relief="groove", bd=2)  
        frame_login.pack(expand=1)

        label_title = tk.Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin(entry_user.get(), entry_pw.get()))
        button.grid(row=3, column=1, sticky='e')

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        signup_btn.grid(row=3, column=2)

    
# 啟動程式
# 製作兩個window, one for logIn, another one is mainAPP
login = LoginPage()
login.title("登入空氣品質查詢app")

root = TkinterTemplate.MyApp()
root.withdraw() # 隱藏window，登入成功後才open
root.title("空氣品質查詢app")

root.mainloop() # keep window working

    
        

