import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm 

from objectivefunction import ObjectiveFunction
from populationinitialization import InitializePopulation, InitializeLGPPopulation
from crossovermutation import CrossoverMutation
from decodechromosome import DecodeChromosome
from geneticmutation import GeneticMutation
from selection import Selection
    
class GeneticAlgorithm(ObjectiveFunction):

    def __init__(self, ga_type='function_optimization', encoding='binary', selector='tournament', 
                 mutation_probability=0.025, crossover_probability=0.75, 
                 number_of_variables=2, f_coeff=1, decoding_scheme='ranged',
                 population_size=100, number_of_genes=50, tournament_size=2,
                 variable_range=3.0, n_copies=1, number_of_generations=1000,
                 tournament_selection_parameter=0.75, variables_registers=4,
                 constant_registers=4, operators=4, lgp_genes=[4,24]):
        
        self.best_fitness = 0
        self.best_index = 0
        self.best_x = np.zeros([1,number_of_variables])
        self.population_fitness = np.zeros(population_size)        
        self.encoding = encoding
        self.selector = selector
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.population_size = population_size
        self.number_of_genes = number_of_genes
        self.number_of_variables = number_of_variables
        self.fractional_coefficient = f_coeff
        self.decoding_scheme = decoding_scheme
        self.tournament_selection_parameter = tournament_selection_parameter
        self.tournament_size = tournament_size
        self.variable_range = variable_range
        self.n_copies = n_copies
        self.number_of_generations = number_of_generations
        self.ga_type = ga_type
        self.variable_registers = variables_registers
        self.constant_registers = constant_registers
        self.operators = operators
        self.lgp_genes = lgp_genes
        
        obj = ObjectiveFunction()
        self.objective = obj.objective
        self.population = np.zeros([population_size, number_of_genes])
                
    def animate(self):
        pass
    
    def InitializePopulation(self):
        
        if self.ga_type == 'function_optimization': 
            population = InitializePopulation(self.encoding, 
                                              self.population_size, 
                                              self.number_of_genes)
        
        if self.ga_type == 'linear_genetic_programming':
            population = InitializeLGPPopulation(self.population_size,
                                                 self.variables_registers,
                                                 self.constants_registers,
                                                 self.operators,
                                                 self.lgp_genes)
        
        self.population = population
        
        return self.population
        
    def EvaluatePopulation(self):
            
        x = np.zeros([self.population_size,self.number_of_variables])
        pop_size = self.population_size
        
        for i in range(pop_size):
            x[i,:] = DecodeChromosome(chromosome=self.population[i,:], 
                                      scheme=self.decoding_scheme,
                                      variable_range=self.variable_range,
                                      n_variables=self.number_of_variables,
                                      )
            
            self.population_fitness[i] = self.Evaluate(x[i,:])
            
            if self.population_fitness[i] > self.best_fitness:
                self.best_fitness = np.copy(self.population_fitness[i])
                self.best_x = x[i,:]
                self.best_index = i
                
    def EvolvePopulation(self):
        
        for g in tqdm(range(self.number_of_generations), desc='Generation'):
        
            self.best_fitness = 0
            self.best_index = 0
            self.best_x = np.zeros([1,self.number_of_variables])
            self.EvaluatePopulation()
            
            temp_population = np.copy(self.population)
            
            
            for itVar in range(0,self.population_size,2):
                i1 = Selection(self.population_fitness)
                i2 = Selection(self.population_fitness)
 
                chromosome1 = temp_population[i1, :]
                chromosome2 = temp_population[i2, :]
                
                r = np.random.rand()
                if r < self.crossover_probability:
                    crossed1, crossed2 = CrossoverMutation(chromosome1, 
                                                           chromosome2,
                                                           gene_length=1)

                    temp_population[itVar,:] = crossed1
                    temp_population[itVar+1,:] = crossed2
                else:
                    temp_population[itVar,:] = chromosome1
                    temp_population[itVar+1,:] = chromosome2
                    
            for itVar in range(self.population_size):
                original_chromosome = temp_population[itVar,:]
                mutated_chromosome = GeneticMutation(original_chromosome)
                temp_population[itVar, :] = mutated_chromosome
                
            best_individual = self.population[self.best_index, :]
            temp_population[0,:] = np.copy(best_individual)
            self.population = np.copy(temp_population)
        