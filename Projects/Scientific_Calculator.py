import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry('400x600')
        self.root.resizable(False,False)

        #Variables
        self.expression = ''
        self.memory = 0

        #Create UI
        self.create_display()
        self.create_buttons()

        #Bind keyboard
        self.root.bind('<Key>', self.key_press)

    def create_display(self):
        #Display frame
        display_frame = tk.Frame(self.root, bg = '#2c3e50', pady = 20)
        display_frame.pack(fill = tk.BOTH)

        #Expression display
        self.expr_label = tk.Label(display_frame, text = "", font = ('Arial',14), bg = '#2c3e50',fg = '#95a5a6', anchor = 'e')
        self.expr_label.pack(fill = tk.BOTH, padx = 10)

        #Result Display
        self.result_label = tk.Label(display_frame, text = '0', font = ('Arial', 24,'bold'), bg = '#2c3e50', fg = 'white', anchor = 'e')
        self.result_label.pack(fill = tk.BOTH, padx = 10)

    def create_buttons(self):
        #Button frame
        button_frame = tk.Frame(self.root, bg = '#ecf0f1')
        button_frame.pack(fill = tk.BOTH, expand = True, padx = 5, pady = 5)

        #Button Layout
        buttons = [
            ['MC', 'MR', 'M+', 'C'],
            ['sin', 'cos', 'tan', 'log', 'sqrt'],
            ['7', '8', '9', '/', '('],
            ['4', '5', '6', '*', ')'],
            ['1', '2', '3', '-', '^'],
            ['0', '.', '=', '+', 'DEL']
        ]

        #Create Buttons
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '=':
                    btn = tk.Button(button_frame, text = button_text, font = ('Arial', 14, 'bold'), bg = '#27ae60', fg = 'white', command = self.calculate)
                elif button_text in ['C', 'DEL']:
                    btn = tk.Button(button_frame, text = button_text, font = ('Arial', 14, 'bold'), bg = '#e74c3c', fg = 'white', command = lambda x = button_text: self.special_button(x))
                elif button_text in ['MC', 'MR', 'M+', 'M-']:
                    btn = tk.Button(button_frame, text = button_text, font = ('Arial', 12, 'bold'), bg = '#9b59b6', fg = 'white',command = lambda x = button_text: self.memory_operation(x))
                elif button_text in ['sin', 'cos', 'tan', 'log', 'sqrt']:
                    btn = tk.Button(button_frame, text = button_text, font = ('Arial',12), bg = '#3498db', fg = 'white', command = lambda x = button_text: self.add_to_expression(x))
                else:
                    btn = tk.Button(button_frame, text = button_text, font = ('Arial', 14), bg = '#34495e', fg = 'white', command = lambda x = button_text: self.add_to_expression(x))

                btn.grid(row = i, column = j, sticky = 'nsew', padx = 2, pady = 2)
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight = 1)
        for j in range(5):
            button_frame.grid_columnconfigure(j, weight = 1)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_display()

    def update_display(self):
        self.expr_label.config(text = self.expression)

    def calculate(self):
        try:
            #Replacing ^ with **
            expr = self.expression.replace('^', '**')

            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')
            expr = expr.replace('log', 'math.log10')
            expr = expr.replace('sqrt', 'math.sqrt')

            result = eval(expr)
            self.result_label.config(text = str(result))
            self.expression = str(result)
        
        except Exception as e:
            self.result_label.config(text = 'Error')
            self.expression = ""

    def special_button(self, button):
        if button == 'C':
            self.expression = ''
            self.result_label.config(text = '0')
            self.expr_label.config(text='')
        elif button == 'DEL':
            self.expression = self.expression[:-1]
            self.update_display()
            
    def memory_operation(self, operation):
        if operation == 'MC':
            self.memory = 0
        elif operation == 'MR':
            self.expression = str(self.memory)
            self.update_display()
        elif operation == 'M+':
            try:
                self.memory += float(self.result_label.cget('text'))
            except:
                pass
        elif operation == 'M-':
            try:
                self.memory -= float(self.result_label.cget('text'))
            except:
                pass

    def key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.()':
            self.add_to_expression(key)
        elif event.keysym == 'Return':
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.special_button('DEL')
        elif event.keysym == 'Escape':
            self.special_button('C')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()