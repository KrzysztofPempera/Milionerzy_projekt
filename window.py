from tkinter import *
from tkinter import messagebox
from engine_ import *
import random

##main interface class
class Window(Frame):

    def __init__(self, master):     ##interface class constructor
        Frame.__init__(self,master)


        self.master.title("MILIONERZY")     ##setting window title

        self.question_frame = Entry(master,font=("TimesNewRoman",10))
        self.question_tag_label = Label(master,font=("TimesNewRoman",20),text ="Pytanie nr")        ##definig question frame and question tag
        self.question_tag_number = Label(master,font=("TimesNewRoman",20),text ="")

        self.question_frame.place(x= 50,y=40,width = 700)
        self.question_tag_label.place(x= 323,y=0)       ##placing question frame and test? note
        self.question_tag_number.place(x= 450,y=0)

        self.question_frame.configure(state="disabled", disabledbackground="white", disabledforeground="black")      ##disabling question frame edit and setting proporties

        self.fifty_used = False
        self.phone_used = False
        self.public_used = False

        self.initButtons(master)        ##calling method to create buttons
        self.initScoreScreen(master)        ##calling method to create score frames

        self.setGame(master)

    def setGame(self,master):     ##game setting method
        engine.random_question()

        self.questionFrameEdit(engine.question)
        self.questionTagNumberEdit(engine.number_questionChcek()+1)
        self.buttonReplace()
        self.scoreScreenSet()
        self.answerButtonSet()


    def scoreScreenSet(self):       ##setting score screen
        self.prize_value.config(text=engine.stan_kontaCheck())
        self.guaranteed_prize_value.config(text = engine.guaranted_cashCheck())

    def questionTagNumberEdit(self,question_tag_number_change):     #changing question indicator
        self.question_tag_number.config(text=question_tag_number_change)

    def answerButtonClick(self,master,ans):        ##method setting up answer button mechanics and looping game
        engine.check_answer(ans)
        if (engine.loss == True):
            self.loosingScreen(master)
        elif engine.scoreCheck() == 12:
            self.winningScreen(master)
        else:
            engine.questionFunction()
            engine.bank()
            engine.question_remove()
            self.setGame(master)

    def answerButtonSet(self):      ##setting buttons with answers
        if engine.scoreCheck() >= 0  and engine.scoreCheck() <= 3:
            self.A_button.config(text =engine.question_answer_base_easy[engine.position][0])
            self.B_button.config(text =engine.question_answer_base_easy[engine.position][1])
            self.C_button.config(text =engine.question_answer_base_easy[engine.position][2])
            self.D_button.config(text =engine.question_answer_base_easy[engine.position][3])
        elif engine.scoreCheck() >= 4  and engine.scoreCheck() <= 7:
            self.A_button.config(text =engine.question_answer_base_medium[engine.position][0])
            self.B_button.config(text =engine.question_answer_base_medium[engine.position][1])
            self.C_button.config(text =engine.question_answer_base_medium[engine.position][2])
            self.D_button.config(text =engine.question_answer_base_medium[engine.position][3])
        elif engine.scoreCheck() >= 8  and engine.scoreCheck() <= 11:
            self.A_button.config(text =engine.question_answer_base_hard[engine.position][0])
            self.B_button.config(text =engine.question_answer_base_hard[engine.position][1])
            self.C_button.config(text =engine.question_answer_base_hard[engine.position][2])
            self.D_button.config(text =engine.question_answer_base_hard[engine.position][3])

    def changeButtonStyle(self,button_change,colour):        ##method to change button appearance via button press
        button_change.config(bg = colour)

    def questionFrameEdit(self,question_frame_change):      ##method to change question frame text via button press
        self.question_frame.configure(state="normal")        ##unlocking question frame
        self.question_frame.delete(0,END)                    ##deleting whats inside
        self.question_frame.insert(0,question_frame_change)  ##inserting new text
        self.question_frame.configure(state="disabled")      ##locking question frame

    def winningScreen(self,master):     ##method which shows ending screen after player wins
        self.A_button.destroy()
        self.B_button.destroy()
        self.C_button.destroy()
        self.D_button.destroy()
        self.phone_button.destroy()
        self.public_button.destroy()            ##deleting all widgets from main frame
        self.fifty_button.destroy()
        self.prize_value_frame.destroy()
        self.guaranteed_prize_value_frame.destroy()
        self.question_tag_label.destroy()
        self.question_tag_number.destroy()
        self.question_frame.destroy()

        self.winning_score_screen_label = Label(master,font=("TimesNewRoman",25),text ="GRATULACJE\n WYGRAŁEŚ 1 000 000$")
        self.winning_score_screen_label.place(x=200, y= 200)


        self.quit_button = Button(master, text="EXIT", height = 5, width = 10 ,bg="lightgrey",command=  self.windowExit)
        self.quit_button.pack(side=BOTTOM)

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
        self.question_tag_label.destroy()
        self.question_tag_number.destroy()
        self.question_frame.destroy()

        self.loosing_score_screen_frame = LabelFrame(master,font =("TimesNewRoman",25),text = "Przegrałeś")
        self.loosing_score_screen_frame.place(x=150, y=100,width=500,height = 300)

        self.loosing_score_screen = Label(self.loosing_score_screen_frame,font=("TimesNewRoman",15),text ="Otrzymujesz nagrodę w wyskokości:")      ##displaying engines score
        self.loosing_score_screen.pack(side=TOP)

        self.loosing_score_screen_price = Label(self.loosing_score_screen_frame,font=("TimesNewRoman",15),text =engine.guaranted_cashCheck())
        self.loosing_score_screen_price.pack(side=TOP)



        self.quit_button = Button(master, text="EXIT", height = 5, width = 10 ,bg="lightgrey",command=  self.windowExit)
        self.quit_button.pack(side=BOTTOM)

    def initButtons(self,master):       ##method to create buttons
        self.A_button = Button(master, text=temp1,  bg="lightblue",command=lambda: self.answerButtonClick(master,0) )
        self.A_button.place(x=50, y=125, width=225, height=75,)

        self.B_button = Button(master, text=temp1,  bg="lightblue",command=lambda: self.answerButtonClick(master,1))
        self.B_button.place(x=325, y=125, width=225, height=75,)

        self.C_button = Button(master, text=temp1,  bg="lightblue",command=lambda: self.answerButtonClick(master,2))
        self.C_button.place(x=50, y=225, width=225, height=75,)

        self.D_button = Button(master, text="NICE",  bg="lightblue",command=lambda: self.answerButtonClick(master,3))
        self.D_button.place(x=325, y=225, width=225, height=75,)

        self.phone_button = Button(master, text="Telefon do przyjaciela",  bg="lightblue",command=lambda:[self.changeButtonStyle(self.phone_button,"red"),self.phoneLifeline()])
        self.phone_button.place(x=50, y=450, width=200, height=75,)

        self.public_button = Button(master, text="Pytanie do publiczności",  bg="lightblue",command=lambda:[self.changeButtonStyle(self.public_button,"red"),self.publicLifeline()])
        self.public_button.place(x=275, y=450, width=200, height=75,)

        self.fifty_button = Button(master, text="50-50",  bg="lightblue", command=lambda:[self.changeButtonStyle(self.fifty_button,"red"),self.fiftyLifeline()])
        self.fifty_button.place(x=500, y=450, width=200, height=75,)

    def initScoreScreen(self,master):       ##method to create score screen
        self.prize_value_frame = LabelFrame(master,font =("TimesNewRoman",10),text = "Pytanie za: ")
        self.prize_value_frame.place(x= 600, y =125,width = 175)
        self.prize_value = Label(self.prize_value_frame,font=("TimesNewRoman",15))
        self.prize_value.pack()

        self.guaranteed_prize_value_frame = LabelFrame(master,font =("TimesNewRoman",10),text = "Gwarantowana wygrana: ")
        self.guaranteed_prize_value_frame.place(x= 600, y =200,width = 175)
        self.guaranteed_prize_value = Label(self.guaranteed_prize_value_frame,font=("TimesNewRoman",15))
        self.guaranteed_prize_value.pack()

    def buttonReplace(self):
        self.A_button.place(x=50, y=125, width=225, height=75,)
        self.B_button.place(x=325, y=125, width=225, height=75,)
        self.C_button.place(x=50, y=225, width=225, height=75,)
        self.D_button.place(x=325, y=225, width=225, height=75,)
    
    '''
    def buttonTest(self,master):
        self.test_button = Button(master, text=temp1,  bg="lightblue",command = self.A_button.place_forget)
        self.test_button.place(x=150, y=300, width=225, height=75,) 
    '''

    def fiftyLifeline(self):
        if self.fifty_used == True:
            print("used")
        elif self.fifty_used == False:
            self.hideButtons(engine.answer_ans)
            self.fifty_used = True

    def phoneLifeline(self):
        self.button_list = ["odpowiedź A","odpowiedź B","odpowiedź C","odpowiedź D"]

        if self.phone_used == True:
            print("used")
        elif self.phone_used == False:
            correct_chance = random.randint(0,100)
            if correct_chance >40:
                self.temp = "Moim zdaniem "+self.button_list[engine.answer_ans]+" jest poprawna"
                messagebox.showinfo("Telefon do przyjaciela",self.temp)

            elif correct_chance <40:
                self.temp = "Moim zdaniem "+self.button_list[random.randint(0,3)]+" jest poprawna"
                messagebox.showinfo("Telefon do przyjaciela",self.temp)

            self.phone_used = True
    
    def publicLifeline(self):
        if self.public_used == True:
            print("used")
        elif self.public_used == False:
            self.percentage = 100
            self.public_answer = []
            for i in range (0,4):
                self.temporary_percentage = random.randrange(self.percentage)
                self.public_answer.append(str(self.temporary_percentage))
                self.percentage = self.percentage - self.temporary_percentage

            self.temp = self.public_answer[0]+"% publiczności twierdzi,że odpowiedź A jest prawidłowa\n"+self.public_answer[1]+"% publiczności twierdzi,że odpowiedź B jest prawidłowa\n"+self.public_answer[2]+"% publiczności twierdzi,że odpowiedź C jest prawidłowa\n"+self.public_answer[3]+"% publiczności twierdzi,że odpowiedź D jest prawidłowa\n"
            messagebox.showinfo("Pytanie do publiczności",self.temp)
            
            self.public_used = True

    def hideButtons(self,ans):
        self.button_list = [self.A_button,self.B_button,self.C_button,self.D_button]
        if ans == 0:
            self.button_list.remove(self.A_button)
        elif ans == 1:
            self.button_list.remove(self.B_button)
        elif ans == 2:
            self.button_list.remove(self.C_button)
        elif ans == 3:
            self.button_list.remove(self.D_button)

        self.temp = random.choice(self.button_list)
        self.temp.place_forget()
        self.button_list.remove(self.temp)
        self.temp = random.choice(self.button_list)
        self.temp.place_forget()

    def windowExit(self):       ##method which exits the game
       exit()


class splashScreen(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)                 
        self.master = master
        
        przycisk_start = Button(master, text = "START",command =lambda: [self.quit(),self.start()])
        przycisk_start.place(x= 100,y=175,width =200, height = 75)

    def start(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.app = Window(self.root)
        self.root.mainloop()
    def quit(self):
        self.master.destroy()


   
    
       
    
temp1 = "TEMP BUTTON"

engine = mechanizm()

glowne_okno = Tk()
glowne_okno.title("Moje okno")
glowne_okno.geometry("400x300")
app2 = splashScreen(glowne_okno)

glowne_okno.mainloop()
