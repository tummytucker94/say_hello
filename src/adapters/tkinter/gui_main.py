from src.core.functions.greetings import say_hello

import tkinter as tk

def create_app():
    """Create Tkinter app and return root & widgets (NO mainloop here)."""
    root = tk.Tk()
    root.title("Say Hello")

    name_entry = tk.Entry(root)
    name_entry.pack()

    output_label = tk.Label(root, text="")
    output_label.pack()

    def on_greet():
        name = name_entry.get()
        output_label.config(text=build_greeting(name))

    greet_button = tk.Button(root, text="Say Hello", command=on_greet)
    greet_button.pack()

    # IMPORTANT: just return; no mainloop here
    return root, name_entry, greet_button, output_label

def run():
    """Run app normally."""
    root, *_ = create_app()
    root.mainloop()
    
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
