p1=input("enter player x's name: ")
p2=input("enter player o's name: ")
s='''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''
l=['123','456','789','159','357','147','258','369']
t=0
l1=[]
l2=[]
z=True
while z:
    print(s)
    if t%2==0:
        n=input(f"{p1}'s(x) turn(enter the number): ")
        if n not in l1 and n not in l2:
            l1.append(n)
            s=s.replace(n,'x')
        else:
            print('\nthat number has already been taken. enter some other number: ')
            continue  
    else:
        n=input(f"{p2}'s(o) turn(enter the number): ")
        if n not in l1 and n not in l2:
            l2.append(n)
            s=s.replace(n,'o')
        else:
            print('\nthat number has already been taken. enter some other number: ')
            continue  
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
    if len(l1)+len(l2)==9:
        print('\nit is a draw')
        print(s)
        z=False
    t+=1
    
    
    
    