#------------------------------------------------------------------------------

# import tkinter as tk

# def button_click():
#     print("Button Clicked!") #Gets printed in terminal
#     label.config(text = "Button was clicked!")

# root = tk.Tk()
# root.title('Button example')

# label = tk.Label(root, text = "Click the Button")
# label.pack()

# #creating a button
# button = tk.Button(root, text = "Click Me!", command = button_click,
#                     bg = "black", fg = "white",
#                     font = ("Arial",12,'italic'))
# button.pack(pady=20)

# root.mainloop()

#-------------------------------------------------------------------------------

# import tkinter as tk

# def submit():
#     user_input  = entry.get()
#     label.config(text = f'You entered: {user_input}')
#     entry.delete(0,tk.END)

# root = tk.Tk()
# root.title("Entry Example")

# entry = tk.Entry(root, width = 30, font = ('Arial',12))
# entry.pack(padx = 20, pady = 10)

# button = tk.Button(root, text = "Submit", command = submit)
# button.pack(pady = 5)

# label = tk.Label(root, text = "Enter your text")
# label.pack(pady = 10)
# root.mainloop()

#-------------------------------------------------------------------------------

# import tkinter as tk

# def get_text():
#     content = text.get('1.0', tk.END)
#     print(content)

# def clear_text():
#     text.delete('1.0', tk.END)

# root = tk.Tk()
# root.title("Text Widget Example")

# text = tk.Text(root, height = 10, width = 40, wrap = tk.WORD)
# text.pack(padx = 10 , pady = 10)
# text.insert('1.0', "Type your text here...")

# tk.Button(root, text = "Get Text", command = get_text).pack(side = tk.LEFT, padx = 5)
# tk.Button(root, text = "Clear", command = clear_text).pack(side = tk.LEFT)

# root.mainloop()

#--------------------------------------------------------------------------------

# import tkinter as tk

# def show_selection():
#     selection = []
#     if var1.get() : selection.append("Python")
#     if var2.get() : selection.append("Java")
#     if var3.get() : selection.append("C++")
#     label.config(text = f"Selected : {",".join(selection)}")

# root = tk.Tk()
# root.title("Check Button Example")

# var1, var2, var3 = tk.IntVar(), tk.IntVar(), tk.IntVar()

# tk.Label(root, text = "Select Programming Language : ").pack(pady = 10)
# tk.Checkbutton(root, text = "Python", variable = var1).pack(anchor = tk.W)
# tk.Checkbutton(root, text = "Java", variable = var2).pack(anchor = tk.W)
# tk.Checkbutton(root, text = "C++", variable = var3).pack(anchor = tk.W)

# tk.Button(root, text = "Show selection", command = show_selection).pack(pady = 10)
# label = tk.Label(root, text = "")
# label.pack()

# root.mainloop()

#-------------------------------------------------------------------------------

# import tkinter as tk

# def show_choice():
#     label.config(text = f"You Selected : {var.get()}")

# root = tk.Tk()
# root.title("Radiobutton Example")

# var = tk.StringVar(value = "Python")

# tk.Label(root, text = "Choose your favorite : ").pack(pady = 10)
# tk.Radiobutton(root, text = "Python", variable = var, value = "Python").pack(anchor = tk.W)
# tk.Radiobutton(root, text = "Java", variable = var, value = "Java").pack(anchor = tk.W)
# tk.Radiobutton(root, text = "C++", variable = var, value = "C++").pack(anchor = tk.W)

# tk.Button(root, text = "Show Choice", command = show_choice).pack(pady = 10)
# label = tk.Label(root, text = "")
# label.pack()

# root.mainloop()

#-------------------------------------------------------------------------------

# import tkinter as tk

# def show_selection():
#     selection = listbox.curselection()
#     if selection:
#         value = listbox.get(selection[0])
#         label.config(text = f"Selected : {value}")

# root = tk.Tk()
# root.title("Listbox Example")

# listbox = tk.Listbox(root, height = 6, selectmode = tk.SINGLE)
# listbox.pack(padx = 10, pady = 10)

# for item in ["Apple", "Banana", "Orange", "Mango", "Grapes", "Strawberry"]:
#     listbox.insert(tk.END, item)

# tk.Button(root, text = "Show Selection", command = show_selection).pack(pady = 5)

# label = tk.Label(root, text = "")
# label.pack()

# root.mainloop()

#-------------------------------------------------------------------------------

# #Pack Geometry Manager
# import tkinter as tk

# root = tk.Tk()
# root.title("Pack Example")
# root.geometry('400x300')

