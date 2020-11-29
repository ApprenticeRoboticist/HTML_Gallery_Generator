import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# gonna remake this from scratch

class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

#with CustomOpen('file') as f:
    #contents = f.read()


class App:
    def __init__(self, master):
        master.title("HTML Photogallery Generator")
        master.geometry("500x650+550+125")
        master.resizable(width=False, height=False)

        # variables
        self.folder_path = ""

        # app frames
        self.upper_frame = LabelFrame(master, text="Step 1", relief=GROOVE)

        self.middle_frame1 = LabelFrame(master, text="Step 2", relief=GROOVE)

        self.middle_frame2 = LabelFrame(master, text="Step 3", relief=GROOVE)
        self.middle2_mini_frame = LabelFrame(self.middle_frame2, relief=FLAT)

        self.lower_frame = LabelFrame(master, text="Step 4", relief=GROOVE)
        self.lower_mini_frame1 = LabelFrame(self.lower_frame, relief=FLAT)
        self.lower_mini_frame2 = LabelFrame(self.lower_frame, relief=FLAT)

        # step1 widgets
        self.button1 = Button(self.upper_frame, text="Choose path to file", command=self.print_message, relief=GROOVE)

        self.label1 = Label(self.upper_frame, width=45, height=2, bg='SlateGray2', textvariable=self.folder_path)

        # GUI init
        self.ui_init()

    def ui_init(self):
        """Placing all widgets"""
        self.button1.pack(padx=15, side=LEFT)
        self.label1.pack(side=TOP, pady=7, padx=10)

        self.upper_frame.pack(side=TOP, padx=10, pady=10, fill=X)
        self.middle_frame1.pack(side=TOP, padx=10, fill=X)
        self.middle_frame2.pack(side=TOP, padx=10, fill=X)
        self.lower_frame.pack(side=TOP, padx=10, fill=X)

    def print_message(self):
        message = "standard message"
        messagebox.showinfo("Błąd", message)

    def set_dir(self):
        pass


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
