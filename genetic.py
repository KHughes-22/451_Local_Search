import board
import random as rand

def selection():
    print("selection")

def crossover(chrom_one, chrom_two,crosspoint):
    return chrom_one[:crosspoint] + chrom_two[crosspoint:], chrom_two[:crosspoint] + chrom_one[crosspoint:]

def main(queens,chrom):
    board_list = []
    code_list = []
    print(board_list)
    #Create states for the amount of Chromosomes we want
    for b in range(chrom):
        #create boards with the number of queens
        b = board.Board(queens)
        board_list.append(b)
        code_list.append(b.encode())
    print(code_list[0], code_list[1])
    code_list[0], code_list[1] = crossover(code_list[0], code_list[1], 2)
    print(code_list[0], code_list[1])




def test_cases():
    main(4, 4)

if __name__ == "__main__":
    test_cases()