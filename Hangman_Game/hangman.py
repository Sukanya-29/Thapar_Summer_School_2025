import tkinter as tk
from tkinter import messagebox
import random

class HangmanGUI:
    def __init__(self, root, words_file, stages_file):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f0f0")

        self.words = self.load_words(words_file)
        self.stages = self.load_stages(stages_file)
        self.word = random.choice(self.words)
        self.word_letters = set(self.word)
        self.correct_letters = set()
        self.guessed_letters = set()
        self.tries = 6

        self.create_widgets()

    def load_words(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def load_stages(self, filename):
        with open(filename, 'r') as file:
            return file.read().split("###")

    def create_widgets(self):
        self.root.configure(bg="#f8f6f2")  # ivory white

        self.hangman_label = tk.Label(
            self.root, text=self.stages[self.tries],
            font=("Courier", 14), justify="left",
            bg="#f8f6f2", fg="#1a1a2e"
        )
        self.hangman_label.pack(pady=10)

        self.word_label = tk.Label(
            self.root, text=" ".join(['_' for _ in self.word]),
            font=("Helvetica", 28, "bold"),
            bg="#f8f6f2", fg="#1a1a2e"
        )
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(
            self.root, font=("Helvetica", 18),
            justify='center', fg="#1a1a2e", bg="#ffffff",
            insertbackground="#1a1a2e", relief="flat"
        )
        self.entry.pack(pady=12, ipadx=5, ipady=5)
        self.entry.focus()

        self.submit_btn = tk.Button(
            self.root, text="Guess", command=self.make_guess,
            font=("Helvetica", 14, "bold"), bg="#6c63ff", fg="white",
            activebackground="#5a54d1", relief="flat", padx=10, pady=5
        )
        self.submit_btn.pack(pady=5)

        self.status_label = tk.Label(
            self.root, text=f"Tries left: {self.tries}",
            font=("Helvetica", 14), bg="#f8f6f2", fg="#555"
        )
        self.status_label.pack(pady=12)

        self.guessed_label = tk.Label(
            self.root, text="Guessed letters: ",
            font=("Helvetica", 12), bg="#f8f6f2", fg="#555"
        )
        self.guessed_label.pack(pady=8)

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid input", "Please enter a single alphabet letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already guessed", f"You already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)
        self.guessed_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

        if guess in self.word_letters:
            self.correct_letters.add(guess)
        else:
            self.tries -= 1
            self.hangman_label.config(text=self.stages[self.tries])
            self.status_label.config(text=f"Tries left: {self.tries}")

        self.update_word_display()

        if self.correct_letters == self.word_letters:
            self.end_game(True)
        elif self.tries == 0:
            self.end_game(False)

    def update_word_display(self):
        display_word = [letter if letter in self.correct_letters else '_' for letter in self.word]
        self.word_label.config(text=" ".join(display_word))

    def end_game(self, won):
        if won:
            messagebox.showinfo("Victory!", f"Congratulations! You guessed the word: {self.word}")
        else:
            messagebox.showerror("Game Over", f"You lost! The word was: {self.word}")
        self.root.destroy()

if __name__ == "__main__":
    words_file = r"hangman_game\words.txt"
    stages_file = r"hangman_game\stages.txt"

    
    root = tk.Tk()
    app = HangmanGUI(root, words_file, stages_file)
    root.mainloop()
