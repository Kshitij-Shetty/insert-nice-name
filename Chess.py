b=[[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]],[["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"],["__","__","__","__","__","__","__","__"]]]

b[0][0][0]='WE'
b[0][0][1]='WH'
b[0][0][2]='WC'
b[0][0][3]='WQ'
b[0][0][4]='WK'
b[0][0][5]='WC'
b[0][0][6]='WH'
b[0][0][7]='WE'
b[1][0][0]='WP'
b[1][0][1]='WP'
b[1][0][2]='WP'
b[1][0][3]='WP'
b[1][0][4]='WP'
b[1][0][5]='WP'
b[1][0][6]='WP'
b[1][0][7]='WP'
b[0][1][0]='WP'
b[0][1][1]='WP'
b[0][1][2]='WP'
b[0][1][3]='WP'
b[0][1][4]='WP'
b[0][1][5]='WP'
b[0][1][6]='WP'
b[0][1][7]='WP'

b[7][7][0]='BE'
b[7][7][1]='BH'
b[7][7][2]='BC'
b[7][7][3]='BQ'
b[7][7][4]='BK'
b[7][7][5]='BC'
b[7][7][6]='BH'
b[7][7][7]='BE'
b[6][7][0]='BP'
b[6][7][1]='BP'
b[6][7][2]='BP'
b[6][7][3]='BP'
b[6][7][4]='BP'
b[6][7][5]='BP'
b[6][7][6]='BP'
b[6][7][7]='BP'
b[7][6][0]='BP'
b[7][6][1]='BP'
b[7][6][2]='BP'
b[7][6][3]='BP'
b[7][6][4]='BP'
b[7][6][5]='BP'
b[7][6][6]='BP'
b[7][6][7]='BP'

a=1000
m=1
p='w'
def print_b():
    n=int(input("Enter the level of the board to be printed.\nBear in mind the range must be between 1-8, entering any other number, will skip the board printing step.\n"))
    for i in range(a):
        if(n<9 and n>-1):
            for i in range(7,-1,-1):
                print(b[n-1][i])
                print()
            print()
            n=int(input("Enter any number from 1 to 8 to print that particular level, entering any other number, will skip the board printing step.\n"))
 
        if(n==0):
            break
des=input("Welcome!\nEnter 'DESCRIPTION' exactly, if you wish to read a bit more into detail about the game.\nAny other input would skip the description. (The requirement for the exact string, as you may have already guessed, has been put in place to get the decription skipped by most.)\n")
if(des=="DESCRIPTION"):
    print("\n\nThis is an attempt at creating a 3-dimensional chess.\nThe traditional game of chess is two dimensional, as it can be played on a board. This 3-dimensional varient, in the real world, would have to be played in a cubic board of some sort.\nIf the traditional chess has an 8×8 moving space then this version would have 8×8×8 spcaes to move in. This makes the game space 8 times larger, when sonsidering the playing space, also makes it much harder for me to depict it, given my poor animationn skills (basically non-existant).\nSo I have tried to show it as a chess with 8 boards stacked, one on top of the other.\n")
    des=input("If you're not satisfied yet, and want to continue reading, then you might as well read the set of rules I came up with.\nThis time enter 'SOMETHING REALLY LONG' for the rules.\n")
    if(des=="SOMETHING REALLY LONG"):
        des=input("\n\nSome rules:\n\t-There are 16 pawns each for each player, along with the other 8 pieces, meaning 24 pieces each.\n\t-The pieces can literally move in 3-dimension, i.e. forward, backward, left, right, upwards and downwards.\n\t-If the first player is on the bottom most level of the cube, then their opponent will be positioned on the opposite edge, on the topmost level, this means that the two players will be placed at the ends on a diagonal (face-diagonal)\n\nThese are all the rules I could come up with.\n IF YOU STILL WANT TO READ MORE, ENTER 'MORE'.\n")
        if(des=="MORE"):
            print("Unfortunately there's nothing more for you to read, you nerd.\nStart playing already.\n")
        else:
            print("Thanks for not trying to read anymore stuff. I was running out of matter *sighs*\n")
