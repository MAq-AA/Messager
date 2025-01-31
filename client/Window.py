from tkinter import *
from tkinter import Toplevel

class Window(Toplevel): 
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def initialWindow(self):
        self.root = self.initialRoot()
        self.initialMessageDiv(self.root)
        self.initialCurrentRoom(self.root)
        self.initialRoomList(self.root)
        self.initialOption(self.root)
        self.root.mainloop()

    def initialRoot(self):
        self.root = Tk()
        self.root.minsize(700, 900)
        self.root.maxsize(700, 900)
        self.root.title("MESSENGER")
        return self.root    

    def initialMessageDiv(self, root):
        frameTextEditor = Frame(root, borderwidth=1, relief=SOLID, padx=8, pady=10)
        self.initialMessageTextEditor(frameTextEditor)
        self.initialMessageButton(frameTextEditor)
        frameTextEditor.place(anchor="se", relx=1, rely=1, width=470, height=150)

    def initialMessageButton(self, frame):
        btn = Button(frame, text="Отправить", command=self.sendMessage)
        btn.pack(anchor="se", pady=[10, 0])

    def initialMessageTextEditor(self, frame):
        editor = Text(frame, height=5, width=56)
        editor.pack(anchor="se")

    def initialCurrentRoom(self, root):
        frameRoom = Frame(root, borderwidth=1, relief=SOLID, padx=8, pady=10)
        frameRoom.place(anchor="ne", relx=1, rely=0, width=470, height=750)

    def initialRoomList(self, root):
        frameRoom = Frame(root, borderwidth=1, relief=SOLID, padx=8, pady=10)
        frameRoom.place(anchor="nw", relx=0, rely=0, width=230, height=750)

    def initialOption(self, root):
        frameRoom = Frame(root, borderwidth=1, relief=SOLID, padx=8, pady=10)
        frameRoom.place(anchor="sw", relx=0, rely=1, width=230, height=150)
        
    def sendMessage(self):
        print("НАЖАЛ")

                