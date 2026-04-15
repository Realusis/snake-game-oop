from game import Game


def main():
    game = Game()
    name = input("Enter your name: ")
    game.set_player_name(name)
    game.run()

if __name__ == "__main__":
    main()