# Dimensions of each block
block_width = 70
block_height = 70

# Starting position of the first block
start_x = 40
start_y = 40

# List to hold the positions of each block
positions = {}

# Letters representing columns
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Loop through rows and columns to generate positions
for row in range(8):
    for col in range(8):
        # Calculate the position of the current block
        x = start_x + col * block_width
        y = start_y + row * block_height
        
        # Generate chess notation for the current position
        notation = letters[col] + str(8 - row)
        
        # Add the position to the dictionary with chess notation as the key
        positions[notation] = [x, y]

# Now positions dictionary contains keys as chess notation and values as position variables

print(positions)