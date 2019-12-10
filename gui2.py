import tkinter
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import shape_detection as sd

# import shape_detection as sd

CURRENT_FILE_PATH_BE_PROCESSED = ".\\giphy.gif"
FILE_TO_BE_EDITED = ".\\shape_rule.clp"
CURRENT_FACT_FILE = ".\\facts.txt"
CURRENT_AGENDA_FILE = ".\\agenda.txt"
CURRENT_RULES_FILE = ".\\rules.txt"

DUMMY_TEXTS = """HAMLET: To be, or not to be--that is the question:
                Whether 'tis nobler in the mind to suffer
                The slings and arrows of outrageous fortune
                Or to take arms against a sea of troubles
                And by opposing end them. To die, to sleep--
                No more--and by a sleep to say we end
                The heartache, and the thousand natural shocks
                That flesh is heir to. 'Tis a consummation
                Devoutly to be wished."""


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

    img2_data = Data()
    img2_data.id_label = ttk.Button(main_frame, image=photo)
    img2_data.id_label.image = photo
    img2_data.id_label.pack(side='left')
    img2_data.id_label['command'] = lambda: print('Detection Image')

    # Four buttons
    open_image_button = ttk.Button(main_frame,
                                   text='Open Image')
    open_image_button.pack()
    open_image_button['command'] = lambda: show_pics_open_image(img1_data, detection_result, match_facts, hit_rules, img2_data)

    rule_editor_button = ttk.Button(main_frame, text='Open rule editor')
    rule_editor_button.pack()
    rule_editor_button['command'] = lambda: go_to_editor_page()

    show_rules_button = ttk.Button(main_frame,
                                   text='Show Rules')
    show_rules_button.pack()
    show_rules_button['command'] = lambda: go_to_new_page("TOOTOOOODOOOO")  # todo

    show_facts_button = ttk.Button(main_frame,
                                   text='Show Facts')
    show_facts_button.pack()
    show_facts_button['command'] = lambda: go_to_new_page("TOOTOOOODOOOO")  # todo

    # Another Label, with its text set another way
    # label2 = ttk.Label(main_frame)
    # label2['text'] = 'What shape do you want?'
    # label2.pack()
    #
    # change_title_button5 = ttk.Button(main_frame,
    #                                   text='HMM the Title (above)')
    # change_title_button5.pack()
    # change_title_button5['command'] = lambda: print('chuan1')

    # ----------------------------------------------------------------------------------------------
    main_frame2 = ttk.Frame(root, padding=20)
    main_frame2.grid()

    lblSize1 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize1.pack(side='left', padx=20)
    detection_result = Data()
    detection_result.id_label = make_scroll(lblSize1)
    detection_result.id_label.delete('1.0', tkinter.END)
    detection_result.id_label.insert(tkinter.END, "Detection result")

    lblSize2 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize2.pack(side='left', padx=20)
    match_facts = Data()
    match_facts.id_label = make_scroll(lblSize2)
    match_facts.id_label.delete('1.0', tkinter.END)
    match_facts.id_label.insert(tkinter.END, "Match facts")

    lblSize3 = tkinter.Label(main_frame2, text="Setting form size to 500X500", font=("Comic Sans", 13), width=40)
    lblSize3.pack(side='left', padx=20)
    hit_rules = Data()
    hit_rules.id_label = make_scroll(lblSize3)
    hit_rules.id_label.delete('1.0', tkinter.END)
    hit_rules.id_label.insert(tkinter.END, "Hit Rules")

    root.mainloop()


def make_scroll(parrent, rows=15, length_per_rows=40, quote="NO FILL"):
    S = tkinter.Scrollbar(parrent)
    T = tkinter.Text(parrent, height=rows, width=length_per_rows)
    S.pack(side='right', fill=tkinter.Y)
    T.pack(side='left', fill=tkinter.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    T.insert(tkinter.END, quote)
    return T


def save_editor_page(texts):
    with open(FILE_TO_BE_EDITED, 'w') as f:
        f.write(texts)
        f.close()


def go_to_editor_page():
    root2 = tkinter.Toplevel()  # Note Toplevel, NOT Tk.

    window2_frame = ttk.Frame(root2, padding=20)
    window2_frame.grid()

    with open(FILE_TO_BE_EDITED, 'r') as f:
        output = f.read()
        lblSize = tkinter.Label(window2_frame, font=("Courier new", 13))
        lblSize.pack(side='left', padx=20)

    data_text = Data()
    data_text.id_label = make_scroll(lblSize, rows=30, length_per_rows=70, quote=output)

    decrease_button = ttk.Button(window2_frame,
                                 text='Save to shape_rule.clp')
    decrease_button.pack(side='right')
    decrease_button['command'] = lambda: save_editor_page(data_text.id_label.get('1.0', tkinter.END))


def show_pics_open_image(data, detection_result_data, match_facts_data, hit_rules_data, data2):
    f_path = filedialog.askopenfilename()
    image = Image.open(f_path)
    image = image.resize((500, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    CURRENT_FILE_PATH_BE_PROCESSED = f_path
    data.id_label['image'] = photo
    data.id_label.configure(image=photo)
    data.id_label.image = photo
    print("current file path: ", CURRENT_FILE_PATH_BE_PROCESSED)

    sd.main(f_path)

    with open(CURRENT_FACT_FILE, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]

    detection_result_data.id_label.delete('1.0', tkinter.END)
    detection_result_data.id_label.insert(tkinter.END, last_line)

    match_facts_data.id_label.delete('1.0', tkinter.END)
    match_facts_data.id_label.insert(tkinter.END, lines_in_even())

    f = open(CURRENT_AGENDA_FILE, "r")
    f = f.read()
    hit_rules_data.id_label.delete('1.0', tkinter.END)
    hit_rules_data.id_label.insert(tkinter.END, f)

    image = Image.open('output.jpg')
    image = image.resize((500, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    CURRENT_FILE_PATH_BE_PROCESSED = f_path
    data2.id_label['image'] = photo
    data2.id_label.configure(image=photo)
    data2.id_label.image = photo

    
def go_to_new_page(texts):
    root2 = tkinter.Toplevel()  # Note Toplevel, NOT Tk.

    window2_frame = ttk.Frame(root2, padding=20)
    window2_frame.grid()

    lblSize = tkinter.Label(window2_frame, font=("Courier new", 13))
    lblSize.pack(side='left', padx=20)
    make_scroll(lblSize, rows=30, length_per_rows=70, quote=texts)


def lines_in_even():
    output = ""
    rows = 0
    with open(CURRENT_FACT_FILE) as f:
        content = f.readlines()
        print(content)

        for i in range(1, len(content), 2):
            output += content[i]

    print("Output")
    print(output)
    return output



main()
