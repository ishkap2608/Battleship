import random
mypoints=0
enemypoints=0
def display(a):
  for i in range(11):
    for j in range(11):
      if j==0 and i==0:
        print(" ",end=" ")
      elif j==0:
        print(chr(64+i),end=" ")
      elif i==0:
        print(j-1,end=" ")
      else:
        print(a[i-1][j-1],end=" ")
    print()
def countlist(a,b):
    x=0
    for i in range(len(a)):
        x+=a[i].count(b)
    return(x)
def strt_grid(a):
  for i in range(11):
    for j in range(11):
      if j==0 and i==0:
        print(" ",end=" ")
      elif j==0:
        print(chr(64+i),end=" ")
      elif i==0:
        print(j-1,end=" ")
      else:
        print("O",end=" ")
        a[i-1].append("O")
    print()
def position_ship(a):
  global x
  global y
  print("all ships must be in placed horizontally or vertically")
  for i in range(2,6):
    print("place ship occupying "+str(i)+" places")
    x=input("from:")
    y=input("to:")
    while len(x)!=2 and len(y)!=2 or 65>ord(x[0]) or 74<ord(x[0]) or 65>ord(y[0]) or 74<ord(y[0]) or x.isdigit() or int(x[1])<0 or int(x[1])>9:
      x=input("invalid please enter again(eg:F5):")
      y=input("to:")
    while x[0]!=y[0] and x[1]!=y[1]:
      x=input("invalid, boat must be vertically or horizontally:")
      y=input("to:")
    while x[0]==y[0] and (int(x[1])-int(y[1]))**2!=(i-1)**2 or x[1]==y[1] and (ord(x[0])-ord(y[0]))**2!=(i-1)**2:
      x=input("invalid, boat must be "+str(i)+" long:")
      y=input("to:")
    for l in range(i):
      if x[0]==y[0]:
        if int(x[1])>int(y[1]):
          a[ord(x[0])-65][int(y[1])+l]=i
        else:
          a[ord(x[0])-65][int(x[1])+l]=i
      elif x[1]==y[1]:
        if ord(x[1])-65>ord(y[1])-65:
          a[ord(y[0])-65-l][int(y[1])]=i
        else:
          a[ord(x[0])-65-l][int(x[1])]=i
    display(a)

def opp_board():
  global battle
  battle=[[],[],[],[],[],[],[],[],[],[]]
  for i in range(10):
    for j in range(10):
      battle[i-1].append("O")
  for i in range(1,5):
    if random.randint(1,2)==1:
      x=random.randint(65,74)
      y=random.randint(0,9-i)
      v=x
      w=y+i
      for j in range(i+1):
        battle[x-65][y+j]=i+1
    else:
      x=random.randint(65,74-i)
      y=random.randint(0,9)
      v=x+i
      w=y
      for j in range(i+1):
        battle[x-65+j][y]=i+1
  for i in range(2,6):
    if sum(x.count(i) for x in battle)<i:
      opp_board()
    else:
      return battle  

def grid_b():
  print("\n")
  for i in range(11):
    for j in range(11):
      if j==0 and i==0:
        print(" ",end=" ")
      elif j==0:
        print(chr(64+i),end=" ")
      elif i==0:
        print(j-1,end=" ")
      else:
        print(battle[i-1][j-1],end=" ")
    print()

def shoot_board(a):
  print("\n")
  print("Shoot Board")
  for i in range(11):
    for j in range(11):
      if j==0 and i==0:
        print(" ",end=" ")
      elif j==0:
        print(chr(64+i),end=" ")
      elif i==0:
        print(j-1,end=" ")
      else:
        print("O",end=" ")
        a[i-1].append("O")
    print()

def shot(a):
  global mypoints  
  print("\n")
  x=input("position to shoot:")
  while len(x)!=2 or 65>ord(x[0]) or 74<ord(x[0]) or int(x[1])<0 or int(x[1])>9 or a[ord(x[0])-65][int(x[1])]!="O":
    x=input("invalid please enter again(eg:F5):")
  k=battle[ord(x[0])-65][int(x[1])]
  if type(k)==int:
    print("HIT")
    a[ord(x[0])-65][int(x[1])]="*"
    battle[ord(x[0])-65][int(x[1])]="*"
    if countlist(battle,k)<1:
        mypoints+=1
        print("You have sunk the computers ship of "+str(k))
  else:
    print("MISS")
    a[ord(x[0])-65][int(x[1])]="M"

def autoshoot(a,b):
  global enemypoints  
  x=random.randint(0,9)
  y=random.randint(0,9)
  k=a[x][y]
  if type(k)==int:
    print("\n")
    print(chr(x+65)+str(y))
    print("\n")
    print("THE COMPUTER HAS HIT")
    b[x][y]="*"
    a[x][y]="*"
    if countlist(a,k)<1:
        enemypoints+=1
        print("The computer has sunk your ship of "+str(k))
  elif b[x][y]!="O":
      autoshoot(a,b)
  else:
    print("\n")
    print("THE COMPUTER HAS MISSED")
    b[x][y]="M"
def ifhit():
    if mypoints<4 and enemypoints<4:
        return True
    else:
        return False
def win():
    if mypoints>enemypoints:
        print("YOU WIN")
    elif mypoints==enemypoints:
        print("DRAW")
    else:
        print("YOU LOSE")
