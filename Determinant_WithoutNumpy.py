import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

def calculate_determinant():
    try:
        # Read matrix dimensions
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Matrix must be square!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(Fraction(value))  # Parse input as a fraction
            matrix.append(row)

        # Calculate determinant using custom recursive method
        determinant = determinant_recursive(matrix)

        # Display the result as an exact fraction
        result_label.config(text=f"Determinant = {determinant}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def determinant_recursive(matrix):
    """Calculate determinant recursively using Laplace expansion."""
    size = len(matrix)

    # Base case: 1x1 matrix
    if size == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case
    det = Fraction(0)
    for col in range(size):
        # Minor matrix
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Laplace expansion
        det += ((-1) ** col) * matrix[0][col] * determinant_recursive(minor)

    return det


def create_matrix_inputs():
    # Clear any previous inputs
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        # Ensure matrix dimensions do not exceed 10x10
        if rows > 10 or cols > 10:
            messagebox.showerror("Error", "Maximum matrix size is 10x10!")
            return
        # Make sure the matrix is square
        if rows != cols:
            messagebox.showerror("Error", "Matrix must be square!")
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
    # Ensure the target cell is within bounds
    if 0 <= row < len(entries) and 0 <= col < len(entries[0]):
        target_cell = entries[row][col]
        target_cell.focus_set()


# Main window
root = tk.Tk()
root.title("Determinant Calculator")

# **Custom styles**
root.configure(bg="#2c3e50")  # Dark gray-blue background
root.geometry("900x700")  # Expanded window size

# **Top frame for welcome message**
top_frame = tk.Frame(root, bg="#1abc9c", height=80)  # Teal green background
top_frame.pack(fill="x")

welcome_label = tk.Label(
    top_frame,
    text="Welcome To Determinant Calculator!",
    bg="#1abc9c",
    fg="#000000",
    font=("Arial", 24, "bold"),
)
welcome_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(
    top_frame,
    text="Using Laplace Expansion",
    bg="#1abc9c",
    fg="black",
    font=("Arial", 20, "italic"),
)
subtitle_label.pack(pady=(0, 10))

# Input frame for matrix size
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
    bg="#16a085",  # Teal green
    fg="#000000",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=3,
)
generate_button.grid(row=0, column=4, padx=20)

# Frame for matrix input
matrix_frame = tk.Frame(root, bg="#34495e")  # Slightly lighter gray-blue
matrix_frame.pack(pady=20)

# Button to calculate determinant
calculate_button = tk.Button(
    root,
    text="Calculate Determinant",
    command=calculate_determinant,
    bg="#d3d3d3",
    fg="red",
    font=("Arial", 16, "bold"),
    width=20,
    height=2,
    relief="raised",
    bd=3,
)
calculate_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="Determinant: ", bg="#2c3e50", fg="white", font=("Arial", 18, "bold"))
result_label.pack(pady=20)

# Run the application
root.mainloop()
