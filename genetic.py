import board
import time
import random

"""
returns the mutation from the board at the crosspoint

param str str1: the first mutaiton string
param str str2: the second mutation string
param int queens: the max number that the chrom can be. The crosspoint is randomly selected
return: returns two strings that have been mutated together at the crosspoint
"""
def cross(str1, str2, queens):
    crosspoint = random.randomrange(1,queens - 1)
    return str1[:crosspoint] + str2[crosspoint:], str2[:crosspoint] + str1[crosspoint:]


def main():
    queens = 5
    chroms = 4
    total_fitness = 0
    boards_list =[]
    chrom_list = []
    fitness_list = []
    #could change out fitness list for percentage list. Might need for later
    percentage_list = []

    #creates three lists that are all corolated.
    #1. the entire board
    #2. the encoded board list (or the queens representaiton on the board)
    #3. the fitness list that contains all fitness levels for all boards
    for i in range(chroms):
        temp_board = board.Board(queens)
        boards_list.append(temp_board)
        chrom_list.append(temp_board.encode())
        fit = temp_board.get_fitness()
        total_fitness += fit
        fitness_list.append(fit)

    for element in fitness_list:
        percentage_list.append(element / total_fitness)


    # print("Chrom List: ", chrom_list)
    # print("fitness_list: ", fitness_list)
    # print("Fitness total: ", total_fitness)
    # print("Percentage_list: ", percentage_list)
    # print("pair selection")
    #print(random.choice(chrom_list, weights=percentage_list))
    pair = []
    print(type(random.choices(chrom_list, weights=percentage_list)))
    while(chrom_list):
        temp = random.choices(chrom_list, weights=percentage_list)
        pair.append(temp)
        chrom_list.remove(temp)
    print(pair)

    



    # for element in boards_list:
    #     element.print_map()
    #     print()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    total = (end - start) * 1000
    print(f'{total:.20f} ms')