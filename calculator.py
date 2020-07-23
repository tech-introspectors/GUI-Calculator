from tkinter import *

#variables
screenbg_color = "#4b585e"
screentext_color  = "#F9AA33"
framebg = "#232f34"
clearbtn_bg = "#F9AA33"
allbtn_bg = "#344955"
text_color = "#F9AA33"




#functions for button
def click(event):
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error!"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.title("Basic Calculator")
root.geometry("360x590")
root.iconbitmap("win_icon.ico")
root.minsize(360,590)
root.maxsize(360,590)

scvalue = StringVar()
scvalue.set(" ")

screen = Entry(root, textvar = scvalue, font = "lucida 30 bold",bd = 0,bg = f"{screenbg_color}", fg= f"{screentext_color}")
screen.pack( ipady = 10)

# Frame 1 ---------------------------------->>>>>
f1 = Frame(root, bg = f"{framebg}")
for i in range(7,10):
    b = Button(f1, text = f"{i}", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
    b.pack(side = LEFT, pady = 15,padx = 15)
    b.bind('<Button-1>', click)

div = Button(f1, text = "/", pady = 10, padx = 10, font = "lucida 25 bold" ,bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
div.pack(side = LEFT, pady = 15,padx = 15, ipadx =4)
div.bind('<Button-1>', click)
f1.pack()

# Frame 2 ---------------------------------->>>>>

f2 = Frame(root, bg = f"{framebg}")
for i in range(4,7):
    b = Button(f2, text = f"{i}", pady = 10, padx = 10, font = "lucida 25 bold" , bd = 0,bg = f"{allbtn_bg}", fg = f"{text_color}")
    b.pack(side = LEFT, pady = 15,padx = 15)
    b.bind('<Button-1>', click)

add = Button(f2, text = "+", pady = 10, padx = 10, font = "lucida 25 bold" ,bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
add.pack(side = LEFT, pady = 15,padx = 14)
add.bind('<Button-1>', click)
f2.pack()

# Frame 3 ---------------------------------->>>>>

f3 = Frame(root, bg = f"{framebg}")
for i in range(1,4):
    b = Button(f3, text = f"{i}", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
    b.pack(side = LEFT, pady = 15,padx = 15)
    b.bind('<Button-1>', click)

sub = Button(f3, text = "-", pady = 10, padx = 10, font = "lucida 25 bold", bd = 0,bg = f"{allbtn_bg}", fg = f"{text_color}")
sub.pack(side = LEFT, pady = 15,padx = 15, ipadx=3)
sub.bind('<Button-1>', click)
f3.pack()

# Frame 4 ---------------------------------->>>>>

f4 = Frame(root, bg = f"{framebg}")

dot = Button(f4, text = ".", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
dot.pack(side = LEFT, pady = 15,padx = 15, ipadx =3)
dot.bind('<Button-1>', click)
f4.pack()

zero = Button(f4, text = "0", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
zero.pack(side = LEFT, pady = 15,padx = 15)
zero.bind('<Button-1>', click)
f4.pack()


equal = Button(f4, text = "=", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
equal.pack(side = LEFT, pady = 15,padx = 15)
equal.bind('<Button-1>', click)
f4.pack()

multi = Button(f4, text = "*", pady = 10, padx = 10, font = "lucida 25 bold",bd = 0, bg = f"{allbtn_bg}", fg = f"{text_color}")
multi.pack(side = LEFT, pady = 15,padx = 15, ipadx=3)
multi.bind('<Button-1>', click)
f4.pack()

# Frame 5 ---------------------------------->>>>>

f5 = Frame(root, bg = f"{framebg}")

clear = Button(f5, text = "C", font ="lucida 25 bold", pady=10, padx =10,bd = 0, bg = f"{clearbtn_bg}")
clear.pack(fill = X)
clear.bind('<Button-1>', click)

f5.pack(fill = X)






root.mainloop()