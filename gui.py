import tkinter
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

IMG_WIDTH = 200
IMG_HEIGHT = 200
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
BACKGROUND_IMAGE = ImageTk


def select_image():
    global panelA, panelB
    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)


window = tkinter.Tk()
cv_img = cv2.imread("./background.jpg")
height, width, no_channels = cv_img.shape

canvas = tkinter.Canvas(window,
                        width=CANVAS_WIDTH,
                        height=CANVAS_HEIGHT,
                        highlightthickness=1,
                        highlightbackground="black"
                        )
canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
window.mainloop()

panelA = tkinter.Label(canvas,
                       image=ImageTk.PhotoImage(image=Image.fromarray(cv_img)),
                       highlightthickness=3,
                       highlightbackground="black",
                       width=IMG_WIDTH,
                       height=IMG_HEIGHT
                       # background=zzyy'red',
                       ).pack()
canvas.create_window(10, 10, anchor=tkinter.NW, window=panelA)
window.mainloop()
canvas.create_window(10, 10, anchor=tkinter.NW, window=labelA)
labelA = tkinter.Label(canvas, text="HMMM").grid(row=0, column=0)

panelB = tkinter.Label(canvas,
                       image=tkinter.PhotoImage('background.jpg'),
                       highlightthickness=3,
                       highlightbackground="black",
                       width=IMG_WIDTH,
                       height=IMG_HEIGHT,
                       background='red',
                       ).grid(row=1, column=1, padx=10, pady=10)
labelB = tkinter.Label(canvas, text="HMMM222").grid(row=0, column=1)
canvas.create_window(10, 10, anchor=tkinter.NW, window=labelB)
canvas.create_window(10, 10, anchor=tkinter.NW, window=panelB)
window.mainloop()

canvas.create_window(10, 10, anchor=tkinter.NW, window=panelB)

canvas_img1 = tkinter.Canvas(window,
                             width=IMG_WIDTH,
                             height=IMG_HEIGHT,
                             highlightthickness=1,
                             highlightbackground="black"
                             )
canvas_img1.pack(expand=tkinter.YES, fill=tkinter.BOTH)
window.mainloop()
canvas_img2 = tkinter.Canvas(window,
                             width=IMG_WIDTH,
                             height=IMG_HEIGHT,
                             highlightthickness=1,
                             highlightbackground="black"
                             )
canvas_img2.pack(expand=tkinter.YES, fill=tkinter.BOTH, side=tkinter.TOP)
widget = tkinter.Label(canvas_img1, text='SPAM1111', fg='black')
canvas_img1.create_window(10, 10, anchor=tkinter.NW, window=widget)
widget = tkinter.Label(canvas_img2, text='SPAM2222', fg='black')
canvas_img2.create_window(10, 10, anchor=tkinter.NW, window=widget)
window.mainloop()
# Create a canvas that can fit the above image
# window.mainloop()


photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
window.mainloop()
# photo = tkinter.PhotoImage(file="background.gif")
#
# root = Tk()
#
# one = Label(root, )
#
# root = Tk()
# img = ImageTk.PhotoImage(Image.open(path))
# panel = tk.Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()
