
import tkinter as tk
from tkinter.colorchooser import askcolor


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint - Drawing App")
        self.root.geometry("800x600")
        
        
        self.brush_color = "black"
        self.brush_size = 5

        
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        
        self.toolbar = tk.Frame(self.root, padx=5, pady=5)
        self.toolbar.pack(fill=tk.X)

        
        self.color_button = tk.Button(self.toolbar, text="Color", command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        self.eraser_button = tk.Button(self.toolbar, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.brush_size_label = tk.Label(self.toolbar, text="Brush Size:")
        self.brush_size_label.pack(side=tk.LEFT, padx=5)

        self.brush_size_slider = tk.Scale(self.toolbar, from_=1, to=20, orient=tk.HORIZONTAL, command=self.set_brush_size)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack(side=tk.LEFT, padx=5)

        
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.last_x, self.last_y = None, None
        self.eraser_mode = False

    def change_color(self):
        
        color = askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color
            self.eraser_mode = False

    def use_eraser(self):
       
        self.eraser_mode = True

    def clear_canvas(self):
       
        self.canvas.delete("all")

    def set_brush_size(self, value):
        
        self.brush_size = int(value)

    def draw(self, event):
        
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            color = "white" if self.eraser_mode else self.brush_color
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=color, width=self.brush_size, capstyle=tk.ROUND, smooth=True)
        self.last_x, self.last_y = x, y

    def reset(self, event):
        
        self.last_x, self.last_y = None, None


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
