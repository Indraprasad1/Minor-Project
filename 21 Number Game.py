def nearestMultiply(num):
    if num >= 4:
        near = num + (4 -(num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE !")
    print("Better luck next Time !")
    exit(0)
    
#Checking Whether numbers are consecutive
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i]-xyz[i-1]) != 1:
            return False
        i = i + 1
    return True

#Starts the game
def start1():
    xyz = []
    last = 0
    while True:
        print("ENter 'F' to take the first chance.")
        print("ENter 'S' to take the second chance.")
        chance = input('>')
        
        #Players take first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\Your Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('>'))
                    
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()
                        
                    i, j = 1, 1
                