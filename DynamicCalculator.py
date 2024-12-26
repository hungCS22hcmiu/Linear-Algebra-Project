import tkinter as tk
from tkinter import messagebox
import sympy as sp


# Function to parse input as float or fraction
def parse_input(value):
    try:
        return sp.Rational(value)  # Use sympy's Rational for precise fraction handling
    except ValueError:
        raise ValueError(f"Invalid input: {value}")


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

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)
        determinant = sympy_matrix.det()

        clear_result_frame()
        result_text = f"Determinant = {determinant}" if determinant % 1 else f"Determinant = {int(determinant)}"
        result_label = tk.Label(result_frame, text=result_text, font=("Arial", 16, "bold"))
        result_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to calculate RREF
def calculate_rref():
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
        rref_matrix, _ = sympy_matrix.rref()

        clear_result_frame()
        tk.Label(result_frame, text="RREF:", font=("Arial", 16, "bold")).pack()
        for i in range(rref_matrix.rows):
            row_text = "   ".join(map(str, rref_matrix.row(i)))
            row_label = tk.Label(result_frame, text=row_text, font=("Arial", 16))
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

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)
        inverse_matrix = sympy_matrix.inv()

        clear_result_frame()
        tk.Label(result_frame, text="Inverse Matrix:", font=("Arial", 16, "bold")).pack()
        for i in range(inverse_matrix.rows):
            row_text = "   ".join(map(str, inverse_matrix.row(i)))
            row_label = tk.Label(result_frame, text=row_text, font=("Arial", 16))
            row_label.pack()
    except sp.MatrixError:
        messagebox.showerror("Error", "Matrix is singular and not invertible!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to calculate transpose
def calculate_transpose():
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
        transpose_matrix = sympy_matrix.T

        clear_result_frame()
        tk.Label(result_frame, text="Transpose Matrix:", font=("Arial", 16, "bold")).pack()
        for i in range(transpose_matrix.rows):
            row_text = "   ".join(map(str, transpose_matrix.row(i)))
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

# Function to calculate eigenvalues
def calculate_eigenvalues():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Eigenvalues are only defined for square matrices!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)
        eigenvalues = sympy_matrix.eigenvals().keys()  # Get eigenvalues only

        clear_result_frame()
        tk.Label(result_frame, text="Eigenvalues:", font=("Arial", 16, "bold")).pack()

        for eigenval in eigenvalues:
            # Format each eigenvalue using pretty notation
            pretty_value = sp.pretty(eigenval, use_unicode=True)
            tk.Label(result_frame, text=pretty_value, font=("Arial", 16)).pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to diagonalize a square matrix
def diagonalize_matrix():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Diagonalization is only defined for square matrices!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        sympy_matrix = sp.Matrix(matrix)

        if not sympy_matrix.is_diagonalizable():
            messagebox.showerror("Error", "The matrix is not diagonalizable!")
            return

        # Perform diagonalization
        P, D = sympy_matrix.diagonalize()
        P_inv = P.inv()

        # Display results
        clear_result_frame()

        tk.Label(result_frame, text="Diagonalization Result:", font=("Arial", 16, "bold")).pack()

        # Display P matrix
        tk.Label(result_frame, text="Matrix P:", font=("Arial", 14, "bold")).pack(pady=5)
        for i in range(P.rows):
            row_text = "   ".join(map(str, P.row(i)))
            tk.Label(result_frame, text=row_text, font=("Arial", 14)).pack()

        # Display D matrix
        tk.Label(result_frame, text="Matrix D (Diagonal):", font=("Arial", 14, "bold")).pack(pady=5)
        for i in range(D.rows):
            row_text = "   ".join(map(str, D.row(i)))
            tk.Label(result_frame, text=row_text, font=("Arial", 14)).pack()

        # Display P^-1 matrix
        tk.Label(result_frame, text="Matrix P^-1 (Inverse of P):", font=("Arial", 14, "bold")).pack(pady=5)
        for i in range(P_inv.rows):
            row_text = "   ".join(map(str, P_inv.row(i)))
            tk.Label(result_frame, text=row_text, font=("Arial", 14)).pack()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
