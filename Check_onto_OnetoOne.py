import tkinter as tk
from tkinter import messagebox
import numpy as np


# Check matrix properties
def check_matrix_properties():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(float(value))
            matrix.append(row)

        # Convert to numpy array
        np_matrix = np.array(matrix)

        # Calculate rank
        rank = np.linalg.matrix_rank(np_matrix)

        # Determine properties
        if rank == cols and rank == rows:
            result = "The matrix is both one-to-one and onto."
        elif rank == cols:
            result = "The matrix is one-to-one but not onto."
        elif rank == rows:
            result = "The matrix is onto but not one-to-one."
        else:
            result = "The matrix is neither one-to-one nor onto."

        # Display results
        result_label.config(text=f"Rank = {rank}\n{result}")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def create_matrix_inputs():
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows > 10 or cols > 10:
            messagebox.showerror("Error", "Maximum matrix size is 10x10!")
            return

        global entries
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i, column=j, padx=10, pady=10)

                # Bind arrow keys for navigation
                entry.bind("<Up>", lambda e, x=i, y=j: navigate_to_cell(x - 1, y))
                entry.bind("<Down>", lambda e, x=i, y=j: navigate_to_cell(x + 1, y))
                entry.bind("<Left>", lambda e, x=i, y=j: navigate_to_cell(x, y - 1))
                entry.bind("<Right>", lambda e, x=i, y=j: navigate_to_cell(x, y + 1))

                row_entries.append(entry)
            entries.append(row_entries)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for rows and columns.")


def navigate_to_cell(row, col):
    if 0 <= row < len(entries) and 0 <= col < len(entries[0]):
        target_cell = entries[row][col]
        target_cell.focus_set()


# Main window
root = tk.Tk()
root.title("Matrix Properties Checker")

# Custom styles
root.configure(bg="#2c3e50")
root.geometry("900x700")

# Top frame
top_frame = tk.Frame(root, bg="#1abc9c", height=80)
top_frame.pack(fill="x")

welcome_label = tk.Label(
    top_frame,
    text="Welcome To Matrix Properties Checker!",
    bg="#1abc9c",
    fg="#000000",
    font=("Arial", 24, "bold"),
)
welcome_label.pack(pady=10)

subtitle_label = tk.Label(
    top_frame,
    text="Check if a matrix is one-to-one, onto, both, or neither.",
    bg="#1abc9c",
    fg="black",
    font=("Arial", 20, "italic"),
)
subtitle_label.pack(pady=(0, 10))

# Input frame
size_frame = tk.Frame(root, bg="#2c3e50")
size_frame.pack(pady=20)

tk.Label(size_frame, text="ROWS", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=10)
row_entry = tk.Entry(size_frame, width=8, font=("Arial", 16), justify="center")
row_entry.grid(row=0, column=1, padx=10)

tk.Label(size_frame, text="COLUMNS:", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=2, padx=10)
col_entry = tk.Entry(size_frame, width=8, font=("Arial", 16), justify="center")
col_entry.grid(row=0, column=3, padx=10)

generate_button = tk.Button(
    size_frame,
    text="Generate Matrix",
    command=create_matrix_inputs,
    bg="#16a085",
    fg="#000000",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=3,
)
generate_button.grid(row=0, column=4, padx=20)

# Matrix input frame
matrix_frame = tk.Frame(root, bg="#34495e")
matrix_frame.pack(pady=20)

# Check button
check_button = tk.Button(
    root,
    text="Check Matrix Properties",
    command=check_matrix_properties,
    bg="#d3d3d3",
    fg="red",
    font=("Arial", 16, "bold"),
    width=25,
    height=2,
    relief="raised",
    bd=3,
)
check_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", bg="#2c3e50", fg="white", font=("Arial", 18, "bold"))
result_label.pack(pady=20)

# Run the application
root.mainloop()
