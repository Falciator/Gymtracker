from tkinter import *

def userUI():
    win1 = Tk()
    win1.title('Login Screen')
    win1.geometry("500x220")
    win1.resizable(False, False)

    name_label = Label(win1, text="Name")
    name_label.grid(row=1, column=0, padx=10, pady=20, sticky="W")

    password_label = Label(win1, text="Password")
    password_label.grid(row=2, column=0, padx=10, pady=20, sticky="W")

    name_entry = Entry(win1, width="30")
    name_entry.grid(row=1, column=1, padx=30, pady=20, sticky="E")

    password_entry = Entry(win1, width="30", show='*')
    password_entry.grid(row=2, column=1, padx=30, pady=20, sticky="E")

    forgot_button = Button(win1, text="forgot password", width=20, command=lambda: reset_pass())
    forgot_button.grid(row=3, column=1, padx=10, pady=10)

    submit_button = Button(win1, text="Submit", width=20, command=lambda: submit_details(win1, password_entry, name_entry))
    submit_button.grid(row=3, column=2, padx=10, pady=10)


    win1.eval('tk::PlaceWindow . center')

    mainloop()



if __name__ == "__main__":  # for testing
    userUI()