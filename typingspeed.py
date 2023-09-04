import tkinter as tk
import random
import time

# List of random sentences for typing practice
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect.",
    "Type as fast as you can!",
    "Programming is fun.",
    "Python is a great language for beginners.",
]

# Function to start the typing test
def start_test():
    global start_time
    global current_sentence
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)
    input_text.delete(0, tk.END)
    start_time = time.time()
    input_text.config(state=tk.NORMAL)
    start_button.config(state=tk.DISABLED)

# Function to calculate typing speed and accuracy
def calculate_speed():
    end_time = time.time()
    typed_text = input_text.get()
    typed_words = typed_text.split()
    elapsed_time = end_time - start_time
    num_words = len(typed_words)
    words_per_minute = int(num_words / (elapsed_time / 60))
    accuracy = calculate_accuracy(current_sentence, typed_text)
    result_label.config(text=f"Speed: {words_per_minute} WPM\nAccuracy: {accuracy}%")
    input_text.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)

# Function to calculate typing accuracy
def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

# Create the main window
window = tk.Tk()
window.title("Typing Speed Tester")

# Create and configure GUI elements
sentence_label = tk.Label(window, text="", wraplength=400)
input_text = tk.Entry(window, state=tk.DISABLED, width=50)
start_button = tk.Button(window, text="Start Typing Test", command=start_test)
result_label = tk.Label(window, text="", font=("Helvetica", 12))

# Layout the GUI elements
sentence_label.pack(pady=10)
input_text.pack(pady=10)
start_button.pack()
result_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