print_b()

def pawn(p):
    d=["__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__"]
    l=0
    if(p=='w'):
        a=0
        l=1
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WP'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==16):
                        break
    else:
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BP'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==16):
                        break
    print("The positions of your pawns are as follows:\n",d)
    a=1000
    for i in range(a):
        print("Enter the coordinates of the pawn you want to move\n")
        z=int(input())
        y=int(input())
        x=int(input())
        #print(x+y+z)
        t=0
        if(l==1):
            if(b[z-1][y-1][x-1]=="WP"):
                t+=1

        else:
            if(b[z-1][y-1][x-1]=="BP"):
                t+=1

        if(t==0):
            print("You don't have a pawn at these coordinates")
            print("Try again.")

        else:
            break

    t=0
    for i in range(a):
        print("Enter the coordinates of the position you want to move the pawn to\n")
        z1=int(input())
        y1=int(input())
        x1=int(input())
        if(l==1):
            if(((z-1==1)and(y-1==0))or((z-1==0)and(y-1==1))):
                if(((z1==z+2)and(y1==y)and(x1==x))or((z1==z+1)and(y1==y)and(x1==x))or((z1==z)and(y1==y+2)and(x1==x))or((z1==z)and(y1==y+1)and(x1==x))):
                    if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                        print("The pawn can't move to this position because it's occupied by your own piece.")
                        print("Try again.")
                    else:
                        t+=1

                else:
                    print("The pawn can't move to this position.")
            else:
                if(((z1==z+1)and(y1==y)and(x1==x))or((z1==z)and(y1==y+1)and(x1==x))):
                    if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                        print("The pawn can't move to this position because it's occupied by your own piece.")
                        print("Try again.")
                    else:
                        t+=1

                else:
                    print("The pawn can't move to this position.")


        else:
            if(((z-1==7)and(y-1==6))or((z-1==6)and(y-1==7))):
                if(((z1==z-2)and(y1==y)and(x1==x))or((z1==z-1)and(y1==y)and(x1==x))or((z1==z)and(y1==y-2)and(x1==x))or((z1==z)and(y1==y-1)and(x1==x))):
                    if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                        print("The pawn can't move to this position because it's occupied by your own piece.")
                        print("Try again.")
                    else:
                        t+=1

                else:
                    print("The pawn can't move to this position.")
            else:
                if(((z1==z-1)and(y1==y)and(x1==x))or((z1==z)and(y1==y-1)and(x1==x))):
                    if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                        print("The pawn can't move to this position because it's occupied by your own piece.")
                        print("Try again.")
                    else:
                        t+=1
                else:
                    print("The pawn can't move to this position.")
                    print("Try again.")

        if(t==1):
            break

    if(l==1):
        b[z1-1][y1-1][x1-1]='WP'
        t+=1

    else:
        b[z1-1][y1-1][x1-1]='BP'

    b[z-1][y-1][x-1]='__'





