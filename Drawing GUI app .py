import tkinter as tk

def draw(event):
  x = event.x
  y = event.y
  
  global brush_size, brush_color
  
  canvas.create_oval(x - brush_size, y - brush_size, x + brush_size, y + brush_size, fill=brush_color)


def change_brush_size(new_size):
  global brush_size
  brush_size = new_size


def change_brush_color(new_color):
  global brush_color
  brush_color = new_color

brush_size = 5
brush_color = "black"

window = tk.Tk()
window.title("Simple Drawing App")

canvas = tk.Canvas(window, width=500, height=300, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


canvas.bind("<B1-Motion>", draw)

options_frame = tk.Frame(window)
options_frame.pack()

brush_size_label = tk.Label(options_frame, text="Brush Size:")
brush_size_label.pack()

brush_size_options = [5, 10, 15]
brush_size_var = tk.IntVar()
brush_size_var.set(brush_size)  

for size in brush_size_options:
  brush_size_button = tk.Radiobutton(options_frame, text=str(size), variable=brush_size_var, command=lambda s=size: change_brush_size(s))
  brush_size_button.pack()

brush_color_label = tk.Label(options_frame, text="Brush Color:")
brush_color_label.pack()

brush_colors = ["black", "red", "blue", "green", "yellow"]

for color in brush_colors:
  color_button = tk.Button(options_frame, text=color, bg=color, command=lambda c=color: change_brush_color(c))
  color_button.pack()

window.mainloop()
