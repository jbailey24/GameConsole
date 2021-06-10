# Game Console

<img src="https://github.com/jbailey24/GameConsole/blob/main/Images/IMG_7456.jpg?raw=true" alt="Image of the Game" height="300"/>      <img src="https://github.com/jbailey24/GameConsole/blob/main/Images/IMG_7460.jpg?raw=true" alt="Image of the Game" height="300"/>


My goal for this project was to create a fully-functioning, self-made game on a ssd1306 oled. Although I fell short of realizing this goal, I made significant progress towards achieving it and was able to overcome numerous obsticles along the way. I enjoyed venturing outside the relm of the projects we did in the first semester, and found it rewarding to solve encountered problems (mostly) on my own. 

My final version of the project loads up a maze onto the ssd1306 along with a square, movable player. The player can be controlled with 4 buttons (left, right, up, down) to navigate through the maze. If the player touches the maze wall, the text 'game over' appears, followed by 'your score: 00000" (the zeros act as placeholders instead of an actual time). Ideally, the game would have scored the time it took to complete the maze, and would have kept track of the fastest time. 

My biggest limiting factor was the storage space on the Metro Express. I constantly had to work around memory errors, and I don't know if I would have been able to complete the game, even when given more time, because of them. 

Click [here](https://youtu.be/extGfHxMhiU) to see a video of my project.

## The Plan

This was my first concept and brainstorm of the maze game specifically. More of my intital plan can be seen [here](https://github.com/jbailey24/GameConsole/tree/main/Plan)

<img src="https://github.com/jbailey24/GameConsole/blob/main/Plan/media/TunnelDash.PNG?raw=true" alt="Image of my Plan" width="750"/>

## Materials 

The materials I used were:
* An SSD1306 oled
* A Metro Express
* 4 buttons (in the final design the would be panel-mounted)
* 4 10k ohm resistors 
* wires


The materials I would have used if I had finished:
* acrylic board
* a panel-mounted switch (to turn on and off)
* a battery pack and batteries
* nuts and bolts

## The Wiring

<img src="https://github.com/jbailey24/GameConsole/blob/main/Images/IMG_1285.jpg?raw=true" width="650"/>

## Onshape Rendering

View in Onshape [here](https://cvilleschools.onshape.com/documents/c500101a5530eafe7376c04a/w/b9b6f445e7ac33f327785da2/e/abd8c56d3d7ee361f654bb46)

<img src="https://github.com/jbailey24/GameConsole/blob/main/Images/Screenshot%202021-06-10%2011.11.55%20AM.png?raw=true" height="300"/> <img src="https://github.com/jbailey24/GameConsole/blob/main/Images/Screenshot%202021-06-10%2011.13.02%20AM.png?raw=true" height="300"/> 
<img src="https://github.com/jbailey24/GameConsole/blob/main/Images/Screenshot%202021-06-10%2011.12.13%20AM.png?raw=true" height="300"/> <img src="https://github.com/jbailey24/GameConsole/blob/main/Images/Screenshot%202021-06-10%2011.13.55%20AM.png?raw=true" height="300"/>

Although the physical aspect of my project was fairly straightforward, I designed a model of what the finished product would look like in Onshape. I ran out of time to cut out some of the holes and add T notches along the sides of the box (to attach sides together), but the general concept of the design is complete. All of the individual parts are fixed and in their 'final' location in relation to the box.

## The Code

View the code [here](https://github.com/jbailey24/GameConsole/tree/main/Code)

The majority of this project was coding. The intitial challege was just finding out the basics of how to turn on and manipulate the display. I used many different resources to figure out the best way to do this, and eventually settled on using i2c (over SPI) and the displayio library. I found that these two guides were the most helpful in learning how to use displayio:
* [https://learn.adafruit.com/circuitpython-display-support-using-displayio/introduction](https://learn.adafruit.com/circuitpython-display-support-using-displayio/introduction)
* https://circuitpython.readthedocs.io/en/latest/shared-bindings/displayio/](https://circuitpython.readthedocs.io/en/latest/shared-bindings/displayio/)

After I decided that, I began writing the foundation of my code. It took a lot of trial and error, even with the guides, to get the basic code to work. Displayio can be confusing to wrap your mind around because of the many layers of groups, tilegrids, bitmaps, and pallettes. I ended up making my own alphabet library so that I could call different letters to spell words. Finally, once I had a solid understanding of how to create and change tilegrids, I was able to more specifially focus on the maze game. I drew up a maze, wired and added code for buttons, and worked on creating the collision system (what happens when the player touches the maze wall). 

<img src="https://github.com/jbailey24/GameConsole/blob/main/Images/IMG_6888.jpg?raw=true" height="300"/>

###### photo of testing my alphabet library

Even though I was constitaly having to work around errors and debug my code, there were several things that served as major roadblocks. The first of which was the problem of integrating functions from another file into the main code file. My goal was to have a library of functions which sewed together mutlipule differnet pixel or tile values in to cohesive sprite (aka create a letter sprite from a collecton of pixels), which I could call in the main code. These functions worked when in my main code, but when I put them in another file, they wouldn't appear on the display. After fiddling around with it some, I found out that the reason they weren't displaying was because they were being 'printed over' by the code from the main file, however I still didn't know how to solve the problem. I eventually discovered that the reason the main code and other file weren't integrating was because in the other file, I called the SETUP function, which, although having the same name as the SETUP in the main code, was actually creating another, invisible display. The solution to this was to get rid of the SETUP in the other file and to define the SETUP-dependent variables in the main code rather than the other file. This got rid of the layer confusion and allowed for the files to integrate smoothly.

Another problem I had was with the bitmap. First of all, the only way to convert an image to a monochrome bitmap with a premade system is with either Photoshop or MSPaint of all things, which, because the only way at home I have to do either of those is use my dad's laptop, made it tricky to make small edits to the bitmap. The larger issue, however, was with the peramitters of the bitmap. All tiles you use have to come from one bitmap, and there are some resitrictions on what that bitmap can be. First of all, the bitmap must be divisable by the size of all tiles you are creating. For me this meant that it had to be divisable by 16 and 3 in one direction and 16, 3, and 5 in the other. Second, called tiles have to have an index value less than 255. Third, in my scenario, in order for the code to be able to recognize collisoins, the maze had to appear exactly as it does on the display and in the top left hand corner of the bitmap. And finally, the bitmap could not exceed a certain size, or else it would throw a memory error. Balacing all of this was very difficult , and I unfortuanlty had to make some 
