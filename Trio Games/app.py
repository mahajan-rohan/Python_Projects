import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # type: ignore
from random import randint
import os
import random

def start_rock_paper_scissors():
    window = tk.Toplevel()
    window.title("Rock-Paper-Scissors")
    window.config(bg="white")

    window_width = 950
    window_height = 550
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    window.resizable(0, 0)

    icon_path = os.path.join(os.path.dirname(__file__), 'rps_icon.ico')
    window.iconbitmap(icon_path)

    rock_img_user = ImageTk.PhotoImage(Image.open("rock-user.png"))
    paper_img_user = ImageTk.PhotoImage(Image.open("paper-user.png"))
    scissors_img_user = ImageTk.PhotoImage(Image.open("scissors-user.png"))

    rock_img_comp = ImageTk.PhotoImage(Image.open("rock-comp.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper-comp.png"))
    scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors-comp.png"))

    user_img = tk.Label(window, image=scissors_img_user, bg="white")
    comp_img = tk.Label(window, image=scissors_img_comp, bg="white")
    
    comp_img.grid(row=1, column=0, pady=20)
    user_img.grid(row=1, column=4, pady=20)

    user_score = tk.Label(window, text=0, font=("Segoe UI Semibold", 30), bg="white", fg="black")
    comp_score = tk.Label(window, text=0, font=("Segoe UI Semibold", 30), bg="white", fg="black")
    
    comp_score.grid(row=1, column=1)
    user_score.grid(row=1, column=3)

    user_label = tk.Label(window, text="Player", font=("Segoe UI Semibold", 20), bg="white", fg="black")
    user_label.grid(row=0, column=3)
    
    comp_label = tk.Label(window, text="Computer", font=("Segoe UI Semibold", 20), bg="white", fg="black")
    comp_label.grid(row=0, column=1)

    results = tk.Label(window, text="You Lost", font=("Segoe UI Semibold", 20), bg="white", fg="black")
    results.grid(row=1, column=2)

    # New label for turns left
    turns_left_label = tk.Label(window, text="Turns Left: 5", font=("Segoe UI Semibold", 20), bg="white", fg="black")
    turns_left_label.grid(row=2, column=2) 

    turns_left = 5

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
        nonlocal turns_left  # Use nonlocal to modify the outer variable
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

        # Decrement turns left and check for game over
        turns_left -= 1
        turns_left_label.config(text=f"Turns Left: {turns_left}")

        if turns_left <= 0:
            show_game_over()

    def show_game_over():
        winner_text = ""
        user_score_value = int(user_score["text"])
        comp_score_value = int(comp_score["text"])

        if user_score_value > comp_score_value:
            winner_text = "You are the Winner!"
        elif user_score_value < comp_score_value:
            winner_text = "Computer is the Winner!"
        else:
            winner_text = "It's a Tie!"

        # Create a new Toplevel window for the game over dialog
        game_over_window = tk.Toplevel(window)
        game_over_window.title("Game Over")
        
        window_width = 300
        window_height = 200
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        game_over_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        game_over_window.resizable(0, 0)
        
        # Display the result message
        result_label = tk.Label(game_over_window, text=f"{winner_text}\nDo you want to play again?", font=("Segoe UI Semibold", 14))
        result_label.pack(pady=20)

        choice_frame = tk.Frame(game_over_window)
        choice_frame.pack(pady=10,padx=10)

        # Button styles
        button_style = {
            'font': ('Segoe UI Semibold', 14),
            'fg': 'black',
            'relief': 'raised',
            'bd': 5,
            'width': 5,
            'height': 2
        }

        # Buttons for choosing marks
        tk.Button(choice_frame, text='Yes', command=lambda: [reset_game(), game_over_window.destroy()], **button_style).pack(side='left', padx=10)
        tk.Button(choice_frame, text='No', command=lambda: [window.destroy(), game_over_window.destroy()], **button_style).pack(side='left', padx=10)

        # Make this dialog modal
        game_over_window.transient(window)  # Set parent window
        game_over_window.grab_set()  # Make it modal


    def reset_game():
        # Reset scores and turns left
        user_score["text"] = "0"
        comp_score["text"] = "0"
        results['text'] = "You Lost"
        
        nonlocal turns_left
        turns_left = 5
        turns_left_label.config(text=f"Turns Left: {turns_left}")

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

    btn_rock = tk.Button(window, text="Rock", font=("Segoe UI Semibold", 20), bg="#5BC0EB", fg="white",command=lambda: update_selection("rock"))
    
    btn_rock.grid(row=3, column=1, pady=20, padx=10)
    
    btn_paper = tk.Button(window, text="Paper", font=("Segoe UI Semibold", 20), bg="#25283D", fg="white",command=lambda: update_selection("paper"))
    
    btn_paper.grid(row=3, column=2, pady=20, padx=10)
    
    btn_scissors = tk.Button(window, text="Scissors", font=("Segoe UI Semibold", 20), bg="#E4572E", fg="white",command=lambda: update_selection("scissors"))
    
    btn_scissors.grid(row=3, column=3, pady=20, padx=10)


