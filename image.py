import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Function to parse input as float or fraction
def parse_input(value):
    try:
        return sp.Rational(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value}")

# Function to clear the previous result display
def clear_result_frame():
    for widget in result_frame.winfo_children():
        widget.destroy()

# Function to calculate the basis for the image of T
def calculate_image_basis():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)
        image_basis = sympy_matrix.columnspace()

        clear_result_frame()
        tk.Label(result_frame, text="Basis for im(T):", font=("Arial", 16, "bold")).pack()
        for vec in image_basis:
            row_text = "   ".join(map(str, vec))
            row_label = tk.Label(result_frame, text=row_text, font=("Arial", 16))
            row_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to calculate the basis for the kernel of T
def calculate_kernel_basis():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)
        kernel_basis = sympy_matrix.nullspace()

        clear_result_frame()
        tk.Label(result_frame, text="Basis for ker(T):", font=("Arial", 16, "bold")).pack()
        for vec in kernel_basis:
            row_text = "   ".join(map(str, vec))
            row_label = tk.Label(result_frame, text=row_text, font=("Arial", 16))
            row_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to create matrix inputs
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
                row_entries.append(entry)
            entries.append(row_entries)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for rows and columns.")

# Main window
root = tk.Tk()
root.title("Matrix Transformation Calculator")
root.geometry("1000x800")
root.configure(bg="#2c3e50")

top_frame = tk.Frame(root, bg="#1abc9c", height=80)
top_frame.pack(fill="x")

welcome_label = tk.Label(
    top_frame,
    text="Matrix Transformation Calculator",
    bg="#1abc9c",
    fg="black",
    font=("Arial", 24, "bold"),
)
welcome_label.pack(pady=10)

size_frame = tk.Frame(root, bg="#2c3e50")
size_frame.pack(pady=20)

tk.Label(size_frame, text="ROWS", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=10)
row_entry = tk.Entry(size_frame, width=8, font=("Arial", 16), justify="center")
row_entry.grid(row=0, column=1, padx=10)

tk.Label(size_frame, text="COLUMNS", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=2, padx=10)
col_entry = tk.Entry(size_frame, width=8, font=("Arial", 16), justify="center")
col_entry.grid(row=0, column=3, padx=10)

generate_button = tk.Button(
    size_frame,
    text="Generate Matrix",
    command=create_matrix_inputs,
    bg="#16a085",
    fg="red",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
)
generate_button.grid(row=0, column=4, padx=20)

matrix_frame = tk.Frame(root, bg="#34495e")
matrix_frame.pack(pady=20)

button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Basis for im(T)", command=calculate_image_basis, font=("Arial", 16), width=20).pack(side="left", padx=10)
tk.Button(button_frame, text="Basis for ker(T)", command=calculate_kernel_basis, font=("Arial", 16), width=20).pack(side="left", padx=10)

result_frame = tk.Frame(root, bg="#34495e")
result_frame.pack(pady=20)

root.mainloop()
