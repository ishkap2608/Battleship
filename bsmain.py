import bsfunc
myboard=[[],[],[],[],[],[],[],[],[],[]]
shoot=[[],[],[],[],[],[],[],[],[],[]]
comp_shoot=[["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]]
bsfunc.strt_grid(myboard)
bsfunc.position_ship(myboard)
print("YOUR BOARD")
bsfunc.display(myboard)
compboard=bsfunc.opp_board()
bsfunc.shoot_board(shoot)
while bsfunc.ifhit():
    bsfunc.shot(shoot)
    bsfunc.display(shoot)
    bsfunc.autoshoot(myboard,comp_shoot)
    print("YOUR BOARD")
    bsfunc.display(myboard)
print("Game over")
bsfunc.win()
