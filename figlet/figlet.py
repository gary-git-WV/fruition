
import random
import sys
from pyfiglet import Figlet
#from figletfonts import figletfonts

figlet = Figlet()
figletfonts = figlet.getFonts()
errormessage = "Invalid usage"

def main():
    # validate cli args
    if len(sys.argv) == 3:
        if (sys.argv[1] == "-f") or (sys.argv[1] == "--font"):
            if sys.argv[2] in figletfonts:
                # valid, so set font to user spec
                f = sys.argv[2]
                figlet.setFont(font=f)
            else:
                # bad args, say so and exit
                sys.exit(f"{errormessage}")
        else:
            # bad args, say so and exit
            sys.exit(f"{errormessage}")
    elif len(sys.argv) == 1:
        # no user spec for font so random it
        rn = random.randrange(0, 548)
        f = figletfonts[rn]
        figlet.setFont(font=f)
    else:
        # bad args, say so and exit
        sys.exit(f"{errormessage}")
    # print the input string in figlet
    s = input("Input:")
    print(figlet.renderText(s))

main()
