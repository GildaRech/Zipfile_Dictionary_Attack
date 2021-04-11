# -*- coding: utf-8 -*-
# This source code is for educational purpose and is the practical material of my tutorial
# delivered at [Y-T] on " building a Rar and/or a Zip file dictionary attack
# toolkit". Please feel free to edit, modify or change any piece of code on this and
# drop me a mail at bansimbagilda@gmail.com in case of any related concern, proposition
# or suggestion that could further our knowledge.
# DISCLAIMER: As mentioned above, this content is for educational purpose only and must
#  be strictly used on owned protected files only. I hereby disclaim that i'm not
# responsible for any harm or damage caused by the misuse of this content.


import os
from Tkinter import *
import tkFileDialog, tkMessageBox
import zipfile
#import rarfile
from threading import Thread

class myFunctions:
    "'this is the main class for the dictionary attack"
    def __init__(self, m):
        self.m=m
    def open(self):
        self.op=tkFileDialog.askopenfilename(parent=self.name, title="Choose the file",
        defaultextension=".txt", filetypes=[('Zip file', '.zip'), ('Rar file', '.rar')])
        self.info=''+str(self.op)
        print format(self.op)
        print self.op[self.op.index("."):]
        self.entry1.insert(END, self.info)
    def open_dictionary(self):
        self.op1=tkFileDialog.askopenfilename(parent=self.name, title="Choose the file",
        defaultextension=".txt", filetypes=[('Text file', '.txt')])
        self.info=''+str(self.op1)
        self.entry2.insert(END, self.info)
    def clean(self):
        self.text.delete("0.0", "100.0")
        self.entry1.delete(0, 100)
        self.entry2.delete(0, 100)
    def clean1(self):
        self.text.delete("0.0", "100.0")
    def attack(self):
        self.fil=str(self.entry1.get())
        self.dict=str(self.entry2.get())
        if self.fil=="" or self.dict=="":
            self.clean()
            self.text.tag_add('warning', '1.0', '9.0')
            self.text.tag_config("warning", background="", foreground="red",font=('Bradley Hand ITC', 20, 'italic'))
            self.text.insert(1.0, "\t File Name or Dictionary INCORRECT\n")
            self.text.insert(2.0, "Please select both File Name and Dictionary"" and try again")
        else:
            t = Thread(target=self.extract, args=(self.fil, self.dict))
            t.start()
    def extract(self, file, dic):
        self.file = file
        self.dic = dic
        #self.clean()
        if self.op[self.op.index("."):]==".rar":
            self.zfile = rarfile.RarFile(self.file)
        elif self.op[self.op.index("."):]==".zip":
            self.zfile = zipfile.ZipFile(self.file)
        self.dico = open(self.dic, 'r')
        for line in self.dico.readlines():
            # self.barprogr.start(50)
            self.password = line.strip('\n')
            self.y = '\n\t Please wait...'
            try:
                self.clean1()
                self.text.insert(2.5, str(self.y))
                self.zfile.extractall(pwd=self.password)
                self.found = '\n \t The password is :' + str(self.password)+'\n'
                #print self.found to print it on the interpreter
                self.clean1()
                self.text.insert(100.5, self.found)
                return 0
            except Exception, e:
                pass
        return 0

class gui(myFunctions):
    "'class of graphical user interface, this inherits from the previous one"
    def __init__(self, name, size, title):
        self.name, self.size, self.title = name, size, title
        self.name=Tk()
        self.name.title(str(self.title))
        self.name.geometry(str(self.size))
        self.menu=Menu(self.name, activeborderwidth=5, bd=10, activeforeground="red", font=("arial", 13, "bold"))
        self.menu1=Menu(self.menu, tearoff=0)
        self.menu2=Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", compound="bottom", underline=0,activeforeground="blue", menu=self.menu1)
        #self.menu.add_cascade(label="Edition", compound="bottom", underline=0, menu=self.menu2)
        self.menu1.add_command(label="Open File", underline=0, command=self.open)
        self.menu1.add_command(label="Open Dictionary", underline=0, command=self.open_dictionary)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quit", underline=1, command=self.name.destroy)
        self.string=StringVar()
        self.string1 = StringVar()
        self.name.config(menu=self.menu, bg="brown")
        Label(self.name, text="Name of File", font=("calibri", 15, "bold")).place(x=0,y=6,height=40, width=200)
        Label(self.name, text="Name of Dictionary", font=("calibri", 15, "bold")).place(x=0,y=34, height=40, width=200)
        self.entry1=Entry(self.name, textvariable=self.string)
        self.entry1.place(x=190, y=18, height=20, width=180)
        self.entry2 = Entry(self.name, textvariable=self.string1)
        self.entry2.place(x=190, y=47, height=20, width=180)
        Button(self.name, text="Browse", font=("calibri", 13, "bold"), command=self.open).place(x=400, y=15, height=25, width=180)
        Button(self.name, text="Browse", font=("calibri", 13, "bold"), command=self.open_dictionary).place(x=400, y=45, height=25, width=180)
        self.text=Text(self.name, fg="green", bg="black", bd=50, font=("Blokletters Viltstift",10, "italic"))
        self.text.place(x=30, y=80, height=230, width=570)
        Button(self.name, text="start", bd=15,bg="black",fg="white", activebackground="green",activeforeground="white" ,font=("calibri", 10, "bold"), command=self.attack).place(x=30, y=283, height=50, width=60)
        Button(self.name, text="stop", bd=15, bg="black", fg="white", activebackground="green",activeforeground="white", font=("calibri", 10, "bold"), command="").place(x=91, y=283,height=50,width=60)
        Button(self.name, text="reset", bd=15, bg="black", fg="white", activebackground="green",activeforeground="white", font=("calibri", 10, "bold"), command=self.clean).place(x=153,y=283, height=50, width=60)
        self.name.resizable(False, True)
        self.name.mainloop()


gui("myApp", "625x360", "Dictionary  Attack at FST") # here we call our main program
