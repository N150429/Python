import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

run =True
previous = 0
def performMath():
    global run
    global previous
    equation = " "
    if previous == 0 :
        equation = input()
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Good Bye, Human")
        run = False
    else:
        equation=re.sub('[a-zA-Z,:()" "]','',equation)
        if previous==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)
        
while run:
    performMath()
