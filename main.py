from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import math, os

BACKGROUND_COLOR = "#FFFFFF" # White

### FUNCTIONALITY ###
image_path = "./image_files/sample.png" # Default image is set to sample.png
ImageFont.load_default()

x = 10 # Default X (Width)
y = 10 # Default Y (Height)

def upload_picture():
    """Selects a picture to be saved to the image path variable. Default is sample.png"""
    global image_path
    filename = filedialog.askopenfilename() # Opens file explorer to select a file
    image_path = filename

def watermark_top_right():
    """Adds a watermark to the top right corner."""
    export_index = len(os.listdir("./exports/"))
    text = text_entry.get() # Gets text entry
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf",font_size) # Takes fontsize provided
    
    with Image.open(image_path).convert("RGBA") as image:      
        txt = Image.new("RGBA", image.size, (255, 255, 255, 0)) # Make a blank image for the text, initialized to transparent text color
        fnt = font
        draw = ImageDraw.Draw(txt)
        draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128)) # Draw text at half opacity, font, position
        output = Image.alpha_composite(image, txt) # Takes image provided and text
        output.save(f"./exports/watermarked_{export_index}.png")
        output.show()

def watermark_bottom_right():
    """Adds a watermark to the bottom right corner."""
    export_index = len(os.listdir("./exports/"))
    text = text_entry.get()
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf",font_size)
    
    with Image.open(image_path).convert("RGBA") as image:
        y = image.size[1] -40
        txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
        fnt = font
        draw = ImageDraw.Draw(txt)
        draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
        output = Image.alpha_composite(image, txt)
        output.save(f"./exports/watermarked_{export_index}.png")
        output.show()

def watermark_center():
    """Adds a watermark to the center of the image. X is approximate depending on length of text."""
    export_index = len(os.listdir("./exports/"))
    text = text_entry.get()
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf",font_size)
    
    with Image.open(image_path).convert("RGBA") as image:
        x = image.size[0] / 2 - 40
        y = image.size[1] /2 
        txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
        fnt = font
        draw = ImageDraw.Draw(txt)
        draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
        output = Image.alpha_composite(image, txt)
        output.save(f"./exports/watermarked_{export_index}.png")
        output.show()

def watermark_grid():
    """Adds a watermark in the patern of a grid to the image."""
    export_index = len(os.listdir("./exports/"))
    text = text_entry.get()
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf",font_size)
    x = 40

    with Image.open(image_path).convert("RGBA") as image:
        txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
        fnt = font
        draw = ImageDraw.Draw(txt)
        columns = (round(image.size[0] / 100)) # Rows (Width) on grid determined by image size
        
        # Spacing of x based on length of text
        if len(text) >= 19:
            spacing = math.floor((image.size[0] / columns) * 3.25)
        elif len(text) >= 15:
            spacing = math.floor((image.size[0] / columns) * 2.65)
        elif len(text) >= 11:
            spacing = math.floor((image.size[0] / columns) * 2.10)
        elif len(text) >= 8:
            spacing = math.floor((image.size[0] / columns) * 1.50)
        else:
            spacing = math.floor(image.size[0] / columns) + 10
        
        for column in range(columns):
            y = 40 # Needed inside for loop otherwise, only one column will be output
            while y < image.size[1]: # Itterates through height of image. Once False, next column is started
                draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
                y += 100 # Rows(Height) stays at 100 spacing increment
            x += spacing

        output = Image.alpha_composite(image, txt)
        output.save(f"./exports/watermarked_{export_index}.png")
        output.show()

