import board

def main():
    queens = 4

    b = board.Board(queens)

    b.print_map()


if __name__ == "__main__":
    main()