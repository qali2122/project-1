import tkinter as tk

def click_button(value):
    current = str(entry.get())
    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=4)

# Button definitions
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '%', 'cos'
]

# Create buttons and add them to the grid
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
              command=lambda b=button: click_button(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI event loop
root.mainloop()
