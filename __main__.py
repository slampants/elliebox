import light_game

if __name__ == "__main__":
    lg = light_game.light_game()
    while True:
        try:
            # Check all pins to see if there's a button being pressed
            # If button is pressed, set lg.light accordingly
            
            lg.check_win_condition()