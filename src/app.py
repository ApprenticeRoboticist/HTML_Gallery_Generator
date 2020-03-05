import os
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

folder_path = None


def set_dir():
    # pobiera i zmienia sciezke lokalizacji plikow
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    os.chdir(folder_path.get())
    print(os.getcwd())


def main():
    # ustawienia glownego okna
    main_window = Tk()
    main_window.title("HTML photogallery generator")
    main_window.geometry("500x550+500+250")

    #main_window.configure(background="gray")
    main_window.resizable(width=False, height=False)

    # ramki w aplikacji

    upper_frame = LabelFrame(main_window, text="Step 1", relief=GROOVE)
    middle_frame = LabelFrame(main_window, text="Step 2", relief=GROOVE)
    lower_frame = LabelFrame(main_window, text="Nosacz", relief=GROOVE)

    # zmienne
    global folder_path
    folder_path = StringVar()

    # przyciski
    btn1 = Button(upper_frame, text="wybierz lokalizację", command=set_dir)
    btn1.pack(padx=15, side=LEFT)

    btn2 = Button(middle_frame, text="say hi")
    btn2.pack(padx=15, side=LEFT)

    # naklejki

    lbl1 = Label(upper_frame, width=45, height=2, bg='SlateGray2', textvariable=folder_path)
    lbl1.pack(side=TOP, pady=7, padx=10)

    # super motywujacy obrazek
    my_img = ImageTk.PhotoImage(Image.open("images/nosacz.jpg"))
    new_image = Label(lower_frame, image=my_img)
    new_image.pack(padx=5)

    # inicjalizacja ramek
    upper_frame.pack(padx=10, pady=10, fill=X)
    middle_frame.pack(padx=10, fill=X)
    lower_frame.pack(padx=10, pady=10)

    main_window.mainloop()


if __name__ == '__main__':
    main()
