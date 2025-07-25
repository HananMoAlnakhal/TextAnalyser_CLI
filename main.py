from predictor import *
from TEXTstyling import *
from TextEditor import *
from util import *
from Analyzer import *
import tkinter as tk
from tkinter import filedialog
from TextEditor import *
import time

from shutil import get_terminal_size
from math import ceil
Report=None
size= get_terminal_size()

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
    
def menu_Options_display():
    clear_screen()
    maxLim=8
    minlim=1
    current=1
    options=["Words stats",
             "Character stats",
             "search for a word",
             "replace word",
             "word Cloud",
             "Text Sentiment",
             "Try with new text",#could add save report/ edited text here
             "EXIT",
             ]
    def display_input():
        clear_screen()
        size= shutil.get_terminal_size()
        print("\033[1;0H"+SkyBlue(TITLE))
        # print(CENTER_SCREEN("MAIN MENU",-5))
        print(BOLD(f'{GREEN(options[0]) if current == 1 else Gray1(options[0])}').center(size.columns))
        print(BOLD(f'{GREEN(options[1]) if current == 2 else Gray1(options[1])}').center(size.columns))
        print(BOLD(f'{GREEN(options[2]) if current == 3 else Gray1(options[2])}').center(size.columns))
        print(BOLD(f'{GREEN(options[3]) if current == 4 else Gray1(options[3])}').center(size.columns))
        print(BOLD(f'{GREEN(options[4]) if current == 5 else Gray1(options[4])}').center(size.columns))
        print(BOLD(f'{GREEN(options[5]) if current == 6 else Gray1(options[5])}').center(size.columns))
        print(BOLD(f'{GREEN(options[6]) if current == 7 else Gray1(options[6])}').center(size.columns))
        print(BOLD(f'{RED(options[7]) if current == 8 else Gray1(options[7])}').center(size.columns))        
        print("\n\n"+"_"*size.columns)
        print(Title2)
        
    display_input()
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char=="UP":
                if current>minlim:
                    current-=1
                else:
                    current=maxLim
                display_input()
            elif Char=="DOWN":
                if current<maxLim:
                    current+=1
                else:
                    current=minlim
                display_input()
            elif Char=="ENTER":
                    if current==maxLim:
                        return "EXIT"
                    return current
            else:
                print("\033[0;0HPLEASE Use UP/DOWN arrow keys to chose one option\nPress Enter to confirm choice")

def Get_Text(*text):
    global Report
    method=choose_input_method()
    if method=="EDITOR":
        listOfSentences=SmartTextEditor()
        Report = SmartTextAnalyzer(",".join(listOfSentences))
    else:
        filePath=choose_file()
        text=open(filePath).read()
        Report = SmartTextAnalyzer(text) 
    return

