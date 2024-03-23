import nbformat

# Create a new Jupyter Notebook
nb = nbformat.v4.new_notebook()

# Loop through numbers 1 to 50 and add code cells with comments
for i in range(1, 51):
    # Create a code cell
    cell = nbformat.v4.new_code_cell(source=f'# Cell {i}\n')
    # Add the code cell to the notebook
    nb.cells.append(cell)

# Save the notebook to a file
file_path = "numbered_cells.ipynb"
with open(file_path, "w") as f:
    nbformat.write(nb, f)

print(f"Jupyter Notebook with numbered cells saved to '{file_path}'")
