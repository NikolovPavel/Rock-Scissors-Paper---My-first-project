import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


game_window = tk.Tk()
game_window.title('Rock-Scissors-Paper')
game_window.geometry('500x300')

label = tk.Label(game_window, text='Computer:', font=('Arial', 14))
label.pack(padx=10, pady=50)

possible_list = ['Rock', 'Paper', 'Scissors']


def lets_play():
    computer_move = random.randint(0, 2)
    if computer_move == 0:
        label.config(text="Computer's move : Rock")
    elif computer_move == 1:
        label.config(text="Computer's move : Paper")
    elif computer_move == 2:
        label.config(text="Computer's move : Scissors")

    if user_choice.get() == "Rock":
        user_choice_value = 0

    elif user_choice.get() == "Paper":
        user_choice_value = 1

    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == computer_move:
        computer_label.config(text="Draw! - "+" Computer:Let's try again!")
    elif (user_choice_value == 0 and computer_move == 1) or \
         (user_choice_value == 1 and computer_move == 2) or \
         (user_choice_value == 2 and computer_move == 0):
        computer_label.config(text="You lose! - "+" Computer:I'm better than you!")

    else:
        computer_label.config(text="Congratulations! You win !!! ")


def closing():
    if messagebox.askyesno(title='Quit', message='Are you sure you want to quit the game?'):
        game_window.destroy()


def info():
    messagebox.showinfo(title='Info', message='Rules of the game: \n Choose from Rock,Paper and '
    'Scissors and win against the computer!')


game_window.protocol("WM_DELETE_WINDOW", closing)
user_choice = ttk.Combobox(game_window, value=['Rock', 'Paper', 'Scissors'])
user_choice.current(0)
user_choice.pack()

computer_label = tk.Label(game_window, text="", font=("Arial", 10), width=50, height=4)
computer_label.pack()

button = tk.Button(game_window, text='Play!', font=("Arial", 10), command=lets_play)
button.pack()

menubar = tk.Menu(game_window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Close', command=closing)
filemenu.add_separator()
filemenu.add_command(label='Close immediately', command=exit)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label='Info', command=info)

menubar.add_cascade(menu=filemenu, label='File')
menubar.add_cascade(menu=helpmenu, label='Help')
game_window.config(menu=menubar)

game_window.mainloop()



