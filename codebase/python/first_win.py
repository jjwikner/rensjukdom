#!/usr/bin/python3

import tkinter as tk


class master():
    """ --- """
    def __init__(self, wind=None, tok=None, lang="sv"):
        self.dy = 20
        self.dx = 20
        self.itemlist = []
        if wind is None:
            self.wind = tk.Tk()
            self.wind.geometry("500x500")
        else:
            self.wind = wind

        if tok is None:
            self.tok = tokens()
        else:
            self.tok = tok

            
        self.wind.title(self.tok.title)

    def add_item(self, obj=None):
        self.itemlist.append(obj)
        
def add_button(top=None, text="", pos = (0,0)):
    (x,y) = pos
    button = tk.Button(top.wind, text=text, command=top.wind.destroy)
    button.pack()
    button.place(x=x,y=y)
    top.add_item(button)
    
def add_ok(top=None, pos=(0,0)):
    (x,y) = pos
    l1 = tk.Label(top.wind, text=tok.ok)
    l1.pack()
    l1.place(x,y)

    top.add_item(l1)
    
def add_label(top=None, label="", pos=(0,0)):
    (x,y) = pos
    lbl = tk.Label(top.wind, text=label)
    lbl.pack()
    lbl.place(x=x,y=y)
    top.add_item(lbl)
 
def ask_question(top=None, pos=(0,0)):
    (x,y) = pos
    e1 = tk.Entry(top.wind)
    e1.place(x=x,y=y)
    top.add_item(e1)
        
class tokens():
    """ For translation purposes """
    def __init__(self, language="sv"):
        self.ok = "OK"
        self.quit = "Avsluta"
        self.next = "Nästa"
        self.client = "Klient"
        self.age = "Ålder"
        self.sex = "Kön"
        self.title = "Ren sjukdom"
        
top = master()

top.wind.after(500, add_label, top, top.tok.client, (1*top.dx, 2*top.dy))
top.wind.after(500, add_label, top, top.tok.age, (1*top.dx, 3*top.dy))
top.wind.after(500, add_label, top, top.tok.sex, (1*top.dx, 4*top.dy))

top.wind.after(500, ask_question, top, (5*top.dx, 2*top.dy))
top.wind.after(500, ask_question, top, (5*top.dx, 3*top.dy))
top.wind.after(500, ask_question, top, (5*top.dx, 4*top.dy))

top.wind.after(500, add_button, top, top.tok.quit, (4*top.dx, 8*top.dy))
top.wind.after(500, add_button, top, top.tok.next, (4*top.dx, 10*top.dy))

# a = input()
# top.wind.mainloop()

print(top.itemlist)
for item in top.itemlist:
    print(item)
    try:
        print(item.get())
    except:
        pass
