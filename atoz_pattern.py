n = (input("enter the string upto 33 characters only:-\n"))
y = 0
for i in range(7):
        for k in range(len(n)):
            if n[k]=='d' or n[k]=="D":
                for j in range(6):
                    if ((i==0 or i==6) and j<4) or ((i==1 or i==5) and j==4) or ((i==2 or i==3 or i==4) and j==5) or j==0:
                        print("*",end="")
                    else:
                        print(end=' ')
                print(end="  ")
            elif n[k]=='h' or n[k]=='H':
                for j in range(5):
                    if j==0 or j==4 or i==3:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end="  ")
            elif n[k]=='a' or n[k]=="A":
                for j in range(5):
                    if (i==4) or (i>1 and (j==0 or j==4)) or (i==0 and j==2) or (i==1 and (j==1 or j==3)):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='s' or n[k]=="S":
                for j in range(5):
                    if i==0 or i==6 or i==3:
                        print("*",end='')
                    elif (i==1 and j==0) or (i==2 and j==0) or (i==4 and j==4) or (i==5 and j==4):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='n' or n[k]=='N':
                for j in range(7):
                    if (j==0) or (j==6) or (j==i):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='c' or n[k]=="C":
                for j in range(5):
                    if (j==0) or (i==0) or (i==6):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='u' or n[k]=="U":
                for j in range(5):
                    if (j==0) or (j==4) or (i==6):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='b' or n[k]=="B":
                for j in range(5):
                    if j==0 or ((i==3 or i==0 or i==6) and j<4) or ((i==1 or i==2 or i==4 or i==5) and j==4):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='e' or n[k]=='E':
                for j in range(5):
                    if j==0 or i==0 or i==6 or i==3:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='f' or n[k]=='F':
                for j in range(5):
                    if j==0 or i==0 or i==3:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='g' or n[k]=='G':
                for j in range(7):
                    if j==0 or i==0 or i==6 or (i==3 and j>2) or (i>2 and (j==3 or j==6)):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='i' or n[k]=='I':
                for j in range(5):
                    if i==0 or i==6 or j==2:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='j' or n[k]=='J':
                for j in range(9):
                    if i==0 or j==4 or (i>2 and j==0) or (i==6 and j<5):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='k' or n[k]=='K':
                for j in range(6):
                    if j==0 or (i==3 and j<3) or ((i==0 or i==6) and j==5) or ((i==1 or i==5) and j==4) or ((i==2 or i==4) and j==3):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='l' or n[k]=='L':
                for j in range(6):
                    if j==0 or i==6:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='m' or n[k]=='M':
                for j in range(7):
                    if j==0 or j==6 or (i==j and i<4) or (i<4 and j==(6-i)):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='o' or n[k]=='O':
                for j in range(7):
                    if j==0 or j==6 or i==0 or i==6:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='p' or n[k]=='P':
                for j in range(5):
                    if j==0 or i==0 or i==3 or (j==4 and i<4):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='q' or n[k]=='Q':
                for j in range (7):
                    if ((i==0 or i==5) and j!=6) or (i!=6 and (j==0 or j==5)) or (i==6 and j==6) or (i==3 and j==2) or (i==4 and j==3):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='r' or n[k]=='R':
                for j in range(8):
                    if j==0 or ((i==0 or i==3) and j<5) or ((i==1 or i==2 or i==4) and j==5) or (i==5 and j==6) or (i==6 and j==7):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='t' or n[k]=='T':
                for j in range(7):
                    if i==0 or j==3:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='v' or n[k]=='V':
                for j in range(13):
                    if i==j or j==12-i:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='w' or n[k]=='W':
                for j in range(7):
                    if j==0 or j==6 or (i>2 and (i==j or j==(6-i))):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='x' or n[k]=='X':
                for j in range(7):
                    if i==j or j==6-i:
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='y' or n[k]=='Y':
                for j in range(7):
                    if (6-i)==j or (j==i and i<4):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]=='z' or n[k]=='Z':
                for j in range(7):
                    if i==0 or i==6 or j==(6-i):
                        print("*",end='')
                    else:
                        print(end=' ')
                print(end='  ')
            elif n[k]==' ':
                print(end='    ')
        print()