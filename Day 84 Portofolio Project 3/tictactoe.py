game_board = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]

winning_condition = [
    []
]

coordinate_list = {
    'A1' : (0,0), 'A2' : (1,0), 'A3' : (2,0),
    'B1' : (0,1), 'B2' : (1,1), 'B3' : (2,1),
    'C1' : (0,2), 'C2' : (1,2), 'C3' : (2,2)
}

player_1_info = {
    "name" : "Player #1",
    "move_symbol" : False
}

player_2_info = {
    "name" : "Player #2",
    "move_symbol" : True
}

player_list = [player_1_info, player_2_info]
grid_filled_list = []
#print(player_list[0]["move_symbol"])

def tictactoe_board():
    print(f"\n {'======' * 8}")
    for x in range(len(game_board )):
        print((x + 1), end = "")
        for val in game_board[x]:
            
            print("\t O" if val == True else "\t X" if val == False else "\t  ", end='\t |')
            #print("\t  ", end='\t |')
        print(f"\n {'======' * 8}")

    print("\t A\t\t B\t\t C")

def check_for_win():
    # Check all 3 rows
    for row in range(3):
        # We check if the three values in a row are the same AND not empty (None)
        if game_board[row][0] == game_board[row][1] == game_board[row][2] and game_board[row][0] is not None:
            return True # A win is found!

    # Check all 3 columns
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] and game_board[0][col] is not None:
            return True # A win is found!

    # Check the two diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] is not None:
        return True # A win is found!
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] is not None:
        return True # A win is found!

    return False # No winner was found

game_is_over = False

while not game_is_over: # buat terminate kalo win lose atau draw
    for turn in player_list:
        while True:
            print(grid_filled_list)
            tictactoe_board()
            player_input = input(f"{turn["name"]} please choose a grid to fill with a {'X' if turn["move_symbol"] == False else 'O'}! (e.g. B2): ")
            player_input = player_input.upper().replace(" ", "")

            

            
            if player_input in grid_filled_list:
                print("That grid has already filled. Find an empty grid!")
                continue

            elif player_input in coordinate_list:
                row, col = coordinate_list[player_input]
            
                game_board[row][col] = turn["move_symbol"]

                grid_filled_list.append(player_input)
                break
            else:
                print("Invalid input! Please choose a valid coordinate like A1, B2, etc.")
                # We would need to add more logic here to re-prompt the same player
                continue

        # CHECK FOR GAME END CRITERIA
        if check_for_win():
            tictactoe_board() # Display the final board
            print(f"🎉 Congratulations {turn['name']}, you won! 🎉")
            game_is_over = True # Set the flag to True to stop the 'while' loop
            break # This exits the 'for turn in player_list' loop immediately

        # If there's no winner, THEN check for a draw
        elif len(grid_filled_list) == 9:
            tictactoe_board()
            print("🤝 It's a draw! 🤝")
            game_is_over = True
            break

