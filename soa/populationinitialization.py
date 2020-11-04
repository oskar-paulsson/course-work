import numpy as np

class InitializationOperator:
    def __init__(self):
        pass

    def BinaryEncoding(self, n_individuals, chromosome_length):

        pop = np.random.rand(n_individuals, chromosome_length)
        pop[pop < 0.5] = 0
        pop[pop >= 0.5] = 1
        population = np.copy(pop.astype('int'))

        return population

    def RealValueEncoding(self, n_individuals, chromosome_length):

        pop = np.random.rand(n_individuals, chromosome_length)
        population = np.copy(pop.astype('int'))

        return population

    def LinearProgramming(self, n_individuals, n_variables, n_constants, n_operators, n_genes):

        population = [0]*n_individuals
        for i in range(n_individuals):
            population[i] = {'chromosome' : []}

            for j in range(np.random.randint(n_genes[0],n_genes[1])+1):
                N = np.random.randint(n_variables)
                O = np.random.randint(n_operators)
                X1 = np.random.randint(n_variables + n_constants)
                X2 = np.random.randint(n_variables + n_constants)

                population[i] = {'chromosome' : np.append(population[i]['chromosome'], [N, O, X1, X2])}

        return population

def InitializePopulation(scheme, n_individuals, chromosome_length):
"""
Initialize population for a genetic algorithm.
    # Arguments:
        scheme: string, binary or realvalue - denotes the type of encoding to be
                used when creating the population

        n_individuals: positive, non-zero integer, how many individuals should be in the
                        population, equivalent to population_size

        chromosome_length: positive, non-zero integer, how many genes should each
                            individual be made up of

    # returns:
        population: a (n_individuals,chromosome_length)-sized numpy.array
"""
    operator = InitializationOperator()

    if scheme.lower() == 'binary':
        population = opeartor.BinaryEncoding(n_individuals, chromosome_length)

    if scheme.lower() == 'realvalue':
        population = operator.RealValueEncoding(n_individuals, chromosome_length)

    return population

def InitializeLGPPopulation(n_individuals, n_variables, n_constants, n_operators=4, n_genes=[4,24]):
"""
Initialize a population for Linear Genetic Programming (LGP).
    # Arguments:
        n_individuals: positive, non-zero integer, how many individuals should be in the
                        population, equivalent to population_size
        n_variables: positive, non-zero integer, number of variable registers
        n_constants: positive, non-zero integer, number of constant registers
        n_operators: positive, non-zero integer, number of operators,
                    4 by default : [addition, subtraction, multiplication, division]
        n_genes: set of two positive, non-zero integers with n_genes[0]<n_genes[1].
                denotes min/max length of individuals, i.e. the number of genes
                in each individual, here a gene=a set of instructions are:
                [destination register, operator, operand1, operand2].
                destination registers are always variables, operand1 and operand2
                can be either variable registers or constant registers

    # returns:
        population : a list of dictionaries, each with a single field called
        "chromosome", the field contains a list of integers and every set of 4
        integers is a set of instructions or a gene.
"""
    operator = InitializationOperator()

    population = operator.LinearProgramming(n_individuals, n_variables, n_constants,
                                            n_operators, n_genes)

    return population
