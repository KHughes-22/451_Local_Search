import board


def Search_Space(b:board):
    b.print_map()

def Find_Highest(b:board):
    print("height")

def main():
    queens = 4

    b = board.Board(queens)

    b_fit = b.encode()
    print(b_fit)
    Search_Space(b)


if __name__ == "__main__":
    main()