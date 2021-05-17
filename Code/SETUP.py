import time
import board
import displayio
import adafruit_imageload           #import external bitmap
import adafruit_displayio_ssd1306   #import specific code for the ssd1306 display

class Setup:

    def __init__(self, bitmap):  #imported bitmap

        displayio.release_displays()
        oled_reset = board.D9

    #defines display; change device address/width/height if needed
        i2c = board.I2C()
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3D, reset=oled_reset)
        self.display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


    #imports sprite sheet, this should contain all sprites, you'll parse them later
        self.sprite_sheet, palette = adafruit_imageload.load(bitmap, bitmap=displayio.Bitmap,palette=displayio.Palette)



    #making individual tilemaps from main sprite sheet
        #self.sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette, width = 20, height = 1, tile_width =1, tile_height = 5)    #width and height are of the tilegrid: tile_width and tile_height are the number of pixels of the bitmap
        self.sprite2 = displayio.TileGrid(self.sprite_sheet, pixel_shader=palette, width = 8, height = 4, tile_width =16, tile_height = 16)
        self.sprite3 = displayio.TileGrid(self.sprite_sheet, pixel_shader=palette, width = 1, height = 1, tile_width =3, tile_height = 5)


    #sub groups
        #self.sprite_group = displayio.Group(scale=6)
        #self.sprite_group.x=0
        #self.sprite_group.y=0

        self.sprite2_group = displayio.Group(scale=1)
        self.sprite2_group.x=0
        self.sprite2_group.y=0

        self.sprite3_group = displayio.Group(scale=1)


    #main group
        self.group = displayio.Group()