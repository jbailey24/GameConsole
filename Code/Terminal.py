#UNFINISHED

import time
import board
import digitalio        #used to control buttons
import displayio        #used to control display

import LetterSheet      #library of letters and numbers
from SETUP import Setup     #library which defines the display, tilegrids, and groups

#setting up the four direction buttons
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

mysetup = Setup("/images/Maze_bitmap5.bmp") #calling the Setup with Maze_bitmap5 as the bitmap

#creating variables to save me typing later
#These variables will serve as tilegrids
wdry = mysetup.words
bgry = mysetup.background
spry = mysetup.sprite
gru = mysetup.group
hsry = mysetup.highscore

#appending the tilegrids to their individual groups
mysetup.words_group.append(wdry)
mysetup.background_group.append(bgry)
mysetup.sprite_group.append(spry)
mysetup.highscore_group.append(hsry)

#appending the individual groups to the main group
gru.append(mysetup.words_group)
gru.append(mysetup.background_group)
gru.append(mysetup.sprite_group)

#setting the intital postion of the player
inx=3 
iny=38 

#setting the postion of the main group in relation to the display (the group is the size of the display, so we want it to be at 0,0)
gru.x= 0
gru.y= 0

#creating the condition death
death = 0

#Body of Code/
#(this is where I call certain tiles)

bgry[0,0]=0     #bgry are assigning the background
bgry[1,0]=1
bgry[2,0]=2
bgry[3,0]=3
bgry[4,0]=4
bgry[5,0]=5
bgry[6,0]=6
bgry[7,0]=7

bgry[0,1]=9
bgry[1,1]=10
bgry[2,1]=11
bgry[3,1]=12
bgry[4,1]=13
bgry[5,1]=14
bgry[6,1]=15
bgry[7,1]=16

bgry[0,2]=18
bgry[1,2]=19
bgry[2,2]=20
bgry[3,2]=21
bgry[4,2]=22
bgry[5,2]=23
bgry[6,2]=24
bgry[7,2]=25

bgry[0,3]=27
bgry[1,3]=28
bgry[2,3]=29
bgry[3,3]=30
bgry[4,3]=31
bgry[5,3]=32
bgry[6,3]=33
bgry[7,3]=34


LetterSheet.Letter.Y(0,0,hsry)      #assigning the YOUR SCORE: 00000 final message
LetterSheet.Letter.O(4,0,hsry)
LetterSheet.Letter.U(8,0,hsry)
LetterSheet.Letter.R(12,0,hsry)
hsry[16,0]=145
LetterSheet.Letter.S(17,0,hsry)
LetterSheet.Letter.C(21,0,hsry)
LetterSheet.Letter.O(25,0,hsry)
LetterSheet.Letter.R(29,0,hsry)
LetterSheet.Letter.E(33,0,hsry)
hsry[37,0]=131
hsry[38,0]=145
hsry[39,0]=145
LetterSheet.Letter.O(40,0,hsry)
LetterSheet.Letter.O(44,0,hsry)
LetterSheet.Letter.O(48,0,hsry)
LetterSheet.Letter.O(52,0,hsry)
LetterSheet.Letter.O(56,0,hsry)


spry[0,0]=142      #assigning the player

#/Body of Code

while True:


    #changes postion of sprite group in relation to main group
    mysetup.sprite_group.x=inx
    mysetup.sprite_group.y=iny

    #displays the main group
    mysetup.display.show(gru)

    #changes player postion based on button input
    if left.value and inx>0:
        inx=inx-1

    if right.value and inx<125: #128 - width of tile(scale)
        inx=inx+1

    if up.value and iny>0:
        iny=iny-1

    if down.value and iny<61: #64 - height of tile(scale)
        iny=iny+1


    #identifies collisions between player and maze wall
    if mysetup.sprite_sheet[inx,iny]==1:
        death = 1

    if mysetup.sprite_sheet[inx+2,iny]==1:
        death = 1

    if mysetup.sprite_sheet[inx,iny+2]==1:
        death = 1

    if mysetup.sprite_sheet[inx+2,iny+2]==1:
        death = 1

    #death sequence
    if death == 1:
        gru.remove(mysetup.background_group) #clears display
        gru.remove(mysetup.sprite_group)     #clears display
        time.sleep(0.25)
        LetterSheet.Letter.G(0,0,wdry)       #calls game over message
        LetterSheet.Letter.A(4,0,wdry)
        LetterSheet.Letter.M(8,0,wdry)
        LetterSheet.Letter.E(14,0,wdry)
        wdry[18,0]=145
        LetterSheet.Letter.O(19,0,wdry)
        LetterSheet.Letter.V(23,0,wdry)
        LetterSheet.Letter.E(27,0,wdry)
        LetterSheet.Letter.R(31,0,wdry)
        time.sleep(2)
        gru.remove(mysetup.words_group)     #clears display 
        gru.append(mysetup.highscore_group) #calls your score message
        time.sleep(60)                      #after 1 minute, an error will be thrown and the game can only be replayed when restarted or resaved



    time.sleep(.01)

