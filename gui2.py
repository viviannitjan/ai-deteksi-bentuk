import tkinter
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import shape_detection as sd

CURRENT_FILE_PATH_BE_PROCESSED = "D:\semester5\AI-tubes\giphy.gif"
FILE_TO_BE_EDITED = "D:\semester5\AI-tubes\shape_rule.clp"


class Data(object):
    def __init__(self):
        self.id_label = None


def main():

    root = tkinter.Tk()


    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    # The image file must be GIF (or one of several other unhelpful
    # formats). To convert a JPG or anything else, use an outside tool.
    # Note that the image file must be in the same folder as this
    # module, if you use this way to refer to the image file.
    image = Image.open(CURRENT_FILE_PATH_BE_PROCESSED)
    image = image.resize((500, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    img1_data = Data()
    img1_data.id_label = ttk.Button(main_frame, image=photo)
    img1_data.id_label.image = photo
    img1_data.id_label.pack(side='left')
    img1_data.id_label['command'] = lambda: print('Source Image')

    button2 = ttk.Button(main_frame, image=photo)
    button2.image = photo
    button2.pack(side='left')
    button2['command'] = lambda: print('Detection Image')

    # Four buttons
    open_image_button = ttk.Button(main_frame,
                                   text='Open Image')
    open_image_button.pack()
    open_image_button['command'] = lambda: show_pics_open_image(img1_data)

    rule_editor_button = ttk.Button(main_frame, text='Open rule editor')
    rule_editor_button.pack()
    rule_editor_button['command'] = lambda: go_to_editor_page()

    show_rules_button = ttk.Button(main_frame,
                                   text='Show Rules')
    show_rules_button.pack()
    show_rules_button['command'] = lambda: print('chuan1')

    show_facts_button = ttk.Button(main_frame,
                                   text='Show Facts')
    show_facts_button.pack()
    show_facts_button['command'] = lambda: print('chuan1')

    # Another Label, with its text set another way
    label2 = ttk.Label(main_frame)
    label2['text'] = 'What shape do you want?'
    label2.pack()

    change_title_button5 = ttk.Button(main_frame,
                                      text='HMM the Title (above)')
    change_title_button5.pack()
    change_title_button5['command'] = lambda: print('chuan1')

    # -----------------------------------------------------
    main_frame2 = ttk.Frame(root, padding=20)
    main_frame2.grid()

    lblSize1 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize1.pack(side='left', padx=20)
    detection_result = Data()
    detection_result.id_label = make_scroll(lblSize1)
    detection_result['text'] = "HMMMMMM"

    lblSize2 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize2.pack(side='left', padx=20)
    make_scroll(lblSize2)

    lblSize3 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize3.pack(side='left', padx=20)
    make_scroll(lblSize3)

    root.mainloop()


def make_scroll(parrent, rows=15, length_per_rows=40):
    S = tkinter.Scrollbar(parrent)
    T = tkinter.Text(parrent, height=rows, width=length_per_rows)
    S.pack(side='right', fill=tkinter.Y)
    T.pack(side='left', fill=tkinter.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """HAMLET: To be, or not to be--that is the question:
                Whether 'tis nobler in the mind to suffer
                The slings and arrows of outrageous fortune
                Or to take arms against a sea of troubles
                And by opposing end them. To die, to sleep--
                No more--and by a sleep to say we end
                The heartache, and the thousand natural shocks
                That flesh is heir to. 'Tis a consummation
                Devoutly to be wished."""
    T.insert(tkinter.END, quote)
    return T


def update_text_box(data, message):
    data.id_label['text'] = message

def go_to_editor_page():
    root2 = tkinter.Toplevel()  # Note Toplevel, NOT Tk.

    window2_frame = ttk.Frame(root2, padding=20)
    window2_frame.grid()

    lblSize = tkinter.Label(window2_frame, font=("Courier new", 13))
    lblSize.pack(side='left', padx=20)
    make_scroll(lblSize, rows=30, length_per_rows=70)

    decrease_button = ttk.Button(window2_frame,
                                 text='Save to shape_rule.clp')
    decrease_button.pack(side='right')
    decrease_button['command'] = "HMM"


def show_pics_open_image(data):
    f_path = filedialog.askopenfilename()
    image = Image.open(f_path)
    image = image.resize((500, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    CURRENT_FILE_PATH_BE_PROCESSED = f_path
    data.id_label['image'] = photo
    data.id_label.configure(image=photo);
    data.id_label.image = photo
    print("current file path: ", CURRENT_FILE_PATH_BE_PROCESSED)

def open_rule_editor():
    with open(FILE_TO_BE_EDITED, 'r') as f:
        output = f.read()



# def show_rules():


main()