class Rectangle:
    
    def __init__(self,width,height):
        self.set_width(width)
        self.set_height(height)
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
        
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*self.width+2*self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            s = ''
            for _ in range(0,self.height):
                for _ in range(0,self.width):
                    s += '*'
                s += '\n'
            return s
        else:
            return 'Too big for picture.'
        
    def get_amount_inside(self,other):
        return int(self.get_area()/other.get_area())
    
class Square(Rectangle):
    
    def __init__(self,size):
        Rectangle.__init__(self,size,size)
    
            
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self,size):
        self.set_width(size)
        self.set_height(size)