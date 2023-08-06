import tkinter as tk

def calculate_bets():
    stack = float(stack_entry.get())
    pot = float(pot_entry.get())
    
    flop_bet = pot * 0.5
    turn_bet = pot * 0.75
    
    flop_bet_label.config(text=f"FLOP: {flop_bet}")
    turn_bet_label.config(text=f"TURN: {turn_bet}")

# Create the main application window
root = tk.Tk()
root.title("GGOP")
root.iconbitmap("ico\\timer_small.ico")

# Create entry fields
stack_label = tk.Label(root, text="STACK:", highlightbackground="lightblue", highlightthickness=2)
stack_label.grid(row=0, column=0)
stack_entry = tk.Entry(root, highlightbackground="lightblue", highlightthickness=2)
stack_entry.grid(row=0, column=1)

pot_label = tk.Label(root, text="POT:", highlightbackground="yellow", highlightthickness=2)
pot_label.grid(row=1, column=0)
pot_entry = tk.Entry(root, highlightbackground="yellow", highlightthickness=2)
pot_entry.grid(row=1, column=1)

# Create display fields
flop_bet_label = tk.Label(root, text="FLOP:", highlightbackground="lightgreen", highlightthickness=2)
flop_bet_label.grid(row=2, column=0, columnspan=2)

turn_bet_label = tk.Label(root, text="TURN:", highlightbackground="orange", highlightthickness=2)
turn_bet_label.grid(row=3, column=0, columnspan=2)

# Create the Calculate button
#calculate_button = tk.Button(root, text="CALC", command=calculate_bets)
#calculate_button.grid(row=4, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", highlightbackground="red", highlightthickness=4, command=calculate_bets)
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

root.mainloop()