for row in range(7):
    for col in range(7):
        if (row==6 and col==0) or (row==6 and col==6):
            print("*", end=" ")
        if (row==4 and col==1) or (row==4 and col==3) or (row==4 and col==5):
            print("*", end="")
        if (row==2 and col==2) or (row==2 and col==4):
            print("*", end=" ")
        if (row==0 and col==4):
            print("*", end=" ")
        else:
            print(end=" ")
    print()

for r in range(7):
    for c in range(7):
        if (r==0 and c==2) or (r==0 and c==1) or (r==0 and c==0):
            print("*", end=" ")
        if (r==1 and c==0):
            print("*", end=" ")
        if (r==2 and c==2) or (r==2 and c==1) or (r==2 and c==0):
            print("*", end=" ")
        if (r==3 and c==6):
            print("*", end=" ")
        if (r==4 and c==2) or (r==4 and c==1) or (r==4 and c==0):
            print("*", end="  ")
        else:
            print(end=" ")
    print()

for ro in range(7):
    for co in range(7):
        if (ro==0 and co==5) or (ro==1 and co==5) or (ro==2 and co==5) or (ro==3 and co==5) or (ro==4 and co==5) or (ro==5 and co==5):
            print("*", end=" ")
        if (ro==6 and co==2) or (ro==6 and co==1) or (ro==6 and co==0):
            print("*", end=" ")
        else:
            print(end=" ")
    print()
        
for row in range(7):
    for col in range(7):
        if (row==6 and col==0) or (row==6 and col==6):
            print("*", end=" ")
        if (row==4 and col==1) or (row==4 and col==3) or (row==4 and col==5):
            print("*", end="")
        if (row==2 and col==2) or (row==2 and col==4):
            print("*", end=" ")
        if (row==0 and col==4):
            print("*", end=" ")
        else:
            print(end=" ")
    print()
      

        
       