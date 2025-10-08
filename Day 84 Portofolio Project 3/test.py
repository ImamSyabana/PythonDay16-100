
game_board = [
    [[None],[None],[None]],
    [[None],[None],[None]],
    [[None],[None],[None]]
]

# (This variable is not used yet, but will be for checking wins)
winning_condition = [
    []
]

# CHANGED: This dictionary now maps coordinates to (row, column) indices
# This is the key to solving the problem.
coordinate_map = {
    'A1' : (0, 0), 'B1' : (0, 1), 'C1' : (0, 2),
    'A2' : (1, 0), 'B2' : (1, 1), 'C2' : (1, 2),
    'A3' : (2, 0), 'B3' : (2, 1), 'C3' : (2, 2)
}

player_1_info = {
    "name" : "Player #1",
    "move_symbol" : False  # Represents X
}

player_2_info = {
    "name" : "Player #2",
    "move_symbol" : True   # Represents O
}

player_list = [player_1_info, player_2_info]

while True:
    # --- This entire printing block is correct and needs no changes ---
    print(f"\n {'======' * 8}")
    # We use game_board here instead of empty_list for clarity
    for i, row in enumerate(game_board):
        # Print row numbers 1, 2, 3
        print((i + 1), end = "")
        for val in row:
            print("\t O" if val == [True] else "\t X" if val == [False] else "\t  ", end='\t |')
        print(f"\n {'======' * 8}")
    
    print("\t A\t\t B\t\t C")

    # This loop logic is also mostly correct
    for turn in player_list:
        # A simple input validation loop can be added here later
        player_input = input(f"{turn['name']} please choose a grid to fill with a {'X' if turn['move_symbol'] == False else 'O'}! (e.g. B2): ")
        player_input = player_input.upper().replace(" ", "")
        
        
        # 1. Get the (row, col) tuple from our new map
        if player_input in coordinate_map:
            row, col = coordinate_map[player_input]
            
            # 2. Update the original game_board list directly at that position
            game_board[row][col] = [turn["move_symbol"]]
        else:
            print("Invalid input! Please choose a valid coordinate like A1, B2, etc.")
            # We would need to add more logic here to re-prompt the same player
