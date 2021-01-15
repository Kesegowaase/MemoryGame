from tkinter import *
from random import*
from tkinter import messagebox
import time

game = Tk()

game.title("Memory Game")
game.geometry("1080x720")
game.minsize(800,600)
game.state('normal')
    

def generateNumber():
    global generator
    for z in range(generator):
        a = randint(0,100)
        list.append(a)
        

def widgetS():
    entry.pack(side = "bottom", fill = X)
    button.pack(side = "bottom", fill = X)
    checkLabel.pack(side = "top")
    checkLabel.after(500,showList)

def showList():
    numberArea.pack()
    global counter
    k = 1
    while 1:
        if counter == generator:
            break
        numberArea.after(1000*k,showText)
        counter +=1
        k +=1
    counter = 0
    numberArea.after(1000*k,clear)
    
def clear():
    numberArea.delete('1.0',END)
    for k in range(33):
        numberArea.insert(f'{k}.0', ' '*(120) + '\n')

def showText():
    global counterList
    line = randint(0, 33) + 1
    column = randint(0, 110)
    position = f'{line}.{column}'
    clear()
    numberArea.insert(position,list[counterList])
    counterList+=1

def first():
    butPlay.forget()
    generateNumber()
    widgetS()
    

def checkEntry():
    global generator
    global correctAnswer

    content = int(entry.get())
    entry.delete(0,"end")
    if content in list:
        checkLabel["text"] = "True"
        correctAnswer += 1
        if correctAnswer == generator:
            messagebox.showinfo("Congratulations","You can pass this level" )
            correctAnswer = 0
            generator += 1
            generateNumber()
            showList()
            checkLabel["text"] = ""
    else:
        messagebox.showinfo("Wrong answer","GAME OVER!")
        game.quit()
    

correctAnswer = 0
generator = 1
counterList = 0
counter = 0
list = []

butPlay = Button(game,text = "Play!",command = first,bg = "white", fg = "black" , font = "Arial 18 bold")
butPlay.pack()

button = Button(game,text = "Try",bg = "white",command = checkEntry, fg = "black" , font = "Arial 18 bold")

entry = Entry(game,bg = "black", fg = "white")

numberArea = Text(game, width=120, height=35)

checkLabel = Label(game,height = 5,width = 20,text="",bg="black",fg="white",font = "Arial 10 bold")


game.mainloop()
