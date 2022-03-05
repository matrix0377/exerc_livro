from tkinter import *
import pygame.mixer

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

number_asked = 0
number_correct = 0
number_wrong = 0

def play_correct_sound():
    global number_correct
    global number_asked
    number_correct = number_correct + 1
    number_asked = number_asked + 1
    correct_s.play()
    
    
def play_wrong_sound():
    global number_wrong
    global number_asked
    number_wrong = number_wrong + 1
    number_asked = number_asked + 1
    wrong_s.play()
    

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

l = Label(app, text='When you are ready, click on the buttons!', height = 3)
l.pack()


b1 = Button(app, text = 'Correct!', width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text='wrong!', width=10, command=play_wrong_sound)
b2.pack(side='right', padx=10, pady=10)


app.mainloop()

print('-=-' * 15)
print('\n')
print("You asked " + str(number_asked) + " questions.\n")
print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")
print('\n')
print('-=-' * 15)


