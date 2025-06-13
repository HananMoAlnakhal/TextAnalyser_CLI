#-----------------ToPrintTextWithColors--------------------

def GRASS(text):
    return'\33[38;5;46m'+str(text)+'\33[0m'
def GREEN(text):
    return'\33[38;5;119m'+str(text)+'\33[0m'
def BROWN(text):
    return'\33[38;5;166m'+str(text)+'\33[0m'
def YELLOW(text):
    return'\33[38;5;226m'+str(text)+'\33[0m'
def ORANGE(text):
    return'\33[38;5;208m'+str(text)+'\33[0m'
def RED(text):
    return'\33[38;5;197m'+str(text)+'\33[0m'
def PINK(text):
    return'\33[38;5;213m'+str(text)+'\33[0m'
def PURPLE(text):
    return'\33[38;5;171m'+str(text)+'\33[0m'
def sysBLUE(text):
    return'\33[38;5;31m'+str(text)+'\33[0m'
def BLUE(text):
    return '\33[38;5;69m'+str(text)+'\33[0m'
def SkyBlue(text):
    return'\33[38;5;80m'+str(text)+'\33[0m'
def CYAN(text):
    return'\33[38;5;51m'+str(text)+'\33[0m'





def BlackBG(text):
    return'\33[48;5;16m'+str(text)+'\33[0m'
def RedBG(text):
    return'\33[48;5;160m'+str(text)+'\33[0m'


#-----------------ToPrintTextWithEffects--------------------
def BOLD(text):
    return '\x1b[1m'+str(text)+'\x1b[0m'
def ITALIC(text):
    return '\x1b[3m'+str(text)+'\x1b[0m'
def UNDERLINED(text):
    return '\x1b[4m'+str(text)+'\x1b[0m'