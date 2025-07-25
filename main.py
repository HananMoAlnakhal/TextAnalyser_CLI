from predictor import *
from TEXTstyling import *
from TextEditor import *
from util import *
from Analyzer import *
import tkinter as tk
from tkinter import filedialog
import time

def choose_file():
    root = tk.Tk()
    root.withdraw() 
    clear_screen()
    print(CENTER_SCREEN("chose a text file that is in a .txt format"))
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:
        clear_screen()
        print(CENTER_SCREEN("Selected file: "+file_path))
        print(CENTER_SCREEN(f"Press {BOLD('Enter')} to confirm or any key to reselect",2))
        pressed=False
        while not pressed:
            if msvcrt.kbhit():
                Char=get_key()
                if Char=="ENTER":
                    return file_path
                else:
                    return choose_file()
    else:
        clear_screen()
        print(CENTER_SCREEN("you choose no file: "+file_path))
        time.sleep(2)
        print(CENTER_SCREEN("please try again..",2))
        return choose_file()


def choose_input_method():
    clear_screen()
    flag=None
    def display_input():
        print(CENTER_SCREEN(BOLD("Do you want to write text? or to import a text file?"),-2),end="")
        options=CENTER_SCREEN(f'                {GREEN("write your text") if flag == True else Gray1("write your text")}   '+\
                              f'   {GREEN("import Text") if flag == False else Gray1("import Text")}',1)
        print(options)
        
    display_input()
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char=="LEFT":
                flag=True
                display_input()
            elif Char=="RIGHT":
                flag=False
                display_input()
            elif Char=="ENTER":
                if flag==None:
                    print(CENTER_SCREEN("PLEASE Use arrow keys to chose one option",5))
                else:
                    break
            else:
                
                print(CENTER_SCREEN("PLEASE Use arrow keys to chose one option\nPress Enter to confirm choice",5))

    if flag==True:
        return "EDITOR"
    else:
        return "IMPORT"
    
def main():
    method=choose_input_method()
    if method=="EDITOR":
        pass
    else:
        filePath=choose_file()
        print(RED(filePath))


main()