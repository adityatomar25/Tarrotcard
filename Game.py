import random
import tkinter as tk
from tkinter import messagebox

# Tarot card deck with meanings
tarot_deck = {
    "The Fool": "Beginnings, spontaneity, leap of faith",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, unconscious knowledge, mystery",
    "The Empress": "Fertility, nurturing, abundance",
    "The Emperor": "Authority, leadership, control",
    "The Hierophant": "Spiritual guidance, tradition, conformity",
    "The Lovers": "Love, partnership, choices",
    "The Chariot": "Determination, willpower, victory",
    "Strength": "Courage, inner strength, compassion",
    "The Hermit": "Soul searching, introspection, solitude",
    "Wheel of Fortune": "Luck, cycles, destiny",
    "Justice": "Fairness, balance, truth",
    "The Hanged Man": "Letting go, surrender, new perspective",
    "Death": "Endings, transformation, rebirth",
    "Temperance": "Balance, moderation, harmony",
    "The Devil": "Materialism, bondage, temptation",
    "The Tower": "Sudden upheaval, chaos, revelation",
    "The Star": "Hope, inspiration, spiritual guidance",
    "The Moon": "Illusion, intuition, subconscious",
    "The Sun": "Joy, success, vitality",
    "Judgment": "Renewal, rebirth, accountability",
    "The World": "Completion, fulfillment, wholeness",
}

# Create an empty list to store card history
card_history = []

def draw_tarot_card():
    return random.choice(list(tarot_deck.keys()))

def interpret_card(card):
    return tarot_deck.get(card, "Meaning not found")

def draw_card_and_show_meaning():
    card = draw_tarot_card()
    meaning = interpret_card(card)
    card_history.append(f"You drew: {card}\nMeaning: {meaning}")

    # Show the drawn card and its meaning in a messagebox
    messagebox.showinfo("Tarot Card Reading", f"You drew: {card}\nMeaning: {meaning}")

def show_card_history():
    # Display the card history in a separate window
    history_text = "\n\n".join(card_history)
    messagebox.showinfo("Card History", history_text)
# Create the main GUI window
root = tk.Tk()
root.title("Tarot Card Reader")

# Create a label
label = tk.Label(root, text="Click 'Draw Card' to draw a Tarot card.")
label.pack(pady=10)

# Create a button to draw a card
draw_button = tk.Button(root, text="Draw Card", command=draw_card_and_show_meaning)
draw_button.pack(pady=10)

# Create a button to show card history
history_button = tk.Button(root, text="Card History", command=show_card_history)
history_button.pack(pady=10)

# Create a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
