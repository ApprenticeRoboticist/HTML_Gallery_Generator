import os
from tkinter import *
from tkinter import messagebox, filedialog, scrolledtext
from tkinter.ttk import Combobox
import time


class App:
    def __init__(self, master):
        """ main window settings"""
        master.title("HTML Photogallery Generator")
        master.geometry("500x650+550+125")
        master.resizable(width=False, height=False)

        """ Variables """
        self.folder_path = StringVar()
        self.title = ""
        self.step_list = []

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
        self.label3 = Label(self.middle2_mini_frame, width=33, height=1,
                            text="Enter the name of the instruction", font=("Tahoma", 10))
        self.entry1 = Entry(self.middle2_mini_frame, width=30, textvariable=self.title, state=DISABLED)
        self.button3 = Button(self.middle_frame2, text="Submit the name", height=1, width=20, fg="black",
                              state=DISABLED, relief=GROOVE,
                              command=lambda: [self.get_name(self.entry1.get()), self.final_button.config(state=NORMAL)])

        """ Step4 widgets"""
        self.label4 = Label(self.lower_mini_frame1, width=40, height=1,
                            text="Choose the amount of photos in given step:", font=("Tahoma", 10))
        self.combo = Combobox(self.lower_mini_frame1, values=(1, 2, 3, 4, 5, 6, 7, 8, 9))
        self.combo.current(0)
        self.button4 = Button(self.lower_mini_frame2, text="Add step", width=15, relief=GROOVE,
                              command=lambda: [self.add_value(self.combo.get()),
                                               self.txt.insert(INSERT, "\n" + str(len(self.step_list)) +
                                                               " step contains " + self.step_list[-1] +
                                                               " photos!"), self.txt.see(END)])
        self.button5 = Button(self.lower_mini_frame2, text="Delete previous", width=15, relief=GROOVE,
                              command=lambda: [self.txt.delete(str(len(self.step_list)+1)+".0", "end")
                                               if len(self.step_list) > 0 else None, self.delete_value()])
        self.button6 = Button(self.lower_mini_frame2, text="Delete all steps", width=15, relief=GROOVE,
                              command=lambda: [self.clear_all(), self.txt.delete("2.0", "end")])
        self.txt = scrolledtext.ScrolledText(self.lower_frame, width=50, height=12)
        self.txt.insert(INSERT, "Amount of photos in given step:")

        """ Ultimate button """
        self.final_button = Button(master, text="Generate the instruction", width=40, height=2, relief=GROOVE,
                                   state=DISABLED, command=lambda: self.generate_form())

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

        self.label4.pack(side=LEFT, padx=10, pady=5)
        self.combo.pack(side=RIGHT, padx=25, pady=15)
        self.button4.pack(side=LEFT, padx=22, pady=5)
        self.button5.pack(side=LEFT, padx=22, pady=5)
        self.button6.pack(side=LEFT, padx=22, pady=5)
        self.txt.pack(side=TOP, padx=15, pady=10)

        self.final_button.pack(side=BOTTOM, padx=30, pady=15)

        self.upper_frame.pack(side=TOP, padx=10, pady=10, fill=X)
        self.middle_frame1.pack(side=TOP, padx=10, fill=X)
        self.middle_frame2.pack(side=TOP, padx=10, fill=X)
        self.middle2_mini_frame.pack(side=TOP, fill=X)
        self.lower_frame.pack(side=TOP, padx=10, fill=X)
        self.lower_mini_frame1.pack(side=TOP)
        self.lower_mini_frame2.pack(side=TOP)

    def set_dir(self):
        """ Sets given directory """
        try:
            filename = filedialog.askdirectory()
            self.folder_path.set(filename)
            os.chdir(self.folder_path.get())
            print(os.getcwd())
        except OSError:
            print("OS Error")

    @staticmethod
    def rename():
        """ Renames photos"""
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
        elif len(value) > 25:
            messagebox.showinfo("Error", "Name can't be bigger than 24 letters long!")
        else:
            self.title = value
            print(self.title)

    def add_value(self, value):
        """Adds the value to the list containing amount of photos for each step """
        self.step_list.append(value)
        print(self.step_list)

    def delete_value(self):
        """ Removes last value from the list containing amount of photos for each step """
        try:
            del self.step_list[-1]
            print(self.step_list)
        except IndexError:
            messagebox.showinfo("Error", "There's nothing to delete!")

    def clear_all(self):
        """ Clears the list containing amount of photos for each step """
        self.step_list.clear()
        print(self.step_list)

    def generate_form(self):
        form = FormGenerator(self.title, self.step_list)
        form.beginning_html()
        form.filling_html()
        form.ending_html()


class FormGenerator:
    def __init__(self, title, step_list):
        self.title = title
        self.step_list = step_list

    def beginning_html(self):
        new_html = open(f"{self.title}.html", 'w')
        new_html.write(f"""<html>
        <head>
        <META HTTP-EQUIV="content-type" CONTENT="text/html; charset=iso-8859-2">
        <title>{self.title}</title>
        <!-- The spell is: "Welcome to Uganda"  -->
        </head>
        <body style="font-family: Verdana; font-size: 10pt">
        <p><b><font face="Arial" size="7">{self.title}</font></b></p>
        """)
        new_html.close()

    def filling_html(self):
        list = [int(i) for i in self.step_list]
        doc = open(f"{self.title}.html", 'a')
        step_amount = len(list)
        print(f"Ilość kroków w tej instrukcji wynosi: {step_amount}.")
        i = 1
        list_iter = 0  # index of the list (instruction step)
        photo_count = 1  # number of pasted photo (independent from step)

        while i <= step_amount:

            if i == 1:
                doc.write(f"""  <p><b><font face="Arial" size="7">{i}</font></b></p>\n""")
                for x in range(1, list[int(list_iter)] + 1):
                    doc.write(f"""          <p><img border="1" src="{photo_count}.jpg" width="700"></p>\n""")
                    print(f"step: {i} photo: {photo_count}")
                    photo_count += 1
                    time.sleep(0.1)
            else:
                doc.write(f"""
        <hr>
            <p><b><font face="Arial" size="7">{i}</font></b></p>\n""")
                for x in range(1, list[list_iter] + 1):
                    doc.write(f"""          <p><img border="1" src="{photo_count}.jpg" width="700"></p>\n""")
                    print(f"step: {i} photo: {photo_count}")
                    photo_count += 1
                    time.sleep(0.1)

            i += 1
            list_iter += 1

        doc.close()

    def ending_html(self):
        doc = open(f"{self.title}.html", 'a')
        doc.write(f"""
        </body>
        <!-- Autor Piotr Adamiec -->
    </html> """)
        doc.close()


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
