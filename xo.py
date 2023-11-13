#getting the name of the players
while True:
    p1=input("enter player x's name: ")
    p2=input("enter player o's name: ")
    if p1!=p2:
        break
    else:
        print('names are same. enter some other name')

#the tic tac toe grid    
s='''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''

#combinations for winning the game
l=['123','456','789','159','357','147','258','369']

t=0 #for deciding which player's turn
l1=[] #numbers entered by player 1
l2=[] #numbers entered by player 2
z=True

#main loop
while z:
    print(s)#printing the grid

    #deciding the player's turn
    if t%2==0:
        n=input(f"{p1}'s(x) turn(enter the number): ")#player 1's turn
        
        #checking whether the number has already been entered
        if n not in l1 and n not in l2 and n in '123456789':
            l1.append(n)
            s=s.replace(n,'x')
        elif n in l1 or n in l2:
            print('\nthat number has already been taken. enter some other number ')
            continue
        else:
            print('\ninvalid input. try again.')
            continue
    else:
        n=input(f"{p2}'s(o) turn(enter the number): ")#plsyer 2's turn

        #checking whether the number has already been entered
        if n not in l1 and n not in l2 and n in '123456789':
            l2.append(n)
            s=s.replace(n,'o')
        elif n in l1 or n in l2:
            print('\nthat number has already been taken. enter some other number ')
            continue
        else:
            print('\ninvalid input. try again.')
            continue

    #checking whether player 1 has won
    if len(l1)>=3:
        for i in l:
            for j in i:
                if j not in l1:
                    break
            else:
                print('\n',p1,' wins',sep='')
                print(s)
                z=False
                break

    #checking whether player 2 has won
    if len(l2)>=3:
        for i in l:
            for j in i:
                if j not in l2:
                    break
            else:
                print('\n',p2,' wins',sep='')
                print(s)
                z=False
                break

    if z==False:
        break
    
    #checking whether it is a draw
    if len(l1)+len(l2)==9:
        print('\nit is a draw')
        print(s)
        z=False
    t+=1
    
    
    
    
