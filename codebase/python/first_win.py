#!/usr/bin/python3

import tkinter as tk

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

class master():
    """ --- """
    def __init__(self, root=None, tok=None, lang="sv"):
        self.dy = 20
        self.dx = 20
        self.itemlist = []
        if root is None:
            self.root = tk.Tk()
            self.root.geometry("500x500")
        else:
            self.root = root

        if tok is None:
            self.tok = tokens()
        else:
            self.tok = tok

            
        self.root.title(self.tok.title)

        self.add_img()
        
    def add_img(self, imgfile="../../database/file.png"):
        canvas=tk.Canvas(self.root, width = 100, height = 100)
        canvas.pack()
        img = tk.PhotoImage(file=imgfile)
        label1 = tk.Label(image=img)
        label1.image = img
        label1.place(x=50,y=50)
        # canvas.create_image(20,20,image=img)
        
    def add_item(self, obj=None):
        self.itemlist.append(obj)
        
def add_button(top=None, text="", pos = (0,0)):
    (x,y) = pos
    button = tk.Button(top.root, text=text, command=top.root.destroy)
    button.pack()
    button.place(x=x,y=y)
    top.add_item(button)
    
def add_ok(top=None, pos=(0,0)):
    (x,y) = pos
    l1 = tk.Label(top.root, text=tok.ok)
    l1.pack()
    l1.place(x,y)

    top.add_item(l1)
    
def add_label(top=None, label="", pos=(0,0)):
    (x,y) = pos
    lbl = tk.Label(top.root, text=label)
    lbl.pack()
    lbl.place(x=x,y=y)
    top.add_item(lbl)

def add_list(top=None, altlist="", pos=(0,0)):
    (x,y) = pos
    lbl = tk.Listbox(top.root, selectmode = "single")
    for pos,ll in enumerate(altlist):
        lbl.insert(pos, ll)
    lbl.pack()
    lbl.place(x=x,y=y)
    top.add_item(lbl)

def ask_question(top=None, pos=(0,0)):
    (x,y) = pos
    e1 = tk.Entry(top.root)
    e1.place(x=x,y=y)
    top.add_item(e1)
        

def main():
    
    top = master()

    top.root.after(500, add_label, top, top.tok.client, (1*top.dx, 2*top.dy))
    top.root.after(500, add_label, top, top.tok.age, (1*top.dx, 3*top.dy))
    top.root.after(500, add_label, top, top.tok.sex, (1*top.dx, 4*top.dy))

    top.root.after(500, ask_question, top, (5*top.dx, 2*top.dy))
    top.root.after(500, ask_question, top, (5*top.dx, 3*top.dy))
    top.root.after(500, add_list, top, ["Man", "Kvinna", "Vill ej ange", "Icke-binär"], (5*top.dx, 4*top.dy))

    top.root.after(500, add_button, top, top.tok.quit, (4*top.dx, 8*top.dy))
    top.root.after(500, add_button, top, top.tok.next, (4*top.dx, 10*top.dy))

    # a = input()
    
    print(top.itemlist)
    for item in top.itemlist:
        print(item)
        try:
            print(item.get())
        except:
            pass

    top.root.mainloop()


#if __name__ == "__main__":

main()
