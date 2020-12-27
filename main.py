import tkinter
main_window = tkinter.Tk()

tombol_1 = tkinter.Button(main_window, text = "Main Menu")
tombol_2 = tkinter.Button(main_window, text = "Restart")
tombol_3 = tkinter.Button(main_window, text = "Option")

tombol_1.pack()
tombol_2.pack()
tombol_3.pack()

main_window.mainloop()