import random
import time

def calcProb(m, n):
    # m: number of items in population
    # n: number of samples
    # Return 1 - m!/((m-n)!*m^n)
    
    prod = 1.0

    for i in range(n):
        prod *= float(m - i) / float(m)

    return (1.0 - prod)


def hasDuplicate(m, n):
    used = set()

    for i in range(n):
        temp = random.randint(0, m-1)
        if (not temp in used):
            used.add(temp)
        else:
            return True

    return False    # No duplication


if __name__ == "__main__":
    random.seed(time.time())
    m = 365
    n = int(input("Input number of students:"))
    ite = 1000000

    print ("Probability that at least two students will have the same birthday = %.20f" %(calcProb(m, n)))

    counters = {True: 0, False: 0}

    for i in range(ite):
        counters[hasDuplicate(m, n)] += 1

    print ("After %d rounds of experiments, %d cases have duplicates, while %d have none." %(ite, counters[True], counters[False]))
    print ("Experimented probability = %.20f" %(float(counters[True]) / float(ite)))

