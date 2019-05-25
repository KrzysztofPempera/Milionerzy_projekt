from tkinter import *
##import engine

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.entry = Entry(master, width = 20,font=("TimesNewRoman",25))
        self.entry.grid(row = 1, column = 3, columnspan = 6)
        self.e2 = Entry(master, width = 20,font=("TimesNewRoman",25),text="test")
        self.e2.grid(row = 3, column = 6, columnspan = 6,sticky = "E")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.grid()


root = Tk()
root.geometry("800x600")
root.resizable(0, 0)
app = Window(root)
root.mainloop()