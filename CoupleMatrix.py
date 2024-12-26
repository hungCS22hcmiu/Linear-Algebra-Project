import tkinter as tk
from tkinter import messagebox
import numpy as np
from fractions import Fraction


def clear_result_frame():
    """Clear the result frame before displaying new results."""
    for widget in result_frame.winfo_children():
        widget.destroy()


def display_matrix(matrix, title="Matrix"):
    """Display a matrix neatly in the result frame."""
    clear_result_frame()
    tk.Label(result_frame, text=title, font=("Arial", 16, "bold"), bg="#34495e", fg="white").pack(pady=10)

    matrix_frame = tk.Frame(result_frame, bg="#2c3e50")
    matrix_frame.pack(pady=10)

    for row in matrix:
        row_text = "   ".join(map(str, row))
        tk.Label(matrix_frame, text=row_text, font=("Courier", 14), bg="#2c3e50", fg="white").pack(anchor="w")


def parse_fraction(value):
    """Convert a string into a fraction or float."""
    try:
        if "/" in value:
            return float(Fraction(value))
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid input: '{value}' is not a valid number or fraction.")


def read_matrix(entries):
    """Convert the entries in a grid into a 2D list of floats."""
    rows = len(entries)
    cols = len(entries[0])
    return [[parse_fraction(entries[i][j].get()) for j in range(cols)] for i in range(rows)]


def calculate_operation(operation):
    """Perform the selected operation between Matrix A and Matrix B."""
    try:
        rows_a = int(row_a_entry.get())
        cols_a = int(col_a_entry.get())
        rows_b = int(row_b_entry.get())
        cols_b = int(col_b_entry.get())

        matrix_a = np.array(read_matrix(entries_a))
        matrix_b = np.array(read_matrix(entries_b))

        if operation == "AxB" and cols_a == rows_b:
            result = np.dot(matrix_a, matrix_b)
            display_matrix(result, title="A x B")
        elif operation == "BxA" and cols_b == rows_a:
            result = np.dot(matrix_b, matrix_a)
            display_matrix(result, title="B x A")
        elif operation == "A+B" and rows_a == rows_b and cols_a == cols_b:
            result = matrix_a + matrix_b
            display_matrix(result, title="A + B")
        elif operation == "A-B" and rows_a == rows_b and cols_a == cols_b:
            result = matrix_a - matrix_b
            display_matrix(result, title="A - B")
        else:
            messagebox.showerror("Error", "Matrix dimensions are not compatible for this operation!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def create_matrix_inputs():
    """Create input fields for Matrix A and Matrix B."""
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    try:
        rows_a = int(row_a_entry.get())
        cols_a = int(col_a_entry.get())
        rows_b = int(row_b_entry.get())
        cols_b = int(col_b_entry.get())

        if rows_a > 10 or cols_a > 10 or rows_b > 10 or cols_b > 10:
            messagebox.showerror("Error", "Maximum matrix size is 10x10!")
            return

        # Create input fields for Matrix A
        global entries_a
        tk.Label(matrix_frame, text="Matrix A", bg="#34495e", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=cols_a, pady=5)
        entries_a = []
        for i in range(rows_a):
            row_entries = []
            for j in range(cols_a):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries_a.append(row_entries)

        # Create input fields for Matrix B
        global entries_b
        tk.Label(matrix_frame, text="Matrix B", bg="#34495e", fg="white", font=("Arial", 16, "bold")).grid(row=rows_a + 1, column=0, columnspan=cols_b, pady=5)
        entries_b = []
        for i in range(rows_b):
            row_entries = []
            for j in range(cols_b):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i + rows_a + 2, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries_b.append(row_entries)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for rows and columns.")


# Main window
root = tk.Tk()
root.title("Matrix Operations Calculator")
root.geometry("1000x800")
root.configure(bg="#2c3e50")

# Top frame for titles
top_frame = tk.Frame(root, bg="#1abc9c")
top_frame.pack(fill="x", pady=10)

tk.Label(top_frame, text="Matrix Operations Calculator", bg="#1abc9c", fg="black", font=("Arial", 24, "bold")).pack(pady=5)

# Input frame for matrix sizes
size_frame = tk.Frame(root, bg="#2c3e50")
size_frame.pack(pady=10)

# Inputs for Matrix A
tk.Label(size_frame, text="Matrix A Rows:", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=5)
row_a_entry = tk.Entry(size_frame, width=5, font=("Arial", 16), justify="center")
row_a_entry.grid(row=0, column=1, padx=5)

tk.Label(size_frame, text="Matrix A Columns:", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=2, padx=5)
col_a_entry = tk.Entry(size_frame, width=5, font=("Arial", 16), justify="center")
col_a_entry.grid(row=0, column=3, padx=5)

# Inputs for Matrix B
tk.Label(size_frame, text="Matrix B Rows:", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=3, column=0, padx=5)
row_b_entry = tk.Entry(size_frame, width=5, font=("Arial", 16), justify="center")
row_b_entry.grid(row=3, column=1, padx=5)

tk.Label(size_frame, text="Matrix B Columns:", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=3, column=2, padx=5)
col_b_entry = tk.Entry(size_frame, width=5, font=("Arial", 16), justify="center")
col_b_entry.grid(row=3, column=3, padx=5)

tk.Button(size_frame, text="Generate Matrices", command=create_matrix_inputs, bg="#16a085", font=("Arial", 14)).grid(row=5, column=0, columnspan=4, pady=10)

# Left frame for buttons
button_frame = tk.Frame(root, bg="#34495e")
button_frame.pack(side="left", padx=20, pady=10)

operations = [
    ("A x B", lambda: calculate_operation("AxB")),
    ("B x A", lambda: calculate_operation("BxA")),
    ("A + B", lambda: calculate_operation("A+B")),
    ("A - B", lambda: calculate_operation("A-B")),
]

for text, command in operations:
    tk.Button(button_frame, text=text, command=command, bg="#3498db", font=("Arial", 14), width=15).pack(pady=10)

# Matrix input frame
matrix_frame = tk.Frame(root, bg="#2c3e50")
matrix_frame.pack(pady=20, side="left")

# Result frame
result_frame = tk.Frame(root, bg="#34495e", relief="solid", bd=2)
result_frame.pack(pady=20, fill="both", expand=True, side="right")

# Run the application
root.mainloop()
