import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hello": "Hi!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks!",
    "what's your name": "I'm Chatbot.",
    "bye": "Goodbye!",
    "thanks": "You're welcome.",
    "thank you": "No problem!"
}

def get_response(user_input):
    return responses.get(user_input.lower(), "I didn't understand that.")

def send_message():
    user_input = message_entry.get().strip()
    if user_input == "":
        return

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n")
    bot_response = get_response(user_input)
    chat_display.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

    message_entry.delete(0, tk.END)

    if user_input.lower() == "bye":
        root.after(1500, root.destroy)

root = tk.Tk()
root.title("Chatbot")
root.geometry("500x500")
root.resizable(False, False)

chat_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=10)

message_entry = tk.Entry(input_frame, font=("Arial", 12))
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
message_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(input_frame, text="Send", width=10, command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()
