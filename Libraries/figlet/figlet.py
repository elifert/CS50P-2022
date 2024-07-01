import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()
if len(sys.argv)==1:
    s = input()
    figlet.setFont(font=choice(list))
    print(figlet.renderText(s))
elif len(sys.argv)==3:
    if (sys.argv[1]=="-f" or sys.argv[2] == "--font") and sys.argv[2] in list:
        s = input()
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")
        
else:
    sys.exit("Invalid usage")
    