# Function to calculate power of A using P and D
def calculate_power_of_a():
    try:
        # Read inputs for P and D
        size = int(row_entry.get())  # Assuming a square matrix of size rows x rows
        matrix_p = []
        matrix_d = []

        for i in range(size):
            row_p = [parse_input(entries_p[i][j].get()) for j in range(size)]
            row_d = [parse_input(entries_d[i][j].get()) for j in range(size)]

            matrix_p.append(row_p)
            matrix_d.append(row_d)

        # Convert to sympy matrices
        P = sp.Matrix(matrix_p)
        D = sp.Matrix(matrix_d)

        # Calculate P^-1
        try:
            P_inv = P.inv()
        except sp.NonInvertibleMatrixError:
            messagebox.showerror("Error", "Matrix P is not invertible. Cannot compute P^-1.")
            return

        # Check for the validity of diagonalization
        A = P * D * P_inv
        if not sp.simplify(P * D * P_inv - A).is_zero_matrix:
            messagebox.showerror("Error", "The provided matrices do not satisfy P * D * P^-1 = A.")
            return

        # Get the value of n
        n = int(power_entry.get())
        if n < 0:
            messagebox.showerror("Error", "Only non-negative powers are supported.")
            return

        # Compute A^n = P * D^n * P^-1
        D_power = D ** n
        A_power = P * D_power * P_inv

        # Display result
        clear_result_frame()
        tk.Label(result_frame, text=f"A^{n}:", font=("Arial", 16, "bold")).pack()

        for i in range(A_power.rows):
            row_text = "   ".join(map(str, A_power.row(i)))
            tk.Label(result_frame, text=row_text, font=("Arial", 16)).pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to create inputs for P, D matrices and power n
