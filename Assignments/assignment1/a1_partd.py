#    Main Author(s): 
#    Main Reviewer(s):

from a1_partc import Queue
def print_grid(grid, title="Grid"):
	"""Helper function to print the grid in a readable format."""
	print(f"\n{title}:")
	for row in grid:
		print(" ".join(f"{x:3}" for x in row))
	print()  # Blank line for spacing


def get_overflow_list(grid):
	"""Returns the list of overflowing cells based on their value and number of neighbors."""
	rows = len(grid)
	cols = len(grid[0]) if grid else 0
	overflow_list = []

	for r in range(rows):
		for c in range(cols):
			# Determine the number of neighbors
			neighbors = 4  # Default is 4 for inner cells
			if r == 0 or r == rows - 1:
				neighbors -= 1  # Top or bottom row (edge)
			if c == 0 or c == cols - 1:
				neighbors -= 1  # Left or right column (edge)

			# Check if the cell is overflowing
			if abs(grid[r][c]) >= neighbors:
				overflow_list.append((r, c))

	return overflow_list if overflow_list else None


def check_same_sign(grid):
	"""Checks if all non-zero cells have the same sign."""
	has_positive = False
	has_negative = False

	for r in range(len(grid)):
		for c in range(len(grid[0])):
			value = grid[r][c]
			if value > 0:
				has_positive = True
			elif value < 0:
				has_negative = True

			if has_positive and has_negative:
				return False

	return True


def process_overflow(grid):
	"""Processes the grid by setting overflowing cells to 0 and adding 1 to neighbors."""
	overflow_cells = get_overflow_list(grid)

	if not overflow_cells:
		return grid  # No overflow, return the original grid

	print_grid(grid, title="Before Overflow")

	# Create a copy of the grid to update
	next_grid = [row[:] for row in grid]

	for r, c in overflow_cells:
		value = grid[r][c]
		sign = 1 if value > 0 else -1  # Determine the sign of the overflowing cell
		next_grid[r][c] = 0  # Overflowing cell becomes empty

		# Update neighbors
		if r > 0:  # Top neighbor
			next_grid[r - 1][c] += 1 * sign
		if r < len(grid) - 1:  # Bottom neighbor
			next_grid[r + 1][c] += 1 * sign
		if c > 0:  # Left neighbor
			next_grid[r][c - 1] += 1 * sign
		if c < len(grid[0]) - 1:  # Right neighbor
			next_grid[r][c + 1] += 1 * sign

	print_grid(next_grid, title="After Overflow")
	return next_grid


def is_overflowing(grid):
	"""Checks if the grid is overflowing based on the existence of overflow cells and mixed signs."""
	overflow_cells = get_overflow_list(grid)

	if not overflow_cells:
		return False  # No overflowing cells

	if check_same_sign(grid):
		return False  # If all non-zero values have the same sign, no overflow

	return True


def overflow(grid, a_queue):
	"""Recursive function to process the grid overflow and return the number of grids added to the queue."""
	print_grid(grid, title="Initial Grid")

	if not is_overflowing(grid):
		print("Grid is not overflowing. Stopping recursion.")
		return 0  # No grids are added if there's no overflow

	# Process the overflow for the current grid
	next_grid = process_overflow(grid)
	a_queue.enqueue(next_grid)  # Add the processed grid to the queue

	print_grid(next_grid, title="Enqueued Grid")

	# Recursive call with the next grid
	grids_added = 1 + overflow(next_grid, a_queue)  # Count the grid just added

	return grids_added  # Return the total count of grids added to the queue
