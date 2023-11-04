import tkinter
from tkinter import messagebox
import random
import pandas as pd
import pyperclip
import json


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ----------------------- SAVING THE PROGRESS ------------------------- #
def known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextcard()

# --------------------------- FLASH CARD ------------------------------ #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    original_data = pd.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}
def nextcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image = front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "Spanish", fill= "black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill ="black")
    flip_timer = window.after(3000, flashcard)
    
    

def flashcard():
    global current_card
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"] , fill="white")
    
    
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, flashcard)

#buttons

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(column=1,row=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=nextcard)
wrong_button.grid(column=0,row=1)

#canvas
canvas = tkinter.Canvas(width=800, height=526)
front = tkinter.PhotoImage(file="images/card_front.png")
back = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263 , image=front)



card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))


canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)

nextcard()

window.mainloop()