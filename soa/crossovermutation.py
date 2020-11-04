import numpy as np

class CrossoverOperator:
    def __init__(self):
        pass

    def SinglePointCrossover(self, chromosome1, chromosome2, gene_length):
        L1 = len(chromosome1)
        gene_length = gene_length
        n1 = L1 / gene_length

        crossover_point = np.random.randint(n1-1)+1
        j = np.copy(crossover_point)

        crossed1 = np.append(chromosome1[:j], chromosome2[-(len(chromosome2)-j):])
        crossed2 = np.append(chromosome1[-(len(chromosome1)-j):], chromosome2[:j])

        return crossed1, crossed2

    def TwoPointCrossover(self, chromosome1, chromosome2, gene_length):

        L1 = len(chromosome1)
        L2 = len(chromosome2)
        gene_length = gene_length

        n1 = L1 / gene_length
        n2 = L2 / gene_length

        cut_start1 = np.random.randint(n1)
        cut_end1 = np.random.randint(cut_start1, n1+1)+1
        cut_start2 = np.random.randint(n2)
        cut_end2 = np.random.randint(cut_start2, n2+1)+1
        print(cut_start1)
        print(cut_end1)
        print(cut_start2)
        print(cut_end2)

        piece1 = chromosome1[cut_start1*gene_length:cut_end1*gene_length]
        piece2 = chromosome2[cut_start2*gene_length:cut_end2*gene_length]
        end1 = chromosome1[-(len(chromosome1)-gene_length*(cut_end1)):]
        end2 = chromosome2[-(len(chromosome2)-gene_length*(cut_end2)):]

        crossed1 = np.append(np.append(chromosome1[0:cut_start1*gene_length], piece2), end1)
        crossed2 = np.append(np.append(chromosome2[0:cut_start2*gene_length], piece1), end2)

        return crossed1, crossed2

def CrossoverMutation(chromosome1, chromosome2, gene_length, two_point=False):
    """
    Crossover occurs between two individuals which have been selected using the
    selection operator. The standard crossover operator is the one-point crossover
    which will conserve the length of the two chromosomes by swapping two segments
    of the chromosomes, thus creating two new individuals.

    Two-point crossover does not necessarily conserve length because the length of the
    segments being swapped will have different lengths, making one of the new individuals
    shorter than the other. Start and end points of the segments are randomly selected
    so that genes are not cut, only complete genes are transferred.

        # Arguments:
            chromosome1, chromosome2: is a list of elements, binary or real valued
            gene_length : integer, critical to know the length of genes, to prevent the destruction
            of genetic material.
            two_point : boolean, tell the operator which type of cross-over should be carried out

        # returns:
            crossed1, crossed2: "offspring" of the "parent"-chromosomes 1 and 2.
    """
# TODO : Make a four-point crossover?

    operator = CrossoverOperator()

    if not two_point:
        crossed1, crossed2 = operator.SinglePointCrossover(chromosome1,
                                                        chromosome2, gene_length)
    else:
        crossed1, crossed2 = operator.TwoPointCrossover(chromosome1,
                                                        chromosome2, gene_length)

    return crossed1, crossed2
