import tkinter as tk
from tkinter import messagebox
import numpy as np


# Function to clear the previous result display
def clear_result_frame():
    for widget in result_frame.winfo_children():
        widget.destroy()


# Function to calculate determinant
def calculate_determinant():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Determinant is only defined for square matrices!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(float(value))
            matrix.append(row)

        # Convert to numpy array and calculate determinant
        np_matrix = np.array(matrix)
        determinant = round(np.linalg.det(np_matrix), 2)

        # Clear previous result and display determinant
        clear_result_frame()
        result_label = tk.Label(result_frame, text=f"Determinant = {determinant}", font=("Arial", 16, "bold"))
        result_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to check matrix properties
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
            properties = "The matrix is both one-to-one and onto."
        elif rank == cols:
            properties = "The matrix is one-to-one but not onto."
        elif rank == rows:
            properties = "The matrix is onto but not one-to-one."
        else:
            properties = "The matrix is neither one-to-one nor onto."

        # Clear previous result and display properties
        clear_result_frame()
        result_label = tk.Label(result_frame, text=f"Matrix Properties:\n{properties}", font=("Arial", 16, "bold"))
        result_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to calculate RREF using NumPy
def calculate_rref():
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
        np_matrix = np.array(matrix, dtype=float)

        # Perform Gaussian elimination to find RREF
        rref_matrix = np_matrix.copy()
        pivot_row = 0

        for pivot_col in range(cols):
            if pivot_row >= rows:
                break

            # Find the pivot row
            max_row = pivot_row + np.argmax(abs(rref_matrix[pivot_row:, pivot_col]))
            if abs(rref_matrix[max_row, pivot_col]) < 1e-10:
                continue

            # Swap rows
            rref_matrix[[pivot_row, max_row]] = rref_matrix[[max_row, pivot_row]]

            # Normalize pivot row
            rref_matrix[pivot_row] /= rref_matrix[pivot_row, pivot_col]

            # Eliminate other rows
            for i in range(rows):
                if i != pivot_row:
                    rref_matrix[i] -= rref_matrix[i, pivot_col] * rref_matrix[pivot_row]

            pivot_row += 1

        # Clear previous result and display RREF
        clear_result_frame()
        tk.Label(result_frame, text="RREF:", font=("Arial", 16, "bold")).pack()
        for i in range(rows):
            row_label = tk.Label(result_frame, text="   ".join(map(lambda x: f"{x:.2f}", rref_matrix[i])), font=("Arial", 16))
            row_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to calculate inverse matrix
def calculate_inverse():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Inverse is only defined for square matrices!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(float(value))
            matrix.append(row)

        # Convert to numpy array and calculate inverse
        np_matrix = np.array(matrix)
        inverse_matrix = np.linalg.inv(np_matrix)

        # Clear previous result and display inverse
        clear_result_frame()
        tk.Label(result_frame, text="Inverse Matrix:", font=("Arial", 16, "bold")).pack()
        for i in range(rows):
            row_label = tk.Label(result_frame, text="   ".join(map(lambda x: f"{x:.2f}", inverse_matrix[i])), font=("Arial", 16))
            row_label.pack()
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "Matrix is singular and not invertible!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to calculate transpose
def calculate_transpose():
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

        # Convert to numpy array and compute transpose
        np_matrix = np.array(matrix)
        transpose_matrix = np_matrix.T

        # Clear previous result and display transpose
        clear_result_frame()
        tk.Label(result_frame, text="Transpose Matrix:", font=("Arial", 16, "bold")).pack()
        for i in range(transpose_matrix.shape[0]):
            row_label = tk.Label(result_frame, text="   ".join(map(lambda x: f"{x:.2f}", transpose_matrix[i])), font=("Arial", 16))
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
root.title("Matrix Operations")
root.geometry("900x700")  # Expanded window size
root.configure(bg="#2c3e50")

# Top frame for title
top_frame = tk.Frame(root, bg="#1abc9c", height=80)
top_frame.pack(fill="x")

welcome_label = tk.Label(
    top_frame,
    text="Welcome to Matrix Calculator!",
    bg="#1abc9c",
    fg="black",
    font=("Arial", 24, "bold"),
)
welcome_label.pack(pady=10)

# Input frame for matrix size
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

# Frame for matrix input
matrix_frame = tk.Frame(root, bg="#34495e")
matrix_frame.pack(pady=20)

# Buttons for operations (horizontal layout)
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Determinant", command=calculate_determinant, font=("Arial", 16), width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="Properties", command=check_matrix_properties, font=("Arial", 16), width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="RREF", command=calculate_rref, font=("Arial", 16), width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="Inverse", command=calculate_inverse, font=("Arial", 16), width=15).pack(side="left", padx=10)
tk.Button(button_frame, text="Transpose", command=calculate_transpose, font=("Arial", 16), width=15).pack(side="left", padx=10)

# Frame for results
result_frame = tk.Frame(root, bg="#34495e")
result_frame.pack(pady=20)

# Run the application
root.mainloop()
