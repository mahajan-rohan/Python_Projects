from tkinter import *
from PIL import Image, ImageTk 
from random import randint
import os

window = Tk()
window.title("Rock-Paper-Scissors")
window.config(bg="white")
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)

rock_img_user = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img_user = ImageTk.PhotoImage(Image.open("scissors-user.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock-comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-comp.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors-comp.png"))

user_img = Label(window, image=scissors_img_user, bg="white")
comp_img = Label(window, image=scissors_img_comp, bg="white")
comp_img.grid(row=1, column=0, pady=20)
user_img.grid(row=1, column=4, pady=20)

user_score = Label(window, text=0, font=("Segoe UI Semibold", 30), bg="white", fg="black")
comp_score = Label(window, text=0, font=("Segoe UI Semibold", 30), bg="white", fg="black")
comp_score.grid(row=1, column=1)
user_score.grid(row=1, column=3)

user_label = Label(window, text="Player", font=("Segoe UI Semibold", 20), bg="white", fg="black")
user_label.grid(row=0, column=3)
comp_label = Label(window, text="Computer", font=("Segoe UI Semibold", 20), bg="white", fg="black")
comp_label.grid(row=0, column=1)

results = Label(window, text="You Lost", font=("Segoe UI Semibold", 20), bg="white", fg="black")
results.grid(row=1, column=2)

def update_results(x):
    results['text'] = x

def update_user_score():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)

def update_comp_score():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

def check_winner(user, computer):
    if user == computer:
        update_results("It's a TIE...!!!")
    elif user == "rock":
        if computer == "paper":
            update_results("You Lost...!!!")
            update_comp_score()
        else:
            update_results("You Won...!!!")
            update_user_score()
    elif user == "paper":
        if computer == "scissors":
            update_results("You Lost...!!!")
            update_comp_score()
        else:
            update_results("You Won...!!!")
            update_user_score()
    elif user == "scissors":
        if computer == "rock":
            update_results("You Lost...!!!")
            update_comp_score()
        else:
            update_results("You Won...!!!")
            update_user_score()

options = ["rock", "paper", "scissors"]

def update_selection(x):
    comp_selection = options[randint(0, 2)]
    if comp_selection == "rock":
        comp_img.configure(image=rock_img_comp)
    elif comp_selection == "paper":
        comp_img.configure(image=paper_img_comp)
    else:
        comp_img.configure(image=scissors_img_comp)

    if x == "rock":
        user_img.configure(image=rock_img_user)
    elif x == "paper":
        user_img.configure(image=paper_img_user)
    else:
        user_img.configure(image=scissors_img_user)

    check_winner(x, comp_selection)

btn_rock = Button(window, text="Rock", font=("Segoe UI Semibold", 20), bg="#5BC0EB", fg="white", command=lambda: update_selection("rock"))
btn_rock.grid(row=2, column=1, pady=20, padx=10)
btn_paper = Button(window, text="Paper", font=("Segoe UI Semibold", 20), bg="#25283D", fg="white", command=lambda: update_selection("paper"))
btn_paper.grid(row=2, column=2, pady=20, padx=10)
btn_scissors = Button(window, text="Scissors", font=("Segoe UI Semibold", 20), bg="#E4572E", fg="white", command=lambda: update_selection("scissors"))
btn_scissors.grid(row=2, column=3, pady=20, padx=10)

window.mainloop()
