from pyfiglet import Figlet, FigletFont
import sys
import random

# if neither arguement is passed
if len(sys.argv) == 1:
    user_input = input("Input: ")

    figlet = Figlet()
    f = Figlet(font=random.choice(figlet.getFonts()))
    print(f.renderText(user_input))

# if arguements are passed properly!
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":

        font = sys.argv[2]
        all_fonts = FigletFont.getFonts()
        
        # validation of font passed
        if font in all_fonts:
            f = Figlet(font=sys.argv[2])
            user_input = input("Input: ")
            print(f.renderText(user_input))

        else:
            sys.exit("Invalid Font!")

    else:
        sys.exit("Invalid Usage!")

else:
    sys.exit("Invalid Usage!")