# tk.Label(root, text = 'Top', bg = 'lightyellow').pack(side=tk.TOP, fill = tk.X)
# tk.Label(root, text = 'Bottom', bg = 'lightgreen').pack(side = tk.BOTTOM, fill = tk.X)
# tk.Label(root, text = 'Left', bg = 'lightblue').pack(side=tk.LEFT, fill = tk.Y)
# tk.Label(root, text = 'Right', bg = 'lightpink').pack(side = tk.RIGHT, fill = tk.Y)
# root.mainloop()

#-------------------------------------------------------------------------------

# # Grid Geometry Manager

# import tkinter as tk

# root = tk.Tk()
# root.title("Grid Example")

# entry = tk.Entry(root, width=20, font=('Arial', 14))  #Simple calculator layout
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons = ['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
# row, col = 1, 0
# for button_text in buttons:
#     btn = tk.Button(root, text = button_text, width=5, height=2)
#     btn.grid(row = row, column = col, padx = 2, pady = 2)
#     col += 1
#     if col > 3:
#         col, row = 0, row+1

# root.mainloop()

#-------------------------------------------------------------------------------

#Place Geometry

# import tkinter as tk

# root = tk.Tk()
# root.title("Place Example")
# root.geometry('400x300')

# label1 = tk.Label(root, text = 'At(50,50)', bg = "lightblue")        #Place widgets at specific coordinates
# label1.place(x=50,y=50)
# label2 = tk.Label(root, text = 'At(150,100)', bg = "lightgreen")
# label2.place(x=150,y=100)

# label3 = tk.Label(root, text = 'Center', bg = 'yellow')     #Using relative positioning (0.0 to 1.0)
# label3.place(relx = 0.5, rely = 0.5, anchor = 'center')

# root.mainloop()

#-------------------------------------------------------------------------------

# #Frames

# import tkinter as tk

# root = tk.Tk()
# root.title('Frame Example')
# root.geometry('400x300')

# top_frame = tk.Frame(root, bg='lightblue', height = 100)
# top_frame.pack(fill =tk.BOTH, expand = True)
# tk.Label(top_frame, text = 'Top Frame', bg = 'lightblue').pack(pady = 20)

# bottom_frame = tk.Frame(root, bg = 'lightgreen', height = 100)
# bottom_frame.pack(fill = tk.BOTH, expand = True)
# for i in range(3):
#     tk.Button(bottom_frame, text = f'Button{i+1}').grid(row =0, column = i, padx = 5, pady = 20)

# root.mainloop()

#-------------------------------------------------------------------------------

#Menu and MenuBar

# import tkinter as tk
# from tkinter import messagebox

# def new_file():
#     messagebox.showinfo('New','New File Created')

# def exit_app():
#     root.quit()

# root = tk.Tk()
# root.title('Menu Example')

# menubar = tk.Menu(root)
# root.config(menu = menubar)

# file_menu = tk.Menu(menubar, tearoff = 0)
# menubar.add_cascade(label = 'File', menu = file_menu)
# file_menu.add_command(label = 'New', command = new_file)
# file_menu.add_separator()
# file_menu.add_command(label = 'Exit', command = exit_app)

# root.mainloop()

#-------------------------------------------------------------------------------

# #message box
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title('Messagebox Example')

# def show_info():
#     messagebox.showinfo('Information', 'This is an information message')

# def show_warning():
#     messagebox.showwarning('Warning', 'This is a warning message')

# def ask_question():
#     result = messagebox.askyesno('Question','Do you like yourself?')
#     if result:
#         messagebox.showinfo('Response','Great Choice!')

# tk.Button(root, text = 'Show Info', command = show_info).pack(pady = 5)
# tk.Button(root, text = 'Show Warning', command = show_warning).pack(pady = 5)
# tk.Button(root, text = 'Ask Question', command = ask_question).pack(pady = 5)

# root.mainloop()

#-------------------------------------------------------------------------------

# #Event Handling

# import tkinter as tk

# def on_click(event):
#     label.config(text = f'Clicked at({event.x},{event.y})')

# def on_key(event):
#     label.config(text = f'Key pressed: {event.char}')

# root = tk.Tk()
# root.title("Event Handling")

# label = tk.Label(root, text = "Interact with me!",font = ('Arial',16))
# label.pack(expand = True, fill = tk.BOTH)
# label.bind('<Button-1>',on_click)
# root.bind('<Key>',on_key)

# root.mainloop()

#-------------------------------------------------------------------------------

# #Canvas Widget

# import tkinter as tk

# root = tk.Tk()
# root.title('Canvas Example')

# canvas = tk.Canvas(root, width = 400, height = 400, bg = 'white')
# canvas.pack()

# #Draw Shapes
# canvas.create_line(50,50,350,50, fill = 'red', width = 3)
# canvas.create_rectangle(50,80,200,150, fill = 'blue')
# canvas.create_oval(250,80,350,180, fill = 'green')
# canvas.create_text(200,350,text = 'Canvas drawing',font = ('Arial',18))

# root.mainloop()

#-------------------------------------------------------------------------------

# #Scrollbar

# import tkinter as tk

# root = tk.Tk()
# root.title("ScrollBar Example")

# frame = tk.Frame(root)
# frame.pack(padx = 10, pady = 10)

# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# listbox = tk.Listbox(frame, yscrollcommand = scrollbar.set, height = 10)
# listbox.pack(side = tk.LEFT)
# scrollbar.config(command = listbox.yview)

# for i in range(1,51):
#     listbox.insert(tk.END, f'Item{i}')

# root.mainloop()

#-------------------------------------------------------------------------------

# #File Dialog

# import tkinter as tk
# from tkinter import filedialog
# def open_file():
#     filename = filedialog.askopenfilename(
#         title = 'Select a file',
#         filetypes = (('Text files', '*.txt'),('All files', '*.*'))
#     )
#     if filename:
#         label.config(text = f'Selected: {filename}')

# def save_file():
#     filename = filedialog.asksaveasfilename(
#         title = 'Save file as',
#         defaultextension = '.txt',
#         filetypes = (('Text files','*.txt'),('All files', '*.*'))
#     )
#     if filename:
#         label.config(text = f'Save to: {filename}')

# def choose_directory():
#     directory = filedialog.askdirectory(title = 'Choose Directory')
#     if directory:
#         label.config(text = f'Directory: {directory}')

# root = tk.Tk()
# root.title('File dialog Example')

# tk.Button(root, text = 'Open File', command = open_file).pack(pady = 5)
# tk.Button(root, text = 'Save File', command = save_file).pack(pady = 5)
# tk.Button(root, text = 'Choose Directory', command = choose_directory).pack(pady = 5)

# label = tk.Label(root, text = 'No Selection', wraplength = 300)
# label.pack(pady = 20)

# root.mainloop()

#-------------------------------------------------------------------------------

# #Custom Classes and OOP

# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master = None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.entry = tk.Entry(self, width = 30)
#         self.entry.pack(pady = 10)

#         self.button = tk.Button(self, text = "Click Me", command = self.say_hello)
#         self.button.pack(pady = 5)

#         self.label = tk.Label(self, text = "")
#         self.label.pack(pady=10)

#     def say_hello(self):
#         name = self.entry.get()
#         if name:
#             self.label.config(text = f'Hello {name}!')
#         else:
#             self.label.config(text = "Please Enter Your Name")

# root = tk.Tk()
# root.title('OOP Example')
# app = Application(master=root)
# app.mainloop()

#-------------------------------------------------------------------------------

# #Entry Validation

# import tkinter as tk
# def validate_number(char):
#     return char.isdigit or char == ''

# root = tk.Tk()
# root.title('Validation Example')

# vcmd = (root.register(validate_number), '%S')

# tk.Label(root, text = 'Enter numbers only: ').pack(pady = 5)
# entry = tk.Entry(root, validate = 'key', validatecommand = vcmd)
# entry.pack(pady = 5)

# root.mainloop()

#-------------------------------------------------------------------------------

# #Themed Widgets(ttk)

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('TTK Example')

# ttk.Button(root, text = 'TTK Button').pack(pady = 10)

# progress = ttk.Progressbar(root, length = 200, mode = 'indeterminate')
# progress.pack(pady = 10)
# progress.start()

# combo = ttk.Combobox(root, values = ['Option 1', 'Option 2', 'Option 3'])
# combo.pack(pady = 10)
# combo.current(0)

# notebook = ttk.Notebook(root)
# notebook.pack(pady = 10, expand = True)

# tab1 = ttk.Frame(notebook)
# tab2 = ttk.Frame(notebook)
# notebook.add(tab1, text = 'Tab 1')
# notebook.add(tab2, text = 'Tab 2')

# ttk.Label(tab1, text = 'Content of Tab 1').pack()
# ttk.Label(tab2, text = 'Content of Tab 2').pack()

# root.mainloop()

#-------------------------------------------------------------------------------