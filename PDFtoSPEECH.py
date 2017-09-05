def printtext():
    global e
    filename = e.get()
    lines = extract_pdf(filename)
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-20)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
        
    for line in lines:
        engine.say(line)
        engine.runAndWait()
        #print (line)
    #messagebox.showinfo("Entered text", string)
       
from PDFreader import extract_pdf
from tkinter import *
from tkinter import messagebox
import pyttsx
root = Tk()
root.title('Name')

root.geometry("800x600") 
root.resizable(0, 0)

e = Entry(root)
e.pack(expand=1,anchor=CENTER)
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(expand=1,anchor=CENTER)

d = Button (root, text="Good-bye", command=root.destroy)
d.pack(expand=1,anchor=CENTER)

root.mainloop()
