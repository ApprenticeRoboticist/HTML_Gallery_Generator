import os
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox


class App:
    def __init__(self, master):
        master.title("HTML Photogallery Generator")
        master.geometry("500x650+550+125")
        master.resizable(width=False, height=False)

        """ Variables """
        self.folder_path = StringVar()
        self.title = ""

        """ Widget frames """
        self.upper_frame = LabelFrame(master, text="Step 1", relief=GROOVE)

        self.middle_frame1 = LabelFrame(master, text="Step 2", relief=GROOVE)

        self.middle_frame2 = LabelFrame(master, text="Step 3", relief=GROOVE)
        self.middle2_mini_frame = LabelFrame(self.middle_frame2, relief=FLAT)

        self.lower_frame = LabelFrame(master, text="Step 4", relief=GROOVE)
        self.lower_mini_frame1 = LabelFrame(self.lower_frame, relief=FLAT)
        self.lower_mini_frame2 = LabelFrame(self.lower_frame, relief=FLAT)

        """ Step1 widgets """
        self.button1 = Button(self.upper_frame, text="Choose path to file",
                              command=lambda: [self.set_dir(), self.button2.config(state=NORMAL),
                                               self.button3.config(state=NORMAL), self.entry1.config(state=NORMAL)],
                              relief=GROOVE)

        self.label1 = Label(self.upper_frame, width=45, height=2, bg='SlateGray2', textvariable=self.folder_path)

        """ Step2 widgets """

        self.label2 = Label(self.middle_frame1, width=30, height=2, text="Do you want to numerate photos?",
                            font=("Tahoma", 10))
        self.button2 = Button(self.middle_frame1, text="YES", height=1, width=20, fg="black", command=self.rename,
                              state=DISABLED, relief=GROOVE)

        """ Step3 widgets """
        self.label3 = Label(self.middle2_mini_frame, width=25, height=1, text="Name the instruction", font=("Tahoma", 10))
        self.entry1 = Entry(self.middle2_mini_frame, width=35, textvariable=self.title, state=DISABLED)
        self.button3 = Button(self.middle_frame2, text="Submit the name", height=1, width=20, fg="black",
                              state=DISABLED, relief=GROOVE,
                              command=lambda: [self.get_name(self.entry1.get()), self.final_button.config(state=NORMAL)])
        """ Ultimate button """
        self.final_button = Button(master, text="Generate the instruction", width=40, height=2, relief=GROOVE,
                                   state=DISABLED, command=lambda: self.print_message)

        """ GUI init method """
        self.ui_init()

    def ui_init(self):
        """ Organizing layout of widgets """
        self.button1.pack(padx=15, side=LEFT)
        self.label1.pack(side=TOP, pady=7, padx=10)

        self.label2.pack(side=LEFT, pady=7, padx=15)
        self.button2.pack(padx=30, side=LEFT)

        self.label3.pack(side=LEFT)
        self.entry1.pack(side=RIGHT, padx=25, pady=5)
        self.button3.pack(side=BOTTOM, padx=30, pady=5)

        self.final_button.pack(side=BOTTOM, padx=30, pady=15)

        self.upper_frame.pack(side=TOP, padx=10, pady=10, fill=X)
        self.middle_frame1.pack(side=TOP, padx=10, fill=X)
        self.middle_frame2.pack(side=TOP, padx=10, fill=X)
        self.middle2_mini_frame.pack(side=TOP, fill=X)
        self.lower_frame.pack(side=TOP, padx=10, fill=X)

    def set_dir(self):
        """sets given directory"""
        try:
            filename = filedialog.askdirectory()
            self.folder_path.set(filename)
            os.chdir(self.folder_path.get())
            print(os.getcwd())
        except OSError:
            print("OS Error")

    def rename(self):
        """Zmienia nazwy plikow zdjeciowych w wybranym folderze na kolejne liczby zaczynajace sie od 1"""
        i = 1
        try:
            for filename in os.listdir(os.getcwd()):
                if filename.endswith(".jpg"):
                    destined_name = str(i) + ".jpg"
                    source = filename

                    os.rename(source, destined_name)
                    i += 1
        except FileExistsError:
            messagebox.showinfo("Error", "Photos have been already numerated!")

    def get_name(self, value):
        """ Set up instructions name """
        if len(value) <= 2:
            messagebox.showinfo("Error", "Name must be at least 3 letters long!")
        else:
            self.title = value
            print(self.title)

    def print_message(self):
        message = "standard message"
        messagebox.showinfo("Błąd", message)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
