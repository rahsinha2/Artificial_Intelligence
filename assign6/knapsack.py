'''
This file contains support code for B551 Hw6                                 # File version:  November 19, 2015                                            #

For questions related to genetic algorithms or the knapsack problem, any AI can be of help. For questions related to the support code itself, contact Alex at aseewald@indiana.edu.
'''
import math
import random
import pickle
import numpy as np
import pandas as pd
from scipy.stats import norm
from numpy.random import choice
from copy import deepcopy

def randomSelection(population,fitnesses):
    '''
    This should return a single chromosome from the population. The selection process should be random, but with weighted probabilities proportional
    to the corresponding 'fitnesses' values.
    *********Using Group Selection*************
    '''
    size = len(population)
    elements = [1, 2, 3, 4] 
    weights = [0.50, 0.30, 0.15, 0.05]
    array_partition = choice(elements, p=weights)
    
    if array_partition == 1:
	lower = 0
	upper = (size/4)-1;
    elif array_partition == 2:
	lower = (size/4)
	upper = (size/2)-1
    elif array_partition == 3:
	lower = (size/2)
	upper = ((3*size)/4)-1
    elif array_partition == 4:
	lower = ((3*size)/4)
	upper = size-1
    
    index = random.randint(lower,upper)
    indexes = np.argsort(fitnesses)[::-1]
    return population[indexes[index]]
    

def reproduce(mom,dad):
    "This does genetic algorithm crossover. This takes two chromosomes, mom and dad, and returns two chromosomes."
    #child1 = deepcopy(mom)
    #child2 = deepcopy(dad)
    length = len(mom)	
    #print "length", length
    pos = random.randint(0,length-2)
    #print "crossover ", pos
    for i in range(pos+1, length):
    	mom[i] , dad[i] = dad[i], mom[i]
    return mom, dad

def mutate(child, mutation_probability):
    "Takes a child, produces a mutated child."
    #mutated = deepcopy(child)
    length = len(child)
    for i in range(0,length):
        flip_or_not = random.uniform(0, 1)
	if flip_or_not <= mutation_probability:
    	    child[i] = not child[i]
    #print "child   = ",child
    #print "mutated = ",mutated
    return child

def fitness(max_volume,volumes,prices):
    '''
    This should return a scalar which is to be maximized.
    max_volume is the maximum volume that the knapsack can contain.
    volumes is a list containing the volume of each item in the knapsack.
    prices is a list containing the price of each item in the knapsack, which is aligned with 'volumes'.
    '''
    if(sum(volumes) > max_volume):
	return 0
    else: 
    	return sum(prices)

def compute_fitnesses(world,chromosomes):
    '''
    Takes an instance of the knapsack problem and a list of chromosomes and returns the fitness of these chromosomes, according to your 'fitness' function.
    Using this is by no means required, if you want to calculate the fitnesses in your own way, but having a single definition for this is convenient because
    (at least in my solution) it is necessary to calculate fitnesses at two distinct points in the loop (making a function abstraction desirable).

    Note, 'chromosomes' is required to be a 2D numpy array of boolean values (a fixed-size boolean array is the recommended encoding of a chromosome, and there should be multiple of these arrays, hence the matrix).
    '''
    return [fitness(world[0], world[1] * chromosome, world[2] * chromosome) for chromosome in chromosomes]

def init_population(world, popsize):
    return np.random.randint(2, size=(popsize,len(world[1])))

def genetic_algorithm(world,popsize,max_years,mutation_probability):
    '''
    world is a data structure describing the problem to be solved, which has a form like 'easy' or 'medium' as defined in the 'run' function.
    The other arguments to this function are what they sound like.
    genetic_algorithm *must* return a list of (chromosomes,fitnesses) tuples, where chromosomes is the current population of chromosomes, and fitnesses is
    the list of fitnesses of these chromosomes. 
    '''
    result = []
    population = init_population(world,popsize)
    fitnesses = compute_fitnesses(world, population)
    tuple1 = (population, fitnesses)
    result.append(tuple1)
    
    
    for i in range(0,max_years):
	population_new = deepcopy(population)
    	mom = randomSelection(population_new, fitnesses)
    	dad = randomSelection(population_new, fitnesses)
    	#print "mom = ", mom, " dad = ",dad
   	child1, child2 = reproduce(mom,dad)
    	#print "child1 = ", child1, " child2 = ",child2
    	x = mutate(child1, mutation_probability)
    	y = mutate(child2, mutation_probability)
    	fitnesses_new = compute_fitnesses(world, population_new)
	print "New"
	print fitnesses_new    
	tuple1 = (population_new, fitnesses_new)
    	result.append(tuple1)
    	population = population_new 
        fitnesses = fitnesses_new
    return result

def run(popsize,max_years,mutation_probability):
    '''
    The arguments to this function are what they sound like.
    Runs genetic_algorithm on various knapsack problem instances and keeps track of tabular information with this schema:
    DIFFICULTY YEAR HIGH_SCORE AVERAGE_SCORE BEST_PLAN
    '''
    table = pd.DataFrame(columns=["DIFFICULTY", "YEAR", "HIGH_SCORE", "AVERAGE_SCORE", "BEST_PLAN"])
    sanity_check = (10, [10, 5, 8], [100,50,80])
    chromosomes = genetic_algorithm(sanity_check,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'sanity_check', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    easy = (20, [20, 5, 15, 8, 13], [10, 4, 11, 2, 9] )
    chromosomes = genetic_algorithm(easy,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'easy', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    medium = (100, [13, 19, 34, 1, 20, 4, 8, 24, 7, 18, 1, 31, 10, 23, 9, 27, 50, 6, 36, 9, 15],
                   [26, 7, 34, 8, 29, 3, 11, 33, 7, 23, 8, 25, 13, 5, 16, 35, 50, 9, 30, 13, 14])
    chromosomes = genetic_algorithm(medium,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'medium', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    hard = (5000, norm.rvs(50,15,size=100), norm.rvs(200,60,size=100))
    chromosomes = genetic_algorithm(hard,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'hard', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    for difficulty_group in ['sanity_check','easy','medium','hard']:
        group = table[table['DIFFICULTY'] == difficulty_group]
        bestrow = group.ix[group['HIGH_SCORE'].argmax()]
        print("Best year for difficulty {} is {} with high score {} and chromosome {}".format(difficulty_group,int(bestrow['YEAR']), bestrow['HIGH_SCORE'], bestrow['BEST_PLAN']))
    table.to_pickle("results.pkl") #saves the performance data, in case you want to refer to it later. pickled python objects can be loaded back at any later point.
    pass

if __name__ == "__main__":
    run(10,50,0.2)
