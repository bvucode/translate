import tkinter
from tkinter import Text
from tkinter import messagebox
from tkinter import scrolledtext
from translate import Translate
from nlp.words import Words
import corpus

root = tkinter.Tk()
root.title("translate")
root.geometry("650x250")
root.configure(bg = "black")

flag = 0

dcengru = corpus.translate("eng-ru")
dcrueng = corpus.translate("ru-eng")

fengru = Translate(*dcengru)
frueng = Translate(*dcrueng)

def translatef():
    txt2.configure(state = "normal")
    txt2.delete(1.0, tkinter.END)
    inp = txt.get(1.0, tkinter.END)
    w = Words(inp)
    wl = w.load()
    sl = gettr(wl)
    if len(sl) != 0:
        triallist = []
        sl.sort(key = lambda x: x[1])
        for i in sl:
            if i[0][1] == "out":
                triallist.append(str(i[0][0]))
            else:
                triallist.append(str(i[0][1]))
        varstr = " ".join(triallist)
        txt2.insert(1.0, varstr)
        txt2.configure(state = "disable")
    else:
        txt2.insert(1.0, "Translation")
        txt2.configure(state = "disable")

def deletef():
    txt2.configure(state = "normal")
    txt.delete(1.0, tkinter.END)
    txt2.delete(1.0, tkinter.END)
    txt2.insert(1.0, "Translation")
    txt2.configure(state = "disable")

def changelang():
    global flag
    if flag == 0:
        lbl["text"] = "Russian"
        lbl2["text"] = "English"
        flag = 1
    else:
        lbl["text"] = "English"
        lbl2["text"] = "Russian"
        flag = 0

def gettr(xarg):
    global fengru
    global frueng
    global flag
    if flag == 0:
        r = fengru.load(xarg)
    else:
        r = frueng.load(xarg)
    return r

def infof():
    msg = messagebox.showinfo( "Translate", "by vbucode")

btn1 = tkinter.Button(root, text = "translate", bg = "gray", command = translatef)
btn2 = tkinter.Button(root, text = "delete", bg = "gray", command = deletef)
btn3 = tkinter.Button(root, text = "info", bg = "gray", command = infof)
btn4 = tkinter.Button(root, text = "<>", bg = "gray", command = changelang)
lbl = tkinter.Label(root, text = "English", fg = "white", bg = "black")
lbl2 = tkinter.Label(root, text = "Russian",  fg = "white", bg = "black")
txt = scrolledtext.ScrolledText(root, width = 35, height = 10)
txt2 = Text(root, width = 35, height = 10)
lbl.place(x = 5, y = 4)
txt.place(x = 5, y = 20)
lbl2.place(x = 360, y = 4)
txt2.place(x = 360, y = 20)
btn4.place(x = 307, y = 20)
btn1.place(x = 5, y = 205)
btn2.place(x = 96, y = 205)
btn3.place(x = 170, y = 205)

if __name__ == "__main__":
    txt2.insert(1.0, "Translation")
    txt2.configure(state = "disable")
    root.mainloop()
