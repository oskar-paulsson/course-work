import numpy as np

class MutationOperator:
    def __init__(self):
        pass

    def SwapMutation(self, chromosome, mutation_probability):
        n_genes = len(chromosome)
        mutatedChromosome = np.copy(chromosome)

        for i in range(n_genes):
            r = np.random.rand()
            if r < mutation_probability:
                mutation_incomplete = True
                while mutation_incomplete:
                    index1 = i
                    index2 = np.random.randint(n_genes)
                    if index1 != index2:
                        swapAllele1 = chromosome[index1]
                        swapAllele2 = chromosome[index2]
                        mutatedChromosome[index2] = swapAllele1
                        mutatedChromosome[index1] = swapAllele2
                        chromosome = np.copy(mutatedChromosome)
                        mutation_incomplete = False

        return chromosome

    def FlipMutation(self, chromosome, mutation_probability):

        n_genes = len(chromosome)
        random_vector = np.random.rand(n_genes)
        chromosome[random_vector < mutation_probability] = 1 - chromosome[random_vector < mutation_probability]

        return chromosome

    def LGPMutation(self, population, variables, constants, mutation_probability):
        n = variables
        m = constants

        population_size = len(population)

        lim = np.array([4, n, m, m+n])

        for i in range(population_size):
            chromosome = population[i]['chromosome']
            for j in range(0,len(chromosome),4):
                instructions = chromosome[j:j+3]
                for k in range(0,len(instructions)):
                    if np.random.rand() < mutation_probability:
                        instructions[k] = np.random.randint(lim[k]+1)
                chromosome[j:j+3] = np.copy(instructions)
            population[i]['chromosome'] = np.copy(chromosome)

        return population

def GeneticMutation(chromosome, mutation_probability=0.75, type='flip'):
    """
    Genetic mutation is performed on each gene, each gene has a probability =< 1 of
    mutating. In the case of flip mutation, a binary gene is changes value.
    In the case of swap mutation, two genes will simply swap places.

    If you're using a GA for LGP, always use LGPMutation.

    Swap mutation works for binary genes and real valued encoding.
    Swap mutation is especially recommended when solving TSP as crossover
    can cause congruency problems

        # Arguments:
            chromosome: is a list of elements, binary or real valued
            mutation_probability : the probability that a single gene (an element of the list
            chromosome)

        # returns:
            chromosome
    """
    operator = MutationOperator()

    if type.lower() == 'flip':
        chromosome = operator.FlipMutation(np.copy(chromosome), mutation_probability)

    if type.lower() == 'swap':
        chromosome = operator.SwapMutation(np.copy(chromosome), mutation_probability)

    return chromosome

def GeneticLPMutation(population, n_variables, n_constants, mutation_probability):

    operator = MutationOperator()

    mutated_population = operator.LGPMutation(np.copy(population), n_variables,
                    n_constants, mutation_probability)

    return mutated_population
