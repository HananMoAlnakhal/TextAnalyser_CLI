from util import CircularDoubledList
import shutil
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



def CENTER_SCREEN(text,line=0):
    size= shutil.get_terminal_size()
    text=f"\033[{(size.lines)//2 + line};{(size.columns-len(text))//2}H{text}" 
    return text

#------------------------------------------
#    RAINBOW-colors
# -----------------------------------------
allColors=CircularDoubledList().enQ_LIST([RED,BROWN,ORANGE,YELLOW,GREEN,CYAN,SkyBlue,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK,FOSHII])

#------------------------------------------
#    COOL-colors
# -----------------------------------------
Cools=[GREEN,SkyBlue,CYAN,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK]
CoolColors=CircularDoubledList().enQ_LIST(Cools+Cools[1:-1][::-1])
#------------------------------------------
#    HOT-colors
# -----------------------------------------
Hots=[RED,BROWN,ORANGE,YELLOW,GREEN]
HotColors=CircularDoubledList().enQ_LIST(Hots+Hots[1:-1][::-1])
#------------------------------------------
#    WormCool(From Red to sysBlue)
# -----------------------------------------
Hot_Cool=[CYAN,SkyBlue,Light_BLUE,BLUE,sysBLUE,MIDPurple,PURPLE,PINK,FOSHII,RED]
HotCool=CircularDoubledList().enQ_LIST(Hot_Cool)
#------------------------------------------
#    Black to white
# -----------------------------------------
BlackWhite=[Gray1,Gray2,Gray3,Gray4,Gray5,Gray6,Gray7,Gray8,Gray9]
GrayScale=CircularDoubledList().enQ_LIST(BlackWhite+BlackWhite[::-1])

#===============================================================================================================================
#    USE CASES
# A FUNCTION THAT EDIT THE TEXT AND RETURN TEXT WITH ASCII SYMBOLS FOR THE TERMINAL
#-------------------------------------------------------------------------------------------------------------------------------
# color=CoolColors.GetColor()
# color=HotColors.GetColor()
# color=allColors.GetColor(reverse=False)#start From red if reversed if not r then starts from cool colors
# color=HotCool.GetColor(reverse=False)# became coolHot
# color(Text)<---------------the final use


TITLE="""

███████╗███╗   ███╗ █████╗ ██████╗ ████████╗    ████████╗███████╗██╗  ██╗████████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
███████╗██╔████╔██║███████║██████╔╝   ██║          ██║   █████╗   ╚███╔╝    ██║       ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║          ██║   ██╔══╝   ██╔██╗    ██║       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║          ██║   ███████╗██╔╝ ██╗   ██║       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                      
"""
WordsStats="""
 _       ______  ____  ____  _____    ______________  ___________
| |     / / __ \\/ __ \\/ __ \\/ ___/   / ___/_  __/   |/_  __/ ___/
| | /| / / / / / /_/ / / / /\\__ \\    \\__ \\ / / / /| | / /  \\__ \\ 
| |/ |/ / /_/ / _, _/ /_/ /___/ /   ___/ // / / ___ |/ /  ___/ / 
|__/|__/\\____/_/ |_/_____//____/   /____//_/ /_/  |_/_/  /____/  
                                                                 
"""
chr_Stats="""
   ________                          __               _____ __        __      
  / ____/ /_  ____ __________ ______/ /____  _____   / ___// /_____ _/ /______
 / /   / __ \\/ __ `/ ___/ __ `/ ___/ __/ _ \\/ ___/   \\__ \\/ __/ __ `/ __/ ___/
/ /___/ / / / /_/ / /  / /_/ / /__/ /_/  __/ /      ___/ / /_/ /_/ / /_(__  ) 
\\____/_/ /_/\\__,_/_/   \\__,_/\\___/\\__/\\___/_/      /____/\\__/\\__,_/\\__/____/  
"""
Title2="""
   _____ __  ______    ____  ______   _____________  ________   ___    _   _____    ____  _______   __________ 
  / ___//  |/  /   |  / __ \\/_  __/  /_  __/ ____/ |/ /_  __/  /   |  / | / /   |  / /\\ \\/ /__  /  / ____/ __ \\
  \\__ \\/ /|_/ / /| | / /_/ / / /      / / / __/  |   / / /    / /| | /  |/ / /| | / /  \\  /  / /  / __/ / /_/ /
 ___/ / /  / / ___ |/ _, _/ / /      / / / /___ /   | / /    / ___ |/ /|  / ___ |/ /___/ /  / /__/ /___/ _, _/ 
/____/_/  /_/_/  |_/_/ |_| /_/      /_/ /_____//_/|_|/_/    /_/  |_/_/ |_/_/  |_/_____/_/  /____/_____/_/ |_|  
                                                                                                               
"""
text3="""
   ______  ______   ___  ______  ___________  ________  ___   _  _____   ____  ______  _______ 
  / __/  |/  / _ | / _ \\/_  __/ /_  __/ __/ |/_/_  __/ / _ | / |/ / _ | / /\\ \\/ /_  / / __/ _ \\
 _\\ \\/ /|_/ / __ |/ , _/ / /     / / / _/_>  <  / /   / __ |/    / __ |/ /__\\  / / /_/ _// , _/
/___/_/  /_/_/ |_/_/|_| /_/     /_/ /___/_/|_| /_/   /_/ |_/_/|_/_/ |_/____//_/ /___/___/_/|_| 
                                                                                               
"""
Sentement_analy="""
╔═╗┌─┐┌┐┌┌┬┐┬┌┬┐┌─┐┌┐┌┌┬┐  ╔═╗┌┐┌┌─┐┬ ┬ ┬┌─┐┬┌─┐
╚═╗├┤ │││ │ ││││├┤ │││ │   ╠═╣│││├─┤│ └┬┘└─┐│└─┐
╚═╝└─┘┘└┘ ┴ ┴┴ ┴└─┘┘└┘ ┴   ╩ ╩┘└┘┴ ┴┴─┘┴ └─┘┴└─┘
"""
sen3="""
   _____            __  _                      __     ___                __           _     
  / ___/___  ____  / /_(_)___ ___  ___  ____  / /_   /   |  ____  ____ _/ /_  _______(_)____
  \\__ \\/ _ \\/ __ \\/ __/ / __ `__ \\/ _ \\/ __ \\/ __/  / /| | / __ \\/ __ `/ / / / / ___/ / ___/
 ___/ /  __/ / / / /_/ / / / / / /  __/ / / / /_   / ___ |/ / / / /_/ / / /_/ (__  ) (__  ) 
/____/\\___/_/ /_/\\__/_/_/ /_/ /_/\\___/_/ /_/\\__/  /_/  |_/_/ /_/\\__,_/_/\\__, /____/_/____/  
                                                                       /____/             
"""

Sent2="""                                                                                
 .-.           .                        .        .              .                  
(   )         _|_   o                  _|_      / \\             |           o      
 `-.  .-. .--. |    .  .--.--. .-. .--. |      /___\\  .--. .-.  | .  ..--.  .  .--.
(   )(.-' |  | |    |  |  |  |(.-' |  | |     /     \\ |  |(   ) | |  |`--.  |  `--.
 `-'  `--''  `-`-'-' `-'  '  `-`--''  `-`-'  '       `'  `-`-'`-`-`--|`--'-' `-`--'
                                                                     ;             
                                                                  `-'              
"""