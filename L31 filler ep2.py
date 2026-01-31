import tkinter as tk
from PIL import image, imageTK
import random

class Animal:
    def __init__(self, canvas, x, y, image_path):
        self.canvas = canvas
        self.x = x
        self.y = y
        
        img = image.open(image_path)
        img = img.resize((50, 50), image.Resampling.LANCZOS)
        self.photo = imageTK.photoImage(img)
        
        self.shape = self.canvas.create_image(self.x, self.y, image=self.photo)
        
    def move(self):
        dx = random.choice([-5, 5])
        dy = random.choice([-5, 5])
        self.canvas.move(self.shape, dx, dy)
        
class cat(Animal):
    def __init__(self,canvas, x, y):
        super().__init__(canvas, y, x, "cat.png")
        
    def move(self):
        dx = random.choice([-10, 10])
        dy = random.choice([-10, 10])
        self.canvas.move(self.shape, dx, dy)
    
class dog(Animal):
    def __init__(self,canvas, x, y):
        super().__init__(canvas, y, x, "dog.png")
        
    def move(self):
        dx = random.choice([-5, 0, 5])
        dy = random.choice([-5, 0, 5])
        self.canvas.move(self.shape, dx, dy)
        
class sparrow(Animal):
    def __init__(self,canvas, x, y):
        super().__init__(canvas, y, x, "sparrow.png")
        
    def move(self):
        dx = random.choice([-8, -4, 0, 4, 8])
        dy = random.choice([-10, -5, -2])
        self.canvas.move(self.shape, dx, dy)
        
class AnimalSimmulation:
    def __init__(self,root):
        self.root = root
        self.root.title("Animal Simulation with PNG and Pillow")
        
        self.canvas = tk.canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.animals = [
            cat(self.canvas, 100, 100),
            dog(self.canvas, 200, 200),
            sparrow(self.canvas, 300, 300)
        ]
        
        self.animate()

    def animate (self):
        for animal in self.animals:
            animal.move()
            self.root.after(200, self.animate)
            
if __name__=="__main__":
    root = tk.Tk()
    app = AnimalSimmulation(root)
    root.mainloop()    