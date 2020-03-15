import os
from tkinter import *
from tkinter import messagebox, filedialog, scrolledtext
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

folder_path = None
title = None


def set_dir():
    # pobiera i zmienia sciezke lokalizacji plikow
    global folder_path
    try:
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        os.chdir(folder_path.get())
        print(os.getcwd())
    except OSError:
        pass


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


def get_name(value):
    """Zbiera dane z okna wejscia w kroku 3 i przypisuje je do zmiennej globalnej title"""
    global title
    title = value
    print(title)


def add_value(chapter_list, value):
    chapter_list.append(value)
    print(chapter_list)


def delete_value(chapter_list):
    del chapter_list[-1]
    print(chapter_list)


def main():
    main_window = Tk()

    # ustawienia glownego okna
    main_window.title("HTML photogallery generator")
    main_window.geometry("500x650+500+125")
    main_window.resizable(width=False, height=False)

    # ramki w aplikacji

    upper_frame = LabelFrame(main_window, text="Step 1", relief=GROOVE)

    middle_frame1 = LabelFrame(main_window, text="Step 2", relief=GROOVE)

    middle_frame2 = LabelFrame(main_window, text="Step 3", relief=GROOVE)
    middle2_mini_frame = LabelFrame(middle_frame2, relief=FLAT)

    lower_frame = LabelFrame(main_window, text="Step 4", relief=GROOVE)
    lower_mini_frame1 = LabelFrame(lower_frame, relief=FLAT)
    lower_mini_frame2 = LabelFrame(lower_frame, relief=FLAT)

    # zmienne globalne
    global folder_path
    folder_path = StringVar()

    # zmienne
    title = ""
    value_list = []

    # Layout
    # step1
    btn1 = Button(upper_frame, text="wybierz lokalizację",
                  command=lambda: [set_dir(), btn2.config(state=NORMAL), btn3.config(state=NORMAL),
                                   en1.config(state=NORMAL)],
                  relief=GROOVE)
    btn1.pack(padx=15, side=LEFT)

    lbl1 = Label(upper_frame, width=45, height=2, bg='SlateGray2', textvariable=folder_path)
    lbl1.pack(side=TOP, pady=7, padx=10)

    # step 2

    lbl2 = Label(middle_frame1, width=30, height=2, text="Czy chcesz ponumerować zdjęcia?", font=("Tahoma", 10))
    lbl2.pack(side=LEFT, pady=7, padx=15)

    btn2 = Button(middle_frame1, text="TAK", height=1, width=20, fg="black", command=rename, state=DISABLED,
                  relief=GROOVE)
    btn2.pack(padx=30, side=LEFT)

    # step 3

    middle2_mini_frame.pack(side=TOP, fill=X)
    lbl3 = Label(middle2_mini_frame, width=25, height=1, text="Podaj nazwę instrukcji", font=("Tahoma", 10))
    lbl3.pack(side=LEFT)
    en1 = Entry(middle2_mini_frame, width=35, textvariable=title, state=DISABLED)
    en1.pack(side=RIGHT, padx=25, pady=5)
    btn3 = Button(middle_frame2, text="Zatwierdź nazwę", height=1, width=20, fg="black",
                  command=lambda: [btn3.config(state=DISABLED), get_name(en1.get()), en1.config(state=DISABLED)],
                  state=DISABLED, relief=GROOVE)
    btn3.pack(side=BOTTOM, padx=30, pady=5)

    # step 4

    lower_mini_frame1.pack(side=TOP)

    lbl4 = Label(lower_mini_frame1, width=40, height=1, text="Wybierz ilość zdjeć w danym kroku instrukcji:", font=("Tahoma", 10))
    lbl4.pack(side=LEFT, padx=10, pady=5)

    combo = Combobox(lower_mini_frame1)
    combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
    combo.current(0)
    combo.pack(side=RIGHT, padx=25, pady=15)

    lower_mini_frame2.pack(side=TOP)

    btn4 = Button(lower_mini_frame2, text="Dodaj krok", width=15, relief=GROOVE, command=lambda: add_value(value_list, combo.get()))
    btn4.pack(side=LEFT, padx=22, pady=5)
    btn5 = Button(lower_mini_frame2, text="Usuń poprzedni", width=15, relief=GROOVE, command=lambda: delete_value(value_list))
    btn5.pack(side=LEFT, padx=22, pady=5)
    btn6 = Button(lower_mini_frame2, text="Usuń wszystkie", width=15, relief=GROOVE)
    btn6.pack(side=LEFT, padx=22, pady=5)

    txt = scrolledtext.ScrolledText(lower_frame, width=40, height=12)
    txt.pack(side=TOP, padx=15, pady=10)
    txt.insert(INSERT, "Tekst inicjalizacyjny")

    # super motywujacy obrazek
    #my_img = ImageTk.PhotoImage(Image.open("images/nosacz.jpg"))
    #new_image = Label(right_frame, image=my_img)
    #new_image.pack(padx=5)

    # inicjalizacja ramek
    upper_frame.pack(side=TOP, padx=10, pady=10, fill=X)
    middle_frame1.pack(side=TOP, padx=10, fill=X)
    middle_frame2.pack(side=TOP, padx=10, fill=X)
    lower_frame.pack(side=TOP, padx=10, pady=10, fill=X)

    main_window.mainloop()


if __name__ == '__main__':
    main()