# Tic-Tac-Toe Game Code
class TicTacToe:
    def __init__(self):
        self.window = tk.Toplevel()
        self.center_window(400, 500)
        self.window.title("Tic Tac Toe")
        icon_path = os.path.join(os.path.dirname(__file__), 'tic_tac_toe_icon.ico')
        self.window.iconbitmap(icon_path)
        self.window.resizable(False, False)
        self.window.configure(bg='#61afef')
        self.current_player = 'X'
        self.player1 = 'X'
        self.player2 = 'O'
        self.board = [' ' for _ in range(9)]
        self.create_game_board()

    def center_window(self, width, height):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_game_board(self):
        frame = tk.Frame(self.window, bg='#61afef')
        frame.place(relx=0.5, rely=0.3, anchor='center', width=350, height=200)

        # Title Label
        tk.Label(frame, text="Player 1, choose 'X' or 'O':", font=('Segoe UI Semibold', 16, 'bold'), bg='#61afef', fg='#ffffff').pack(fill=tk.X, padx=10, pady=10)


        self.choice_frame = tk.Frame(frame, bg='#61afef')
        self.choice_frame.pack(pady=10,padx=10)

        # Button styles
        button_style = {
            'font': ('Segoe UI Semibold', 14),
            'bg': '#FFC914',
            'fg': '#ffffff',
            'activebackground': '#E6B800',
            'activeforeground': '#ffffff',
            'relief': 'raised',
            'bd': 5,
            'width': 5,
            'height': 2
        }

        # Buttons for choosing marks
        tk.Button(self.choice_frame, text='X', command=lambda: self.choose_mark('X'), **button_style).pack(side='left', padx=10)
        
        button_style['bg'] = '#E4572E'  # Change color for O button
        button_style['activebackground'] = '#D04524'  # Active state color for O button
        tk.Button(self.choice_frame, text='O', command=lambda: self.choose_mark('O'), **button_style).pack(side='left', padx=10)

    def choose_mark(self, mark):
        self.player1 = mark
        self.player2 = 'O' if mark == 'X' else 'X'
        self.current_player = self.player1
        self.choice_frame.destroy()
        self.initialize_board()

    def initialize_board(self):
        # Display turn label
        self.turn_label = tk.Label(self.window,text=f"Player {self.current_player}'s turn ({self.current_player})",font=('Segoe UI Semibold', 14), bg='#AFC5D4', fg='#333333')
        
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=0,sticky='ew')

        self.buttons = []
        
        for i in range(9):
            btn = tk.Button(self.window,text='', font=('Segoe UI Semibold', 24), width=8,height=3,bg='#AFC5D4',fg='#000000',command=lambda i=i: self.make_move(i))
            
            btn.grid(row=(i // 3) + 2, column=i % 3, sticky='nsew')
            self.buttons.append(btn)

        for i in range(3):
            self.window.grid_rowconfigure(i + 2, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def make_move(self, index):
        if self.board[index] != ' ':  
            messagebox.showwarning("Cheating Alert", "This position is already marked! Try another.")
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player,bg='#FFC914' if self.current_player == 'X' else '#E4572E')

        
        if self.check_winner():
            self.show_game_over_message(f"Player {self.current_player} wins!")
        
        elif ' ' not in self.board:  
            self.show_game_over_message("It's a Tie!")
        
        else:
            # Switch players
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2
            # Update turn label
            self.turn_label.config(text=f"Player {self.current_player}'s turn ({self.current_player})")

    
    def check_winner(self):
        
         winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  [0, 3, 6], [1, 4, 7], [2, 5, 8],  [0, 4, 8], [2, 4, 6]]
         for combo in winning_combinations:
             if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                 return True
         return False

    
    def show_game_over_message(self,message):
        response = messagebox.askyesno("Game Over", f"{message}\nDo you want to play again?")
        if response:
             # Restart the game
            self.window.destroy()
            TicTacToe()  
        else:
             # Close the game window
            self.window.destroy()


# Guess the Number Game Code
class GuessTheNumberGame:
    def __init__(self):
        root = tk.Toplevel()
        root.title("Guess The Number Game")
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        root.resizable(0,0)

       # Random number between 1 and 10
        self.number=random.randint(1 ,10 )
       # Number of attempts made by the player
        self.attempts =0 
       # Maximum allowed attempts 
        self.max_attempts =5 

       # Create widgets for the game 
        self.create_widgets(root)

    def create_widgets(self , root ):
       # Header 
        tk.Label(root , text ="WELCOME TO GUESS THE NUMBER GAME" , font=("Segoe UI Semibold" ,16 ,"bold")).pack(pady=10)
       
       # Rules 
        rules =( "RULES:\n""1. The computer selects a number (1-10).\n""2. You have 5 attempts to guess the number.\n""3. Guess correctly within 5 attempts to win!"
        )
        tk.Label(root , text=rules , font=("Segoe UI Semibold" ,12) , justify ="left").pack(pady=10)

       # Input and Buttons 
        self.guess_label=tk.Label(root , text ="Enter your guess (1-10):" , font=("Segoe UI Semibold" ,12))
        self.guess_label.pack(pady=5)

       # Entry field for player's guess 
        self.guess_entry=tk.Entry(root , font=("Segoe UI Semibold" ,12))
        self.guess_entry.pack(pady=5)

       # Button to submit guess 
        self.submit_button=tk.Button(root , text ="Submit Guess" , font=("Segoe UI Semibold" ,12) , command=self.check_guess)
        self.submit_button.pack(pady=10)

       # Label to display result of guess 
        self.result_label=tk.Label(root , text="" , font=("Segoe UI Semibold" ,12))
        self.result_label.pack(pady=10)


    def check_guess(self):
        try:
            guess=int(self.guess_entry.get())
            if guess <1 or guess >10:
                raise ValueError("Out of range")

          # Increment number of attempts made 
            self.attempts +=1

            if guess==self.number:
              # Player guessed correctly 
                self.display_result(True)
            elif (self.attempts >=self.max_attempts):
              # Player has used all attempts without guessing correctly 
                self.display_result(False)
            else:
                hint ="Too high!" if guess >self.number else "Too low!"
              # Display hint and remaining attempts 
                remaining_attempts=self.max_attempts -self.attempts
                result_text=f"{hint} Attempts left: {remaining_attempts}"
              # Update result label with hint 
                self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Invalid Input","Please enter a valid number between 1 and 10.")

    def display_result(self,is_winner):
        if is_winner:
            message=f"Congratulations! You guessed the number in {self.attempts} attempts."
        else:
            message=f"You lost! The correct number was {self.number}."

      # Update result label with final message 
        self.result_label.config(text=message)

def create_main_menu():
    root = tk.Tk()
    root.title("The Triple Game Challenge")
    icon_path = os.path.join(os.path.dirname(__file__), 'game_icon.ico')
    root.iconbitmap(icon_path)
    center_window(root,400, 500)
    root.resizable(False, False)
    root.configure(bg="#282c34") 

    # Title Label
    label = tk.Label(root, text="Choose a Game", font=("Segoe UI Semibold", 24, "bold"), bg="#282c34", fg="#ffffff")
    label.pack(pady=20)

    # Button Styles
    button_style = {
        'font': ("Segoe UI Semibold", 16),'bg': "#61afef",'fg': "#ffffff",'activebackground': "#528bdb",'activeforeground': "#ffffff",'relief': 'flat',
        'bd': 0,'width': 20,'height': 2
    }

    # Game Buttons
    button1 = tk.Button(root, text="Rock-Paper-Scissors", command=start_rock_paper_scissors, **button_style)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Tic Tac Toe", command=lambda: TicTacToe(), **button_style)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Guess The Number", command=lambda: GuessTheNumberGame(), **button_style)
    button3.pack(pady=10)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Segoe UI Semibold", 16), bg="#e06c75", fg="#ffffff",activebackground="#d45d68", activeforeground="#ffffff", relief='flat', bd=0, width=20, height=2)
    exit_button.pack(pady=20)

    root.mainloop()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    create_main_menu()