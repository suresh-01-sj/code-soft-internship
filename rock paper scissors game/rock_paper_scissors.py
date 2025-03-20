from tkinter import *  # Import all classes and functions from tkinter
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL (Python Imaging Library)
from random import randint  # Import randint function from the random module

# Create the main window and set its title and background color
window = Tk()
window.title("Game Rock paper and Scissor")
window.configure(background="black")

# Load images for the game
image_rock1 = ImageTk.PhotoImage(Image.open("images/rock1.PNG"))
image_paper1 = ImageTk.PhotoImage(Image.open("images/paper1.PNG"))
image_scissor1 = ImageTk.PhotoImage(Image.open("images/scissor1.PNG"))
image_rock2 = ImageTk.PhotoImage(Image.open("images/rock2.PNG"))
image_paper2 = ImageTk.PhotoImage(Image.open("images/paper2.PNG"))
image_scissor2 = ImageTk.PhotoImage(Image.open("images/scissor2.PNG"))

# Create labels to display the images for the player and computer
label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Create labels to display the scores for the player and computer
computer_score = Label(window, text=0, font=('arial', 60, "bold"), fg="red")
player_score = Label(window, text=0, font=('arial', 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# Create labels to indicate the player and computer sections
player_indicator = Label(window, font=('arial', 40, "bold"), text="PLAYER", bg="orange", fg="blue")
computer_indicator = Label(window, font=('arial', 40, "bold"), text="COMPUTER", bg="orange", fg="blue")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

# Create a label to display the final message
final_message = Label(window, font=('arial', 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)

# List of choices for the game
to_select = ["rock", "paper", "scissor"]

def updateMessage(a):
    # Update the final message label with the given text
    final_message['text'] = a
    
def computer_Update():
    # Increment the computer's score and update the score label
    final = int(computer_score['text'])
    final += 1
    computer_score['text'] = str(final)
    
def player_Update():
    # Increment the player's score and update the score label
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)

def winner_check(p, c):
    # Determine the winner based on the player's and computer's choices
    if p == c:
        updateMessage("It is a tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins !!")
            computer_Update()
        else:
            updateMessage("Player Wins !!")
            player_Update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins !!")
            computer_Update()
        else:
            updateMessage("Player Wins !!")
            player_Update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins !!")
            computer_Update()
        else:
            updateMessage("Player Wins !!")
            player_Update()
      
def choice_update(a):
    # Update the choice for the computer and player, and determine the winner
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    
    winner_check(a, choice_computer)

# Create buttons for the player's choices and link them to the choice_update function
button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update('rock'))
button_rock.grid(row=2, column=1)

button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update('paper'))
button_paper.grid(row=2, column=2)

button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update('scissor'))
button_scissor.grid(row=2, column=3)

# Start the main event loop of the Tkinter application
window.mainloop()
