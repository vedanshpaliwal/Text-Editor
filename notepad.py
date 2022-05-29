from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled -Notepad")
    file = None
    textarea.delete(1.0,END)
    
  
  

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    
    if file ==" ":
        file =NONE
    else:
        root.title(os.path.basename(file) + " -Notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
    
    
    

def savefile():
    global file 
    if file ==None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension="*.txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file =="":
             file = None
    
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

    else:
         f = open(file,"w")
         f.write(textarea.get(1.0, END))
         f.close()

def saveas_file():
    global file
    file = asksaveasfilename(initialfile="Untitled.txt",defaultextension="*.txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    f = open(file, "w")
    f.write(textarea.get(1.0, END))
    f.close()

    root.title(os.path.basename(file) + " - Notepad")
    print("File Saved")


def quitAPP():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad","Notepad by vedansh Paliwal")
    
    
if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("note.ico")
    root.geometry("644x788")
    
    
    #add textarea
    textarea =Text(root,font="lucia 13") 
    file = None 
    textarea.pack(expand=TRUE,fill=BOTH)
    
    # menu bar 
    menubar = Menu(root)
    filemenu = Menu(menubar,tearoff=0)
    
    # to open a new file
    
    filemenu.add_command(label="New" ,command=newfile)
    
    # to open a already existing file
    
    
    filemenu.add_command(label="Open",command=openfile) 
    
    #to save a file
    
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_command(label="Save As",command=saveas_file)
    
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitAPP)
    menubar.add_cascade(label="File",menu=filemenu)
    
    root.config(menu = menubar)
    
    
    # defining a edit menu
    editmenu = Menu(menubar,tearoff=0)
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    
    menubar.add_cascade(label="Edit",menu=editmenu)
    root.config(menu=menubar)
    
    # edit menu has been ended
    
    
    # help menu has been started
    helpmenu =Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)
    root.config(menu=menubar)
    # help menu has been ended
    
    
    # adding Scrollbar
    
    scrollbar = Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)    
    textarea.config(yscrollcommand=scrollbar.set)
    
    
       
    root.mainloop()  