import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:

    def __init__(self, root):
        self.root = root
        self.root.title('Simple Text Editor')
        self.root.geometry('800x600')
        self.filename = None
        self.create_menu()
        self.create_text_area()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu = menubar)
        file_menu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'File', menu = file_menu)
        file_menu.add_command(label = 'New', command = self.new_file)
        file_menu.add_command(label = 'Open', command = self.open_file)
        file_menu.add_command(label = 'Save', command = self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label = 'Exit', command = self.exit_editor)

    def create_text_area(self):
        frame = tk.Frame(self.root)
        frame.pack(fill = tk.BOTH, expand = True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.text_area = tk.Text(frame, yscrollcommand = scrollbar.set,
                                font = ('Courier',12), wrap = tk.WORD)
        self.text_area.pack(fill = tk.BOTH, expand = True)
        scrollbar.config(command = self.text_area.yview)

    def new_file(self):
        self.text_area.delete('1.0', tk.END)
        self.filename = None
        self.root.title('Simple Text Editor - New File')

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension = '.txt',
            filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if self.filename:
            self.text_area.delete('1.0', tk.END)
            with open(self.filename, 'r') as file:
                self.text_area.insert('1.0', file.read())
            self.root.title(f'Text Editor - {self.filename}')

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                defaultextension = '.txt',
                filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
            )
        if self.filename:
            with open(self.filename, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))
            self.root.title(f'Text Editor - {self.filename}')

    def exit_editor(self):
        if messagebox.askokcancel('Quit','Do you want to quit?'):
            self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()