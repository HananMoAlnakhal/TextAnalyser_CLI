import msvcrt
import os
from lang_models import *
def clear_screen():
    os.system('cls')

def get_key():
    first = msvcrt.getch()
    if first == b'\x00':
        second = msvcrt.getch()
        if second == b'H':
            return 'UP'
        elif second == b'P':
            return 'DOWN'
        if second == b'K':
            return 'LEFT'
        elif second == b'M':
            return 'RIGHT'
    elif first == b'\r':
        return 'ENTER'
    elif first == b'\t': #tab
        return 'SELECT'
    elif first == b'\b': 
        return 'BACKSpace'
    elif first== b' ':
        return '_SPACE_'
    
    return first.decode(errors='ignore')

def writing_line(p=0):
    def print_Text(noPointer=False):
        print(f'\033[{p};0H'+" "*100)
        if not noPointer:
            print(f'\033[{p};0H'+"> "+text[:pos+1]+"|"+text[pos+1:])
            for i in range(1,4):
                print(f'\033[{p+i};0H'+" "*100)
            if GetNext:
                for ind,Word in enumerate(NextWords):
                    print(f'\033[{p+ind+1};0H'+" "*100)
                    print(f'\033[{p+ind+1};0H ',text+"\33[38;5;31m"+Word[0]+"\33[0m")
            else:
                for ind,Word in enumerate(CurrentWords):
                    print(f'\033[{p+ind+1};0H'+" "*100)
                    print(f'\033[{p+ind+1};0H ',len(text[:-len(Last_part)-1])*"_"+" "+Word[0][:len(Last_part)]+"\33[38;5;31m"+Word[0][len(Last_part):]+"\33[0m")       
        else:
            print(f'\033[{p};0H'+"> "+text)
    text=""
    pos=0
    GetNext=False
    last2Words=[]
    Last_part=""
    CurrentWords=[]
    NextWords=[]
    print_Text()

    while True:
        if msvcrt.kbhit():
            CHAR = get_key()
            if CHAR=='ENTER':
                print_Text(noPointer=True)
                break

            elif CHAR=="LEFT":
                if pos>0:
                    pos-=1
                print_Text()

            elif CHAR=="RIGHT":
                if pos<len(text):
                    pos+=1
                print_Text()

            elif CHAR=="SELECT":
                if GetNext==False:
                    text=text[:-len(Last_part)]+CurrentWords[0][0]
                    pos+=len(CurrentWords[0][0])-len(Last_part)
                    CurrentWords=[]
                else:
                    text+=NextWords[0][0]+" "
                    pos+=len(NextWords[0][0])+1
                    GetNext=True
                    NextWords=[] 

                print_Text()
            elif CHAR=="UP":
                    continue
            elif CHAR=="DOWN":
                    continue
            else:
                if CHAR=="_SPACE_":
                    CHAR=" "
                    GetNext=True
                    words=text.split()
                    last2Words=[words[-2],words[-1]] if len(words)>1 else [words[-1]]
                    NextWords=Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                    text=text[:pos]+CHAR+text[pos:]
                    pos+=1

                elif CHAR=="BACKSpace":
                    if text[pos-1]!=" ":
                        GetNext=False
                    text=text[:pos-2]+text[pos:]
                    Last_part=Last_part[:-1]
                    if pos>0:
                        pos-=1

                elif len(CHAR)==1:
                    GetNext=False
                    text=text[:pos]+CHAR+text[pos:]
                    Last_part=text.split()[-1] if len(text.split())>0 else ""
                    CurrentWords=[w[0] if w[0].startswith(Last_part) else "" for w in NextWords  ][:3]
                    if len(CurrentWords)>0 :
                        CurrentWords=Pred2Gram.predict_next_top(" ".join(last2Words))
                        CurrentWords=[w for w in CurrentWords if w[0].startswith(Last_part)][:3]
                    pos+=1
                print_Text()

    return text

def SmartTextEditor(stopCriteria="#"):
    lines=[]
    x=""
    pointer_pos=1
    clear_screen()
    while True:
        x=writing_line(p=pointer_pos)
        if x.startswith(stopCriteria):
            break
        lines.append(x.strip())
        pointer_pos+=1
    return(lines)

if __name__=="__main__":
    print(SmartTextEditor())