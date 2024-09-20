import board
import time
import random

def Choose_Pairs(chrom_list, percentage_list):
    return random.choices(chrom_list, percentage_list, k = len(chrom_list))

"""
returns the mutation from the board at the crosspoint

param str str1: the first mutaiton string
param str str2: the second mutation string
param int queens: the max number that the chrom can be. The crosspoint is randomly selected
return: returns two strings that have been mutated together at the crosspoint
"""
def cross(str1, str2, queens):
    crosspoint = random.randrange(1,queens - 1)
    return str1[:crosspoint] + str2[crosspoint:], str2[:crosspoint] + str1[crosspoint:]

def mutation(chrom,queens):
    #print(chrom)
    chrom_len = len(chrom)
    #the position of the mutaion can be to at most queens - 1
    position = random.randint(0, queens - 1)
    chrom_change = str(random.randint(0, chrom_len))
    #print(position, chrom_change)
    return chrom[:position] + chrom_change + chrom[position + 1:]
    #return chrom[:position] + str(chrom_change) + chrom[position + 1:-1]


def main():
    queens = 4
    chroms = 4
    #MAX_FIT = queens * (queens - 1) / 2
    boards_list =[]
    chrom_list = []
    fitness_list = []
    total_fitness = 0
    MAX_FIT = queens * (queens - 1) / 2

    b1 = board.Board(5)
    print(b1.encode())
    b1.decode('11111')
    b1.print_map()


    #could change out fitness list for percentage list. Might need for later


    #creates three lists that are all corolated.
    #1. the entire board
    #2. the encoded board list (or the queens representaiton on the board)
    #3. the fitness list that contains all fitness levels for all boards
    for i in range(chroms):
        temp_board = board.Board(queens)
        boards_list.append(temp_board)
        chrom_list.append(temp_board.encode())
        fitness_list.append(temp_board.get_fitness())

    
    #while (total_fitness not in fitness_list):
    k = 0
    while(k < 3):
        print("Generation at ", k)
        percentage_list = []
        total_fitness = 0
        #update percentage list, fitness list, total fitness
        for index in range(chroms):
            fitness_list[index] = boards_list[index].get_fitness()
            total_fitness += fitness_list[index]
        for index in range(chroms):
            percentage_list.append(fitness_list[index] / total_fitness)


        print("Chrom List: ", chrom_list)
        print("fitness_list: ", fitness_list)
        print("Max Fit: ", MAX_FIT)
        print("total fit" , total_fitness)
        print("Percentage_list: ", percentage_list)
        print("pair selection")
        
        #create pairs
        pair = Choose_Pairs(chrom_list, percentage_list)
        print(pair)
        for i in range(0,len(pair),2):
            pair[i], pair[i + 1] = cross(pair[i], pair[i + 1], queens)
        print(pair)
        for index in range(len(pair)):
            if random.random() < .5:
                pair[index] = mutation(pair[index], queens)
        chrom_list = pair
        print(chrom_list)
        k += 1
    print("found max fitness at generation, ", k)
    for index in range(chroms):
        s = chrom_list[index]
        boards_list[index].decode(s)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    total = (end - start) * 1000
    print(f'{total:.20f} ms')