def Data_table(Data:dict,Title="Character frequency",Lines=12,c_w=3,d_w=5):
    Values_to_print=sorted(Data.items(),key=lambda x:x[1],reverse=True)
    columns_number=ceil(len(Values_to_print)/Lines)
    c_Group=[[]for i in range(columns_number)]
    for i,Data in enumerate(Values_to_print):
        c_Group[i//Lines].append(Data[0].rjust(d_w)+"  :  "+str(Data[1]).ljust(d_w)+" ")
    c_Group[-1]=c_Group[-1]+([" "]*(Lines-len(c_Group[-1]))) #for filling empty rows in last columns_number
    col_Width=len(c_Group[0][0])+c_w
    Table_Width=(columns_number*col_Width)+columns_number+1
    Table_Lines=["\u250C"+("\u2500"*(Table_Width-2))+"\u2510",
                "\u2502"+Title.center(Table_Width-2)+"\u2502",
                "\u251C"+"\u252C".join(["\u2500"*(col_Width) for i in range(columns_number)])+"\u2524"]
    for r in range(Lines):
        row="\u2502"
        for column in c_Group:
            row+=(column[r].center(col_Width)+"\u2502")
        Table_Lines.append(row)
    Table_Lines.append("\u2514"+"\u2534".join(["\u2500"*(col_Width) for i in range(columns_number)])+"\u2518")
    return Table_Lines,Table_Width

def print_table(Table,center=False,right=False):
    Terminal_Width=get_terminal_size().columns
    for line in Table:
        if center:
            print(line.center(Terminal_Width))
        elif right:
            print(line.rjust(Terminal_Width))
        else:
            print(line)

def display_Word_stats(Report,n=10):
    def display():
        clear_screen()
        print(BABY_Yellow(BOLD(WordsStats)))
        #\033[1;0H
        print(BABY_Yellow(f"{UNDERLINED(BOLD('WORDS STATS'))} "+"─"*30+f" press {PINK('esc')} to back to menu"))
        print()
        print(f"{BABY_Yellow('TOTAL WORDS #:')}\t\t{Report.totalWords}")
        print(f"{GREEN('Unique words #:')}\t\t{len(Report.uni)}")
        print(f"{CYAN('keywords count:')}\t\t{Report.uniqueCount}")
        print("\u250C"+("\u2500"*23)+"\u252C"+("\u2500"*22)+"\u2510")
        print("\u2502 "+"word".ljust(9)+ "Frequency".center(10)+"\t\u2502"+f" {CYAN('keyword')}   Frequency  \u2502")
        print("\u251C"+("\u2500"*23)+"\u253C"+("\u2500"*22)+"\u2524")
        Most_FrequentWords=Report.MostFrequentWords(n=n)
        Most_FrequentKeyWords=Report.MostFrequentWords(n=n,KeyWords=True)
        for Freq,key in zip(Most_FrequentWords,Most_FrequentKeyWords):
            print("\u2502 "+Freq[0].ljust(9)+str(Freq[1]).center(10)+"\t\u2502",(key[0].ljust(9)+str(key[1]).center(10))+"  \u2502")
        print("\u2514"+("\u2500"*23)+"\u2534"+("\u2500"*22)+"\u2518\n")
        
    display()
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char=="ESC":
                return

def display_Character_stats(Report):
    def display():
        clear_screen()
        print(BABY_Yellow(BOLD(chr_Stats)))
        #\033[1;0H
        print(CYAN(f"{UNDERLINED(BOLD('Character STATS'))} "+"─"*30+f" press {PINK('esc')} to back to menu"))
        print()
        print(f"{BABY_Yellow('Character Count #:')}\t\t{Report.CharacterCount}")
        print(f"{CYAN('Unique Character #:')}\t\t{len(list(Report.CharacterOccurrence.keys()))}")
        print_table(Data_table(Report.CharacterOccurrence,c_w=0)[0],center=True)

    display()
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char=="ESC":
                return

def input_box(title="",shape=False,pos=5):
    print(f"\033[{pos};0H  {title}")
    print("  \u256D"+"\u2500"*(get_terminal_size().columns-8)+"\u256E")
    print("  \u2502"+" "*(get_terminal_size().columns-8)+"\u2502")
    print("  \u2570"+"\u2500"*(get_terminal_size().columns-8)+"\u256F")
    print(f"\033[{pos+1};10H")
    if not shape:
        input_Text=input("  \u2502"+" ",)
        print(f"\033[{pos+3};5H")
        return input_Text
       
def Search_sc(Report):
    def display():
        clear_screen()
        input_box(pos=5,title=SkyBlue("Text to search:"),shape=True)
        text_for_search=""
        while text_for_search =="":
            text_for_search=input_box(pos=5)

        search_results=Report.searchText(text_for_search)
        Report._displaySearch(search_results)
    display()
    while True:
        if msvcrt.kbhit():
            display()
            Char=get_key()
            if Char=="ESC":
                return

def replace_sc(Report):
    def display():
        clear_screen()
        input_box(pos=5,title=ORANGE("Old text:"),shape=True)
        input_box(pos=10,title=GREEN("New Value:"),shape=True)
        text_for_search=""
        replace_with=""
        while text_for_search =="" or replace_with=="":
            text_for_search=input_box(pos=5)
            replace_with=input_box(pos=10)
        Report.replaceWords(text_for_search,replace_with)

    display()
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char=="ESC":
                return
            display()

def Word_Cloud(Report):
    def display(p):
        clear_screen()
        if p==1:
            Report.WordCloud(n=30,KeyWords=True,Vis=True)
        if p==2:
            Report.WordCloud(n=30,KeyWords=False,Vis=True)
        if p==3:
            Report.WordCloud(n=30,KeyWords=True,Bar=True)
        if p==4:
           Report.WordCloud(n=30,KeyWords=False,Bar=True)
        # cases[p-1]

    display(1)
    maxLim=4
    minLim=1
    pos=1
    while True:
        if msvcrt.kbhit():
            Char=get_key()
            if Char == "LEFT":
                if pos > minLim:
                    pos -= 1
                else:
                    pos=maxLim
                display(pos)
            elif Char == "RIGHT":
                if pos < maxLim:
                    pos += 1
                else:
                    pos=minLim

                display(pos)
            elif Char=="ESC":
                return
            else:
                print(f"\033[0;0HPLEASE Use Right/Left arrow keys to navigate between clouds \nPress {RED("esc")} to back to menu")

def main():
    COL=shutil.get_terminal_size().columns
    while COL< 150:
        print(CENTER_SCREEN(" PLEASE EDIT THE WINDOW WIDTH AND MA IT ---wider----"))
        time.sleep(0.3)
        COL=shutil.get_terminal_size().columns
    Get_Text()
    clear_screen()
    print(CENTER_SCREEN(Gray3("Analyzing   ")))
    time.sleep(0.3)
    print(CENTER_SCREEN(Gray7("Analyzing.  ")))
    time.sleep(0.3)
    print(CENTER_SCREEN(Gray8("Analyzing.. ")))
    time.sleep(0.3)
    print(CENTER_SCREEN(Gray9("Analyzing...")))
    time.sleep(0.5)
    print("\033[1;0H"+SkyBlue(TITLE))
    time.sleep(1)

    while True:
        screens=[display_Word_stats,display_Character_stats,Search_sc,replace_sc,Word_Cloud,Get_Text,Get_Text]
        option=menu_Options_display()
        if option=="EXIT":
            break
        screens[option-1](Report)
            
    clear_screen()
    print(CENTER_SCREEN("SEE YOU LATER ✨"))


    
    


main()