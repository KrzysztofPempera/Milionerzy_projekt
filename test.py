'''
from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
    

    
app = tk.Tk()
labelExample = tk.Button(app, text="0")

def change_label_number(num):
    counter = int(str(labelExample['text']))
    counter += num
    labelExample.config(text=str(counter))
    
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=lambda: change_label_number(2))

buttonExample.pack()
labelExample.pack()
app.mainloop()

while True:
    player.random_question()
    player.question()
    player.answer()
    player.check_answer()
    player.bank()
    player.question_remove()
'''
from basic_var import *
a = 1
b = 1
if a  == b :
    score += 1

print(score)
