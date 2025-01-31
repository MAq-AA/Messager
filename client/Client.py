from .Window import Window 
from .EntryWin import EntryWin

def main(): 
    entryWin = EntryWin()
    client = Window()
    while True:
        do_entry = entryWin.succesful_entry
        if not do_entry:
            entryWin.initialAll()
            entryWin.root.wait_window()
        if do_entry:  
            client.initialWindow()
          