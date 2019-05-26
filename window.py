from tkinter import *
##import engine

##main interface class
class Window(Frame):

    
    def __init__(self, master):     ##interface class constructor
        Frame.__init__(self,master)

        self.master.title("MILIONERZY")     ##setting window title

        self.entry = Entry(master,font=("TimesNewRoman",20))
        self.e2 = Label(master,font=("TimesNewRoman",20),text ="all your base are belong to us")        ##definig question frame and test? note

        self.entry.place(x= 50,y=40,width = 700)                
        self.e2.place(x= 100,y=0,width = 600)       ##placing question frame and test? note

        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")      ##disabling question frame edit and setting proporties       
        

        self.initButtons(master)        ##calling method to create buttons
        self.initScoreScreen(master)        ##calling method to create score frames

    def changeTestLabel(self,n):        ##method to change test? note via button press
        self.e2.config(text =n)

    def changeButtonStyle(self,button_change):        ##method to change button appearance via button press        
        button_change.config(bg = "red")

    def questionFrameEdit(self,question_frame_change):      ##method to change question frame text via button press
        self.entry.configure(state="normal")        ##unlocking question frame
        self.entry.delete(0,END)                    ##deleting whats inside
        self.entry.insert(0,question_frame_change)  ##inserting new text      
        self.entry.configure(state="disabled")      ##locking question frame

    def loosingScreen(self,master):     ##method which shows ending screen after players loss
        self.A_button.destroy()
        self.B_button.destroy()
        self.C_button.destroy()
        self.D_button.destroy()
        self.phone_button.destroy()
        self.public_button.destroy()            ##deleting all widgets from main frame
        self.fifty_button.destroy()
        self.prize_value_frame.destroy()
        self.guaranteed_prize_value_frame.destroy()
        self.e2.destroy()
        self.entry.destroy()

        self.loosing_score_screen_frame = LabelFrame(master,font =("TimesNewRoman",25),text = "Przegrałeś")
        self.loosing_score_screen_frame.place(x=150, y=100,width=500,height = 300)
        
        self.loosing_score_screen = Label(self.loosing_score_screen_frame,font=("TimesNewRoman",15),text ="Otrzymujesz nagrodę w wyskokości:")      ##displaying players score
        self.loosing_score_screen.pack(side=TOP)

        self.loosing_score_screen_price = Label(self.loosing_score_screen_frame,font=("TimesNewRoman",15),text =temp1)
        self.loosing_score_screen_price.pack(side=TOP)

        self.quit_button = Button(master, text="EXIT", height = 5, width = 10 ,bg="lightgrey",command=lambda:  self.windowExit())
        self.quit_button.pack(side=BOTTOM)

    def initButtons(self,master):       ##method to create buttons 
        self.A_button = Button(master, text=temp1,  bg="lightblue")
        self.A_button.place(x=50, y=125, width=225, height=75,)
    
        self.B_button = Button(master, text=temp1,  bg="lightblue")
        self.B_button.place(x=325, y=125, width=225, height=75,)

        self.C_button = Button(master, text=temp1,  bg="lightblue")
        self.C_button.place(x=50, y=225, width=225, height=75,)

        self.D_button = Button(master, text="NICE",  bg="lightblue", command=lambda: self.loosingScreen(master))
        self.D_button.place(x=325, y=225, width=225, height=75,)
        
        self.phone_button = Button(master, text=temp1,  bg="lightblue",command=lambda:[self.changeButtonStyle(self.phone_button)])
        self.phone_button.place(x=50, y=450, width=200, height=75,)
    
        self.public_button = Button(master, text=temp1,  bg="lightblue",command=lambda:[self.changeButtonStyle(self.public_button)])
        self.public_button.place(x=275, y=450, width=200, height=75,)

        self.fifty_button = Button(master, text="SUDO rm -rf /*",  bg="lightblue", command=lambda:[self.changeButtonStyle(self.fifty_button)] )
        self.fifty_button.place(x=500, y=450, width=200, height=75,)
        
    def initScoreScreen(self,master):       ##method to create score screen
        self.prize_value_frame = LabelFrame(master,font =("TimesNewRoman",10),text = "Pytanie za: ")
        self.prize_value_frame.place(x= 600, y =125,width = 175)
        self.prize_value = Label(self.prize_value_frame,font=("TimesNewRoman",15),text ="1000$")
        self.prize_value.pack()

        self.guaranteed_prize_value_frame = LabelFrame(master,font =("TimesNewRoman",10),text = "Gwarantowana wygrana: ")
        self.guaranteed_prize_value_frame.place(x= 600, y =200,width = 175)
        self.guaranteed_prize_value = Label(self.guaranteed_prize_value_frame,font=("TimesNewRoman",15),text ="1000$")
        self.guaranteed_prize_value.pack()

    def windowExit(self):       ##method which exits game
       exit()

temp1 = "TEMP BUTTON"
root = Tk()
root.geometry("800x600")
root.resizable(0, 0)
##root.configure(background ="white")
app = Window(root)
root.mainloop()