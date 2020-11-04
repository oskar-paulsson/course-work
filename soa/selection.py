import numpy as np

class SelectionOperator:
    def __init__(self):
        pass

    def Tournament(self, population_fitness, tournament_size, selection_probability):
        population_size = len(population_fitness)

        i_temp = np.random.randint(0,population_size,tournament_size)
        tournament_selection = population_fitness[i_temp]

        tournament_over = False

        while not tournament_over:
            r = np.random.rand()
            if r < selection_probability:
                max_fitness_index = np.where(tournament_selection == max(tournament_selection))
                i_selected = i_temp[max_fitness_index]
                tournament_over = True
            else:
                i_remove = np.where(tournament_selection == max(tournament_selection))
                tourment_selection[i_remove] = []

        return i_selected

    def RouletteWheel(self, population_fitness):

        phi = np.cumsum(population_fitness) / np.sum(population_fitness)
        r = np.random.rand()
        slice = np.copy(phi[phi > r])
        i_selected = np.where(phi==slice[0])

        return i_selected


def Selection(population_fitness, selection_probability=0.8, tournament_size=2, type='tournament'):
    """
    The selection-operator class has two methods:
    RouletteWheel and Tournament, which can carry out selection.
    Simply pass the fitness of all individuals in your population to the selection method
    and it will, by default carry out tournament selection with a tournament size 2
    and tournament selection parameter 0.8.

    The method (Selection) SHOULD NOT be given the entire population but simply the array
    containing the fitness of each individual. Correspondingly, the method will
    return the INDEX of the winning individual, not the individual itself.

        # Arguments:
            population_fitness: a list containing the fitness of every individual in the
            current population
            selection_probability: a float/ratio < 1 which is used for the TOURNAMENT selection
            tournament_size: integer, the size (number of individuals) to take part in tournament
            type: TOURNAMENT or ROULETTEWHEEL.

        # return:
            winning_index: the INDEX of the winning (i.e. selected) individual
    """
    operator = SelectionOperator()

    if type.lower() == 'tournament':
        winning_index = operator.Tournament(population_fitness,
                            tournament_size, selection_probability)

    if type.lower() == 'roulettewheel':
        winning_index = operator.RouletteWheel(population_fitness)

    return winning_index
