class Color:
    #Still needs bounds checking before object init
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def get_red(self):
        return self._red
    def get_blue(self):
        return self._blue
    def get_green(self):
        return self._green
    def set_red(self, newRed):
        self._red = newRed
    def set_blue(self, newBlue):
        self._blue = newBlue
    def set_green(self, newGreen):
        self._green = newGreen
    def __str__(self):
        return f"Red: {self._red}, Green: {self._green}, Blue: {self._blue}"
    

def colInverterDupe(color):
        newRed = 255 - color.get_red()
        newBlue = 255 - color.get_blue()
        newGreen = 255 - color.get_green()
        invertedColor = Color(newRed, newGreen, newBlue)
        return invertedColor

def colInverterChange(color):
        color.set_red(255 - color.get_red())
        color.set_blue(255 - color.get_blue())
        color.set_green(255 - color.get_green())
        
    

#c1 = Color(45,55,230)
#print(c1)
#invc1 = colInverterDupe(c1)
#print(invc1)
#print(f"UpdateC1:{c1}")
#Throw test
#OOBcolor = color(-5,56,)