import pcbnew
from pcbnew import ToMM, FromMM

# Load the current PCB board
board = pcbnew.GetBoard()

# Create a dictionary to store the positions of switches by their value
switch_positions = {}

# Iterate over all footprints to find all switches (SW[number]) and store their positions by value
for footprint in board.GetFootprints():
    ref = footprint.GetReference()
    if ref.startswith("SW"):
        value = footprint.GetValue()
        switch_positions[value] = footprint.GetPosition()

# Iterate over all footprints to find all LEDs (U[number])
for footprint in board.GetFootprints():
    ref = footprint.GetReference()
    if ref.startswith("U"):
        value = footprint.GetValue()
        if value in switch_positions:
            # Get the position of the corresponding switch
            switch_position = switch_positions[value]
            
            # Calculate the new position 5.05 mm below the switch
            new_x = switch_position.x
            new_y = switch_position.y + FromMM(5.05)  # -5.05mm downward
            
            # Set the new position for the LED
            footprint.SetPosition(pcbnew.VECTOR2I(new_x, new_y))
            print(f"Moved {ref} (Value: {value}) to position 5.05 mm below the corresponding switch.")

# Refresh the PCB view
pcbnew.Refresh()