def watermark_checkered():
    """Adds a watermark in a checkered pattern to the image."""
    export_index = len(os.listdir("./exports/"))
    x = 40
    text = text_entry.get()
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf",font_size)

    with Image.open(image_path).convert("RGBA") as image:
        txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
        fnt = font
        draw = ImageDraw.Draw(txt)
        columns = (round(image.size[0] / 100))
        rows = (round(image.size[1] / 100))
        
        #NOTE Spacings are not quite even for height. Still produce a checkered pattern
        if len(text) >= 20:
            x_spacing = math.floor((image.size[0] / columns) * 3.00) # Width multiple
            y_spacing = math.floor((image.size[1] / rows) * 1.26) # Height multiple
        elif len(text) >= 16:
            x_spacing = math.floor((image.size[0] / columns) * 2.45) # Width multiple
            y_spacing = math.floor((image.size[1] / rows) * 1.28) # Height multiple
        elif len(text) >= 12:
            x_spacing = math.floor((image.size[0] / columns) * 1.90) # Width multiple
            y_spacing = math.floor((image.size[1] / rows) * 1.31) # Height multiple
        elif len(text) >= 9:
            x_spacing = math.floor((image.size[0] / columns) * 1.30) # Width multiple
            y_spacing = math.floor((image.size[1] / rows) * 1.25) # Height multiple
        else:
            x_spacing = math.floor(image.size[0] / columns) #  Width default - 1.00
            y_spacing = math.floor(image.size[1] / rows) # Height default - 1.00

        for column in range(columns):
            if column % 2 == 0:
                y = 40 # Even column starting height
                while y < image.size[1]:
                    draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
                    y += y_spacing
            elif column % 2 == 1:
                y = -10 # Odd column starting height
                while y < image.size[1]:
                    y += y_spacing
                    draw.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))                    
            x += x_spacing

        output = Image.alpha_composite(image, txt)
        output.save(f"./exports/watermarked_{export_index}.png")
        output.show()
    
### GRAPHICAL INTERFACE ###
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
window.title("Tkinter Watermarking Application")
# Logo & Canvas initialization
canvas = Canvas(width=450, height=175, highlightthickness=0, bg=BACKGROUND_COLOR)
logo = PhotoImage(file="./image_files/logo_wide.png")
logo_background = canvas.create_image(200, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=3, pady=20, padx=50)

## SELECT PICTURE, WATERMARK TEXT, FONT SIZE
# LABEL - Select Picture
picture_label = Label(text="1. Select Picture")
picture_label.grid(row=1,column=0, pady=20)
# BUTTON - Select Picture
picture_button = Button(text="Select Picture", width=25, command=upload_picture)
picture_button.grid(row=1,column=1, sticky='w')
# LABEL - Text to insert
text_label = Label(text="2. Enter Text     ")
text_label.grid(row=2,column=0, pady=20)
# ENTRY FIELD - Text to insert field
text_entry = Entry(width=30)
text_entry.grid(row=2,column=1, sticky='w')
text_entry.insert(0, "Example")
# LABEL - Font size
font_size_label = Label(text="3. Font size      ")
font_size_label.grid(row=3,column=0, pady=20)
# ENTRY FIELD - Font size
font_size_entry = Entry(width=5)
font_size_entry.grid(row=3,column=1, sticky='w')
font_size_entry.insert(0, "25")

## WATERMARK LABELS
# LABEL - Select Watermark Pattern
watermark_label = Label(text="4. Select Pattern")
watermark_label.grid(row=4,column=0, pady=20)
# LABEL - Top Right
tr_label = Label(text="Top Right")
tr_label.grid(row=5,column=0)
# LABEL - Bottom Right
br_label = Label(text="Bottom Right")
br_label.grid(row=5,column=1)
# LABEL - Center
center_label = Label(text="Centered")
center_label.grid(row=5,column=2)
# LABEL - Grid
grid_label = Label(text="Grid")
grid_label.grid(row=5,column=3)
# LABEL - Checkered
checkered_label = Label(text="Checkered")
checkered_label.grid(row=5,column=4)

## WATERMARK BUTTONS
# BUTTON - Top Right Watermark
tr_watermark_img = PhotoImage(file="./image_files/top_right.png")
tr_watermark = Button(image=tr_watermark_img, highlightthickness=0, command=watermark_top_right)
tr_watermark.grid(row=6, column=0)
# BUTTON - Bottom Right Watermark
br_watermark_img = PhotoImage(file="./image_files/bottom_right.png")
br_watermark = Button(image=br_watermark_img, highlightthickness=0, command=watermark_bottom_right)
br_watermark.grid(row=6, column=1)
# BUTTON - Center Watermark
center_img = PhotoImage(file="./image_files/center.png")
center_watermark = Button(image=center_img, highlightthickness=0, command=watermark_center)
center_watermark.grid(row=6, column=2, padx=10)
# BUTTON - Grid Watermark
grid_watermark_img = PhotoImage(file="./image_files/grid.png")
grid_watermark = Button(image=grid_watermark_img, highlightthickness=0, command=watermark_grid)
grid_watermark.grid(row=6, column=3, padx=40)
# BUTTON - Checkered Watermark
checkered_watermark_img = PhotoImage(file="./image_files/checker_board.png")
checkered_watermark = Button(image=checkered_watermark_img, highlightthickness=0, command=watermark_checkered)
checkered_watermark.grid(row=6, column=4, padx=10)

window.mainloop()