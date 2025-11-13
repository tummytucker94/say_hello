from src.core.functions.greetings import say_hello

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Say Hello")

    # --- Name label ---
    name_label = tk.Label(root, text="Enter your name:")
    name_label.pack()

    # --- Name entry ---
    name_entry = tk.Entry(root)
    name_entry.pack()

    # --- Output label ---
    output_label = tk.Label(root, text="")
    output_label.pack()

    # --- What happens when the button is clicked ---
    def handle_click():
        name = name_entry.get()          # read text from the entry box
        greeting = say_hello(name)       # use your existing function
        output_label.config(text=greeting)  # show the result in the label

    # --- Button ---
    say_hello_button = tk.Button(root, text="Say Hello", command=handle_click)
    say_hello_button.pack()



    root.mainloop()

if __name__ == "__main__":
    main()
