from tkinter import Tk, Button, Label, Canvas
from random import randint

base = Tk()
base.title("BALL GAME")
base.resizable(False, False)

color = Canvas(base, width=590, height=610)
color.pack()

standard = 0
length = 5
marks = 0
slide_obj = None

class Model:
    def __init__(self, color, m1, n1, m2, n2):
        self.m1 = m1
        self.n1 = n1
        self.m2 = m2
        self.n2 = n2
        self.color = color
        self.circle = color.create_oval(self.m1, self.n1, self.m2, self.n2, fill="blue", tags='dot1')

    def game(self):
        global standard, marks, length
        if standard >= 510:
            if length - 5 <= self.m1 and length + 40 + 5 >= self.m2:
                marks += 5
                color.delete('dot1')
                game_play()
            else:
                color.delete('dot1')
                result()
            return
        standard += 1
        self.color.move(self.circle, 0, 1)
        self.color.after(10, self.game)

class Slide:
    def __init__(self, color, m1, n1, m2, n2):
        self.color = color
        self.num = color.create_rectangle(m1, n1, m2, n2, fill="green", tags='dot2')

    def push(self, num):
        global length
        if num == 1:
            if length + 40 < 570:
                self.color.move(self.num, 20, 0)
                length += 20
        else:
            if length > 5:
                self.color.move(self.num, -20, 0)
                length -= 20

def game_play():
    global standard
    standard = 0
    size = randint(0, 570)
    game1 = Model(color, size, 20, size + 30, 50)
    game1.game()

def result():
    base2 = Tk()
    base2.title("THE BALL GAME")
    base2.resizable(False, False)
    set_canvas = Canvas(base2, width=300, height=300)
    set_canvas.pack()
    
    z = Label(set_canvas, text=f"\nGame over\n\nYou have scored = {marks}\n\n")
    z.pack()
    
    btx = Button(set_canvas, text="Enter if you want to play again", bg="yellow", command=lambda: repeat(base2))
    btx.pack()
    
    bty = Button(set_canvas, text="CLOSE", bg="red", command=lambda: destroy(base2))
    bty.pack()

def repeat(base2):
    base2.destroy()
    function()

def destroy(base2):
    base2.destroy()
    base.destroy()

def function():
    global marks, length, slide_obj
    marks = 0
    length = 5
    slide_obj = Slide(color, 5, 560, 45, 575)
    
    Bt0 = Button(color, text="Move Right**", bg="pink", command=lambda: slide_obj.push(1))
    Bt0.place(x=335, y=580)
    
    Bt1 = Button(color, text="**Move Left", bg="pink", command=lambda: slide_obj.push(0))
    Bt1.place(x=260, y=580)
    
    game_play()
    base.mainloop()

if __name__ == "__main__":
    function()
