import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

#with CustomOpen('file') as f:
    #contents = f.read()


class App(Frame):

    def __init__(self):
        super().__init__()

        # inicjalizacja zmiennych
        self.e_message1 = StringVar()

        self.e_message2 = StringVar()
        self.directory = os.getcwd()
        # inicjalizacja ramki aplikacji
        self.init_ui()

    def init_ui(self):

        self.master.title("HTML Gallery Generator")
        self.pack(fill=BOTH, expand=True)

        lab1 = Label(self, text="Wprowadź scieżkę do folderu ze zdjęciami", fg="Blue", pady="10")
        lab1.pack(side=TOP)

        lab2 = Label(self, text=self.directory, fg="Blue", pady="10")
        lab2.pack(side=BOTTOM)

        entrybox1 = Entry(self, textvariable=self.directory, fg="Yellow", bg="Black", width=30)
        entrybox1.pack(side=TOP)
        entrybox1.focus()
        self.directory = entrybox1.get()

        btn1 = Button(self, text="Zmień scieżkę!", command=self.change_dir(), activeforeground="Red", activebackground="Pink")
        btn1.pack()

        #my_img = ImageTk.PhotoImage(Image.open("nosacz.jpg"))
        #new_image = Label(image=my_img)
        #new_image.pack()

    def print_message(self):
        message = self.e_message1.get()
        messagebox.showinfo("Błąd", message)

    def set_dir(self):
        pass



def main():
    root = Tk()
    root.geometry("350x300+500+250")
    root.resizable(width=False, height=False)
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()
