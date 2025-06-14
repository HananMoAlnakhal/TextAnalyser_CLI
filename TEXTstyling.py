#-----------------ToPrintTextWithColors--------------------

# def GRASS(text,BG=False): (＞﹏＜) I didn't like that color anymore!
#     return f"\33[{'48'if BG else'38'};5;46m"+str(text)+'\33[0m'
def MIDPurple(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;141m"+str(text)+'\33[0m'
def GREEN(text,BG=False):
    return  f"\33[{'48'if BG else'38'};5;119m"+str(text)+'\33[0m'
def BROWN(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;202m"+str(text)+'\33[0m'
def YELLOW(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;226m"+str(text)+'\33[0m'
def ORANGE(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;214m"+str(text)+'\33[0m'
def RED(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;197m"+str(text)+'\33[0m'
def PINK(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;213m"+str(text)+'\33[0m'
def PURPLE(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;171m"+str(text)+'\33[0m'
def sysBLUE(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;31m"+str(text)+'\33[0m'
def BLUE(text,BG=False):
    return  f"\33[{'48'if BG else'38'};5;69m"+str(text)+'\33[0m'
def Light_BLUE(text,BG=False):
    return  f"\33[{'48'if BG else'38'};5;75m"+str(text)+'\33[0m'
def SkyBlue(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;117m"+str(text)+'\33[0m'
def CYAN(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;51m"+str(text)+'\33[0m'
def FOSHII(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;199m"+str(text)+'\33[0m'
def BABY_Yellow(text,BG=False):
    return f"\33[{'48'if BG else'38'};5;228m"+str(text)+'\33[0m'
def BlackBG(text,BG=True):
    return f"\33[{'48'if BG else'38'};5;16m"+str(text)+'\33[0m'
def Gray1(text):
    return "\33[38;5;238m"+str(text)+'\33[0m'
def Gray2(text):
    return "\33[38;5;240m"+str(text)+'\33[0m'
def Gray3(text):
    return "\33[38;5;243m"+str(text)+'\33[0m'
def Gray4(text):
    return "\33[38;5;247m"+str(text)+'\33[0m'
def Gray5(text):
    return "\33[38;5;249m"+str(text)+'\33[0m'
def Gray6(text):
    return "\33[38;5;250m"+str(text)+'\33[0m'
def Gray7(text):
    return "\33[38;5;251m"+str(text)+'\33[0m'
def Gray8(text):
    return "\33[38;5;253m"+str(text)+'\33[0m'
def Gray9(text):
    return "\33[38;5;255m"+str(text)+'\33[0m'
#-----------------To-Print-Text-With-Effects--------------------
def BOLD(text):
    return '\x1b[1m'+str(text)+'\x1b[0m'
def ITALIC(text):
    return '\x1b[3m'+str(text)+'\x1b[0m'
def UNDERLINED(text):
    return '\x1b[4m'+str(text)+'\x1b[0m'

class Linked_Colors:
    class ColorNode:
        def __init__(self,val,next=None,prev=None):
            self.v=val
            self.next=next
            self.prev=prev

    def __init__(self):
        self._tail=None
        self._head=None
        self._size=0

    def enqueue(self,e):
        newest=self.ColorNode(e)
        if self._size==0:
            newest.next=newest
            newest.prev=newest
            self._head=newest
            self._tail=newest
        else:
            newest.next=self._head
            newest.prev=self._tail
            self._tail.next=newest
        self._tail = newest
        self._head.prev=self._tail
        self._size+=1

    def enQ_LIST(self,LIST):
        for item in LIST:
            self.enqueue(item)
        return self

    def GetColor(self,reverse=False):
        val=self._tail.v if not reverse else None
        self.__rotate(reverse)
        if reverse:val=self._tail.v
        return val
    
    def __rotate(self,r=False):
        if r:
            self._tail = self._tail.next    
        else:
            self._tail = self._tail.prev
#------------------------------------------
#    RAINBOW-colors
# -----------------------------------------
allColors=Linked_Colors().enQ_LIST([RED,BROWN,ORANGE,YELLOW,GREEN,CYAN,SkyBlue,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK,FOSHII])
#adding enQ_LIST mwthod made us avoid the following code each time we wanna make a color sequence:
# colors_list=[RED,BROWN,ORANGE,YELLOW,GREEN,CYAN,SkyBlue,BLUE,sysBLUE,MIDPurple,PURPLE,PINK,FOSHII]
# LinkedColors=Linked_Colors()
# for color in colors_list:
#     LinkedColors.enqueue(color)
# def ColorSer():
#     LinkedColors.rotate()
#     return LinkedColors._tail.v

#------------------------------------------
#    COOL-colors
# -----------------------------------------
Cools=[GREEN,SkyBlue,CYAN,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK]
CoolColors=Linked_Colors().enQ_LIST(Cools+Cools[1:-1][::-1])
#------------------------------------------
#    HOT-colors
# -----------------------------------------
Hots=[RED,BROWN,ORANGE,YELLOW,GREEN]
HotColors=Linked_Colors().enQ_LIST(Hots+Hots[1:-1][::-1])
#------------------------------------------
#    WormCool(From Red to sysBlue)
# -----------------------------------------
Hot_Cool=[CYAN,SkyBlue,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK,FOSHII,RED]
HotCool=Linked_Colors().enQ_LIST(Hot_Cool)
#------------------------------------------
#    Black to white
# -----------------------------------------
BlackWhite=[Gray1,Gray2,Gray3,Gray4,Gray5,Gray6,Gray7,Gray8,Gray9]
GrayScale=Linked_Colors().enQ_LIST(BlackWhite+BlackWhite[::-1])
#===============================================================================================================================
#    USE CASES
# A FUNCTION THAT EDIT THE TEXT AND RETURN TEXT WITH ASCII SYMBOLS FOR THE TERMINAL
# color=CoolColors.GetColor()
# color=HotColors.GetColor()
# color=allColors.GetColor(reverse=False)#start From red if reversed if not r then starts from cool colors
# color=HotCool.GetColor(reverse=False)# became coolHot
# color(Text)<---------------the final use