def create_power_matrix_inputs():
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    try:
        size = int(row_entry.get())  # Assuming square matrices
        global entries_p, entries_d, power_entry
        entries_p = []
        entries_d = []

        # Input fields for P
        tk.Label(matrix_frame, text="Matrix P", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").grid(row=0, column=0, columnspan=size)
        for i in range(size):
            row_p = []
            for j in range(size):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_p.append(entry)
            entries_p.append(row_p)

        # Input fields for D
        tk.Label(matrix_frame, text="Matrix D", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").grid(row=size + 1, column=0, columnspan=size)
        for i in range(size):
            row_d = []
            for j in range(size):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i + size + 2, column=j, padx=5, pady=5)
                row_d.append(entry)
            entries_d.append(row_d)

        # Input field for n
        tk.Label(matrix_frame, text="Power (n):", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").grid(row=(2 * size) + 3, column=0, padx=10)
        power_entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
        power_entry.grid(row=(2 * size) + 3, column=1, padx=10)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid size for square matrices.")

def calculate_eigenvalues_and_vectors():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Eigenvalues and eigenvectors are only defined for square matrices!")
            return

        # Build the matrix from user input
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        # Convert to a SymPy matrix
        sympy_matrix = sp.Matrix(matrix)

        # Debugging: Print matrix
        print(f"Input Matrix:\n{sympy_matrix}")

        # Calculate eigenvalues and eigenvectors
        eigen_info = sympy_matrix.eigenvects()

        # Debugging: Print raw eigenvalue and eigenvector data
        print("\nEigenvalue and Eigenvector Details:")
        for eigenvalue, multiplicity, eigenvectors in eigen_info:
            print(f"Eigenvalue: {eigenvalue}, Multiplicity: {multiplicity}")
            print(f"Eigenvectors: {eigenvectors}")

        # Display results in GUI
        clear_result_frame()
        tk.Label(result_frame, text="Eigenvalues and Eigenvectors:", font=("Arial", 16, "bold")).pack(pady=10)

        for eigenvalue, multiplicity, eigenvectors in eigen_info:
            # Display the eigenvalue
            pretty_value = sp.pretty(eigenvalue, use_unicode=True)
            tk.Label(result_frame, text=f"Eigenvalue: {pretty_value}", font=("Arial", 16, "bold"), fg="#1abc9c").pack(pady=5)

            # Display each eigenvector
            tk.Label(result_frame, text=f"Eigenvectors (Multiplicity: {multiplicity}):", font=("Arial", 14, "bold")).pack(pady=5)
            for vector in eigenvectors:
                formatted_vector = sp.pretty(vector, use_unicode=True)
                tk.Label(result_frame, text=formatted_vector, font=("Courier", 14), bg="#1abc9c").pack(pady=2)

            # Separator for clarity
            tk.Label(result_frame, text="-" * 50, font=("Arial", 12), fg="#7f8c8d").pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to calculate A^n directly
def calculate_matrix_power_direct():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Matrix power is only defined for square matrices!")
            return

        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(parse_input(value))
            matrix.append(row)

        n = int(power_entry.get())
        if n < 0:
            messagebox.showerror("Error", "Only non-negative powers are supported!")
            return

        sympy_matrix = sp.Matrix(matrix)
        result_matrix = sympy_matrix**n

        clear_result_frame()
        tk.Label(result_frame, text=f"A^{n}:", font=("Arial", 16, "bold")).pack()
        for i in range(result_matrix.rows):
            row_text = "   ".join(map(str, result_matrix.row(i)))
            tk.Label(result_frame, text=row_text, font=("Arial", 16)).pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to create input field for A^n (direct)
def create_power_input_direct():
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())

        if rows != cols:
            messagebox.showerror("Error", "Matrix power is only defined for square matrices!")
            return

        global entries, power_entry
        entries = []

        tk.Label(matrix_frame, text="Input Matrix", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").grid(row=0, column=0, columnspan=cols)

        # Create input fields for matrix
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)

        # Input field for power n
        tk.Label(matrix_frame, text="Power (n):", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").grid(row=rows + 1, column=0, padx=10, pady=10)
        power_entry = tk.Entry(matrix_frame, width=8, font=("Arial", 16), justify="center")
        power_entry.grid(row=rows + 1, column=1, padx=10, pady=10)

        # Button to calculate A^n
        calculate_button = tk.Button(matrix_frame, text="Calculate A^n", command=calculate_matrix_power_direct, font=("Arial", 16), bg="#16a085", fg="red")
        calculate_button.grid(row=rows + 1, column=2, padx=10, pady=10)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for rows and columns.")


# Main window
root = tk.Tk()
root.title("Matrix Operations with Sympy")
root.geometry("900x700")
root.configure(bg="#2c3e50")

top_frame = tk.Frame(root, bg="#1abc9c", height=80)
top_frame.pack(fill="x")

welcome_label = tk.Label(
    top_frame,
    text="Welcome to Sympy Matrix Calculator!",
    bg="#1abc9c",
    fg="black",
    font=("Arial", 24, "bold"),
)
welcome_label.pack(pady=10)

# Frame for operation buttons on the left
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(side="left", fill="y", padx=10, pady=10)

tk.Button(button_frame, text="Determinant", command=calculate_determinant, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="RREF", command=calculate_rref, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="Inverse", command=calculate_inverse, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="Transpose", command=calculate_transpose, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="Eigenvalues", command=calculate_eigenvalues, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="Diagonalize", command=diagonalize_matrix, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="A^n (from P, D)", command=create_power_matrix_inputs, font=("Arial", 16), width=15).pack(pady=10)
tk.Button(button_frame, text="Calculate A^n", command=calculate_power_of_a, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="Eigenvalues & Vectors", command=calculate_eigenvalues_and_vectors, font=("Arial", 16), width=15).pack(pady=10)

tk.Button(button_frame, text="A^n (Direct)", command=create_power_input_direct, font=("Arial", 16), width=15).pack(pady=10)

# Frame for matrix size inputs
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

# Frame for results
result_frame = tk.Frame(root, bg="#34495e")
result_frame.pack(pady=20)

root.mainloop()
