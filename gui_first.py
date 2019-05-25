from tkinter import *
##import engine 



class Window(Frame):
    def __init__(self, master = NONE):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()
    
    def init_window(self):
        self.master.title("MILIONERZY")

        self.pack(fill=BOTH, expand = 1)

        quitButton = Button(self, text="QUIT",command = self.client_exit, height = 5, width = 10)
        quitButton.place(x=0, y=0)

        self.showStartingText()

        questionText = StringVar()
        questionText.set("hello")
        questionFrame = Entry( bg = "blue", fg = "white", width = 500,textvariable = questionText)
        questionFrame.place(x=300, y=300)

       
    def showStartingText(self):
        startingText = "HELLO TO OUR GAME"

        showText = Label(self, text = startingText)
        showText.pack()
   

    def client_exit(self):
        exit()



root = Tk()
root.geometry("800x600")
root.resizable(0, 0)
root.configure(background = 'white')

app = Window(root)

root.mainloop()





