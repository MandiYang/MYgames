import random
import time
from tkinter import Tk, Button, DISABLED, messagebox

def show_symbol(x, y):
    global first
    global beforeX, beforeY
    global move, pair
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        beforeX = x
        beforeY = y
        first = False
        move = move + 1
    elif beforeX != x or beforeY != y:
        if buttons[beforeX, beforeY]['text'] != buttons[x, y]['text']:
            time.sleep(0.8)
            buttons[beforeX, beforeY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[beforeX, beforeY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            pair = pair + 1
            if pair == len(buttons)/2:
                messagebox.showinfo('Matching', 'Total moves: ' +
                                    str(move), command=root.destroy())
        first = True
        
buttons = {}
first = True
beforeX = 0
beforeY = 0
move = 0
pair = 0
button_symbols = {}

symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705',  u'\u2708', u'\u2708',
           u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
           u'\u2714', u'\u2714', u'\u2716', u'\u2716',  u'\u2728', u'\u2728',
           u'\u2764', u'\u2764' , u'\u2615', u'\u2615',  u'\u2744', u'\u2744']

random.shuffle(symbols)

if __name__ =='__main__':
    root = Tk()
    root.title('Memory') 
    root.resizable(width=False, height=False)
    for x in range(6):
        for y in range(5):
            button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=3, height=3)
            button.grid(column=x, row=y)
            buttons[x, y] = button
            button_symbols[x, y] = symbols.pop()

    root.mainloop()


