from board import DISPLAY as display
import displayio


général = displayio.Group(scale=1,x=0,y=0)
display.show(général)

class rectangle:
    def __init__(self, x=0,y=0,color=0xFF0000, width=20, height=20, scale=1, hidden=False):
        
        
        self.bitmap = displayio.Bitmap(width, height, 1)

        self.palette = displayio.Palette(1)
        self.palette[0] = color
        
        tile_grid = displayio.TileGrid(self.bitmap,pixel_shader=self.palette,width=width,height=height, tile_width=1, tile_height=1)
        tile_grid.hidden = hidden
       
        self.group = displayio.Group(scale=scale,x=x,y=y)

        self.group.insert(0,tile_grid)
        général.append(self.group)
        
    
    @property
    def x(self):
        return self.group.x
    @x.setter
    def x(self, x):
        self.group.x = x
    
    @property
    def y(self):
        return self.group.y
    @y.setter
    def y(self, y):
        self.group.y = y

    @property
    def color(self):
        return self.group[0].pixel_shader[0]
    @color.setter
    def color(self, color):
        self.palette[0] = color

    @property
    def width(self):
        return self.bitmap.width

    @property
    def height(self):
        return self.bitmap.height

    @property
    def scale(self):
        return self.group.scale
    @scale.setter
    def scale(self, scale):
        self.group.scale = scale

    @property
    def hidden(self):
        return self.group[0].hidden
    @hidden.setter
    def hidden(self, hidden):
        self.group[0].hidden = hidden


class image:
    def __init__(self, x=0,y=0, scale=1, path="/thingz.bmp",hidden=False):

        file = open(path, "rb")
        self.bitmap = displayio.OnDiskBitmap(file)

        tile_grid = displayio.TileGrid(self.bitmap,pixel_shader=self.bitmap.pixel_shader)
        tile_grid.hidden = hidden
        self.group = displayio.Group(scale=scale,x=x,y=y)
        self.group.insert(0,tile_grid)
        
        général.append(self.group)
    
    @property
    def x(self):
        return self.group.x
    @x.setter
    def x(self, x):
        self.group.x = x
    
    @property
    def y(self):
        return self.group.y
    @y.setter
    def y(self, y):
        self.group.y = y

    @property
    def scale(self):
        return self.group.scale
    @scale.setter
    def scale(self, scale):
        self.group.scale = scale
    
    @property
    def hidden(self):
        return self.group[0].hidden
    @hidden.setter
    def hidden(self, hidden):
        self.group[0].hidden = hidden

    @property
    def height(self):
        return self.bitmap.height
    
    @property
    def width(self):
        return self.bitmap.width


class icon:
    def __init__(self, x=0,y=0, scale=1, name="cross",color=0xFFFFFF, hidden=False):
        path = "/lib/sprites/icons/"+name+".bmp"
        file = open(path, "rb")

        self.bitmap = displayio.OnDiskBitmap(file)
        self.new_palette = displayio.Palette(2)
        self.new_palette[0] = color

        tile_grid = displayio.TileGrid(self.bitmap,pixel_shader=self.new_palette)
        tile_grid.hidden = hidden
        self.group = displayio.Group(scale=scale,x=x,y=y)
        self.group.insert(0,tile_grid)
        
        général.append(self.group)
    
    @property
    def x(self):
        return self.group.x
    @x.setter
    def x(self, x):
        self.group.x = x
    
    @property
    def y(self):
        return self.group.y
    @y.setter
    def y(self, y):
        self.group.y = y

    @property
    def scale(self):
        return self.group.scale
    @scale.setter
    def scale(self, scale):
        self.group.scale = scale
    
    @property
    def hidden(self):
        return self.group[0].hidden
    @hidden.setter
    def hidden(self, hidden):
        self.group[0].hidden = hidden

    @property
    def height(self):
        return self.bitmap.height
    
    @property
    def width(self):
        return self.bitmap.width

    @property
    def color(self):
        return self.new_palette[0]
    @color.setter
    def color(self, color):
        self.new_palette[0] = color


def collision(a,b):
  
    if (a.x+a.width*a.scale) > b.x and (b.x+b.width*b.scale) > a.x:
        if (a.y+a.height*a.scale) > b.y and (b.y+b.height*b.scale) > a.y :
            return True
        else:
            return False        
    else:
        return False

def border_collision(border,sprite):
    if border=='n':
        return sprite.y <= 0
    if border=='s':
        return (sprite.y+sprite.height*sprite.scale) >= display.height
    if border=='w':
        return sprite.x <= 0
    if border=='e':
        return (sprite.x+sprite.width*sprite.scale) >= display.width
    return False

def version():
    return "1.0.0"

