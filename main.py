from modules.game_module import Game  # ← ggf. Dateiname anpassen

def main():
    user_input = None
    while user_input not in ["1", "2"]:
        from turtle import Screen
        screen = Screen()
        user_input = screen.textinput("Players", "Single Player or Two Players? Type 1 or 2")
        if user_input == "exit":
            screen.bye()

    players = int(user_input)
    game = Game(players)
    game.game_loop()

if __name__ == "__main__":
    main()