def elephant(p):
    d=["__","__"]
    l=0
    if(p=='w'):
        a=0
        l=1
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WE'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    else:
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BE'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    print("The positions of your elephants are as follows:\n",d)
    a=1000
    for i in range(a):
        print("Enter the coordinates of the elephant you want to move\n")
        z=int(input())
        y=int(input())
        x=int(input())
        print(x+y+z)
        t=0
        if(l==1):
            if(b[z-1][y-1][x-1]=="WE"):
                t+=1

        else:
            if(b[z-1][y-1][x-1]=="BE"):
                t+=1

        if(t==0):
            print("You don't have an elephant at these coordinates")
            print("Try again.")

        else:
            break

    t=0
    for i in range(a):
        print("Enter the coordinates of the position you want to move the elephant to\n")
        z1=int(input())
        y1=int(input())
        x1=int(input())
        if(((x1==x)and(y1==y)and(z1!=z))or((x1==x)and(y1!=y)and(z1==z))or((x1!=x)and(y1==y)and(z1==z))):
            if(l==1):
                if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                    print("The elephant can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1
            else:
                if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                    print("The elephant can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1


        else:
            print("The elephant can't move to this position.")
            print("Try again.")

        if(t==1):
            break

    if(l==1):
        b[z1-1][y1-1][x1-1]='WE'
        t+=1

    else:
        b[z1-1][y1-1][x1-1]='BE'

    b[z-1][y-1][x-1]='__'




def horse(p):
    d=["__","__"]
    l=0
    if(p=='w'):
        a=0
        l=1
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WH'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    else:
        a=0
        l=2
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BH'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    print("The positions of your horses are as follows:\n",d)
    a=1000
    for i in range(a):
        print("Enter the coordinates of the horse you want to move\n")
        z=int(input())
        y=int(input())
        x=int(input())
        print(x+y+z)
        t=0
        if(l==1):
            if(b[z-1][y-1][x-1]=="WH"):
                t+=1

        else:
            if(b[z-1][y-1][x-1]=="BH"):
                t+=1

        if(t==0):
            print("You don't have a horse at these coordinates")
            print("Try again.")

        else:
            break

    t=0
    for i in range(a):
        print("Enter the coordinates of the position you want to move the horse to\n")
        z1=int(input())
        y1=int(input())
        x1=int(input())
        if(((x1==x-1)and(y1==y+2)and(z1==z))or((x1==x-1)and(y1==y+2)and(z1==z))or((x1==x+2)and(y1==y+1)and(z1==z))or((x1==x-2)and(y1==y+1)and(z1==z))or((x1==x+1)and(y1==y-2)and(z1==z))or((x1==x-1)and(y1==y-2)and(z1==z))or((x1==x-2)and(y1==y-1)and(z1==z))or((x1==x+2)and(y1==y-1)and(z1==z))or((x1==x-2)and(y1==y)and(z1==z+1))or((x1==x+2)and(y1==y)and(z1==z+1))or((x1==x)and(y1==y+2)and(z1==z+1))or((x1==x)and(y1==y-2)and(z1==z+1))or((x1==x-1)and(y1==y)and(z1==z+2))or((x1==x+1)and(y1==y)and(z1==z+2))or((x1==x)and(y1==y+1)and(z1==z+2))or((x1==x)and(y1==y-1)and(z1==z+2))or((x1==x-2)and(y1==y)and(z1==z-1))or((x1==x+2)and(y1==y)and(z1==z-1))or((x1==x)and(y1==y+2)and(z1==z-1))or((x1==x)and(y1==y-2)and(z1==z-1))or((x1==x-1)and(y1==y)and(z1==z-2))or((x1==x+1)and(y1==y)and(z1==z-2))or((x1==x)and(y1==y+1)and(z1==z-2))or((x1==x)and(y1==y-1)and(z1==z-2))):
            if(l==1):
                if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                    print("The horse can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1
            else:
                if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                    print("The horse can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1


        else:
            print("The horse can't move to this position.")
            print("Try again.")

        if(t==1):
            break

    if(l==1):
        b[z1-1][y1-1][x1-1]='WH'
        t+=1

    else:
        b[z1-1][y1-1][x1-1]='BH'

    b[z-1][y-1][x-1]='__'



def camel(p):
    d=["__","__"]
    l=0
    if(p=='w'):
        a=0
        l=1
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WC'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    else:
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BC'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==2):
                        break
    print("The positions of your camels are as follows:\n",d)
    a=1000
    for i in range(a):
        print("Enter the coordinates of the camel you want to move\n")
        z=int(input())
        y=int(input())
        x=int(input())
        print(x+y+z)
        t=0
        if(l==1):
            if(b[z-1][y-1][x-1]=="WC"):
                t+=1

        else:
            if(b[z-1][y-1][x-1]=="BC"):
                t+=1

        if(t==0):
            print("You don't have a camel at these coordinates\n")
            print("Try again.")

        else:
            break


    t=0
    for i in range(a):
        print("Enter the coordinates of the position you want to move the camel to\n")
        z1=int(input())
        y1=int(input())
        x1=int(input())
        if(x1==x):
            c=y-y1
            if(c<0):
                c=-c
            if(((y1==y+c)and(z1==z-c))or((y1==y+c)and(z1==z-c))):
                print(c)

            if(l==1):
                if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1
            else:
                if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1



        elif(y1==y):
            c=x-x1
            if(c<0):
                c=-c
            if(((x1==x+c)and(z1==z-c))or((x1==x+c)and(z1==z-c))):
                print(c)

            if(l==1):
                if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1
            else:
                if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1



        elif(z1==z):
            c=y-y1
            if(c<0):
                c=-c
            if(((y1==y+c)and(x1==x-c))or((y1==y+c)and(x1==x-c))):
                print(c)

            if(l==1):
                if(b[z1-1][y1-1][x1-1]=='WH'or b[z1-1][y1-1][x1-1]=='WP'or b[z1-1][y1-1][x1-1]=='WE'or b[z1-1][y1-1][x1-1]=='WC'or b[z1-1][y1-1][x1-1]=='WK'or b[z1-1][y1-1][x1-1]=='WQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1
            else:
                if(b[z1-1][y1-1][x1-1]=='BH'or b[z1-1][y1-1][x1-1]=='BP'or b[z1-1][y1-1][x1-1]=='BE'or b[z1-1][y1-1][x1-1]=='BC'or b[z1-1][y1-1][x1-1]=='BK'or b[z1-1][y1-1][x1-1]=='BQ'):
                    print("The camel can't move to this position because it's occupied by your own piece.")
                    print("Try again.")
                else:
                    t+=1



        else:
            print("The camel can't move to this position.")
            print("Try again.")

        if(t==1):
            break

    if(l==1):
        b[z1-1][y1-1][x1-1]='WC'
        t+=1

    else:
        b[z1-1][y1-1][x1-1]='BC'

    b[z-1][y-1][x-1]='__'


def queen(p):
    d=["__"]
    if(p=='w'):
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WQ'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==1):
                        break
    else:
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BQ'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==1):
                        break
    print("The positions of your queen are as follows:\n",d)
    print("Enter the coordinates of the elephant you want to move\n")
    y=int(input())
    z=int(input())
    x=int(input())
    print(x+y+z)


def king(p):
    d=["__"]
    if(p=='w'):
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='WK'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==1):
                        break
    else:
        a=0
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if(b[i][j][k]=='BK'):
                        d[a]=[i+1,j+1,k+1]
                        a+=1
                    if(a==1):
                        break
    print("The position of your king are is follows:\n",d)
    y=d[0][0]
    z=d[0][1]
    x=d[0][2]
    print("Enter the coordinates of the place you want to move the king to\n")
    y1=int(input())
    z1=int(input())
    x1=int(input())
    print(x+y+z)


def play(p):
    if(m>1):
        n=int(input(print('Enter 1 to print the board\n')))
        if(n==1):
            print_b()
    print("\n\nMove "+str(m)+"\n")

    if(p=='w'):
        print("It's white's turn.")
        print("What do you want to move")
        print("Enter:\n1 for pawn\n2 for elephant\n3 for horse\n4 for camel\n5 for queen\n6 for king\n")
        x=int(input())
        print(x)
        if(x==1):
            pawn(p)
        elif(x==2):
            elephant(p)
        elif(x==3):
            horse(p)
        elif(x==4):
            camel(p)
        elif(x==5):
            queen(p)
        elif(x==6):
            king(p)
        p='b'
    else:
        print("It's black's turn.")
        print("What do you want to move")
        print("Enter:\n1 for pawn\n2 for elephant\n3 for horse\n4 for camel\n5 for queen\n6 for king\n")
        x=int(input())
        print(x)
        if(x==1):
            pawn(p)
        elif(x==2):
            elephant(p)
        elif(x==3):
            horse(p)
        elif(x==4):
            camel(p)
        elif(x==5):
            queen(p)
        elif(x==6):
            king(p)
        p='w'



play(p)
p='b'
for i in range(a):
    m+=1
    x=int(input("Enter 1 to keep playing\n"))
    if(x==1):
        if(m%2==0):
            p='w'
        else:
            p='b'

        play(p)
    else:
        break
