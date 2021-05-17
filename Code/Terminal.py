import time
import board
import digitalio
import displayio

import LetterSheet
from SETUP import Setup

left = digitalio.DigitalInOut(board.D2)
left.direction = digitalio.Direction.INPUT
left.pull = digitalio.Pull.DOWN

right = digitalio.DigitalInOut(board.D10)
right.direction = digitalio.Direction.INPUT
right.pull = digitalio.Pull.DOWN

up = digitalio.DigitalInOut(board.D3)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.DOWN

down = digitalio.DigitalInOut(board.D7)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.DOWN

mysetup = Setup("/images/Maze_bitmap4.bmp")

#spry = mysetup.sprite
spry2 = mysetup.sprite2
spry3 = mysetup.sprite3
gru = mysetup.group

#mysetup.sprite_group.append(spry)
mysetup.sprite2_group.append(spry2)
mysetup.sprite3_group.append(spry3)

#gru.append(mysetup.sprite_group)
gru.append(mysetup.sprite2_group)
gru.append(mysetup.sprite3_group)

inx=50 #initial position of player
iny=15 #initial position of player

gru.x= 0
gru.y= 0

death = 0

#Body of Code/

spry2[0,0]=0
spry2[1,0]=1
spry2[2,0]=2
spry2[3,0]=3
spry2[4,0]=4
spry2[5,0]=5
spry2[6,0]=6
spry2[7,0]=7

spry2[0,1]=9
spry2[1,1]=10
spry2[2,1]=11
spry2[3,1]=12
spry2[4,1]=13
spry2[5,1]=14
spry2[6,1]=15
spry2[7,1]=16

spry2[0,2]=18
spry2[1,2]=19
spry2[2,2]=20
spry2[3,2]=21
spry2[4,2]=22
spry2[5,2]=23
spry2[6,2]=24
spry2[7,2]=25

spry2[0,3]=27
spry2[1,3]=28
spry2[2,3]=29
spry2[3,3]=30
spry2[4,3]=31
spry2[5,3]=32
spry2[6,3]=33
spry2[7,3]=34


spry3[0,0]=93

#/Body of Code

while True:


#controls player movement

    mysetup.sprite3_group.x=inx
    mysetup.sprite3_group.y=iny

    mysetup.display.show(gru)

    if left.value and inx>0:
        inx=inx-1

    if right.value and inx<125: #128 - width of tile(scale)
        inx=inx+1

    if up.value and iny>0:
        iny=iny-1

    if down.value and iny<59: #64 - height of tile(scale)
        iny=iny+1


#identifies collisions

    if mysetup.sprite_sheet[inx,iny]==1:
        death = 1
        print(death)

    if mysetup.sprite_sheet[inx+2,iny]==1:
        death = 1

    if mysetup.sprite_sheet[inx,iny+2]==1:
        death = 1

    if mysetup.sprite_sheet[inx+2,iny+2]==1:
        death = 1



    time.sleep(.01)



