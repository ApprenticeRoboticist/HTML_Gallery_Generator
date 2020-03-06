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


def rename():
    i = 1
    try:
        for filename in os.listdir(os.getcwd()):
            destined_name = str(i) + ".jpg"
            source = filename

            os.rename(source, destined_name)
            i += 1
    except:
        messagebox.showinfo("Błąd", "Zdjęcia zostały już wcześniej ponumerowane!")


def main():
    main_window = Tk()

    # ustawienia glownego okna
    main_window.title("HTML photogallery generator")
    main_window.geometry("500x550+500+250")
    main_window.resizable(width=False, height=False)

    # ramki w aplikacji

    upper_frame = LabelFrame(main_window, text="Step 1", relief=GROOVE)
    middle_frame = LabelFrame(main_window, text="Step 2", relief=GROOVE)
    lower_frame = LabelFrame(main_window, text="Nosacz", relief=GROOVE)

    # zmienne globalne
    global folder_path
    folder_path = StringVar()

    # Layout
    # step1
    btn1 = Button(upper_frame, text="wybierz lokalizację", command=lambda: [set_dir(), btn2.config(state=NORMAL)])
    btn1.pack(padx=15, side=LEFT)

    lbl1 = Label(upper_frame, width=45, height=2, bg='SlateGray2', textvariable=folder_path)
    lbl1.pack(side=TOP, pady=7, padx=10)

    # step 2

    lbl2 = Label(middle_frame, width=30, height=2, text="Czy chcesz ponumerować zdjęcia?", font=("Tahoma", 10))
    lbl2.pack(side=LEFT, pady=7, padx=15)

    btn2 = Button(middle_frame, text="TAK", height=1, width=20, fg="black", command=rename, state=DISABLED)
    btn2.pack(padx=30, side=LEFT)
    #btn2.config(state=NORMAL)

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
