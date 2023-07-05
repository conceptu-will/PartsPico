import numpy as np

# Numpy is a 3rd party library for numerical work in Python.
# To install (from a command line): pip install numpy

# Within Thonny, use Tools>>Manage packages


# print(population)

def fitness(individual):
    return sum(individual)


def selection(population, fitness_scores, k=3):
    selection_index = np.random.randint(len(population))
    # Choose a random 'k' number of individuals, and select the most fit.
    # 'Tournament' selection
    for index in np.random.randint(0, len(population), k-1):
        if fitness_scores[index] > fitness_scores[selection_index]:
            selection_index = index

    return population[selection_index]


def shouldRecombine(crossover_rate):
    return np.random.rand() < crossover_rate


def shouldMutate(mutation_rate):
    return np.random.rand() < mutation_rate


def reproduction(parent_a, parent_b, crossover_rate):
    child_a = parent_a.copy()
    child_b = parent_b.copy()
    
    # reproduction is not guaranteed.  
    if (shouldRecombine(crossover_rate)):
        crossover_index = np.random.randint(1, len(parent_a) - 2)
        child_a = parent_a[:crossover_index] + parent_b[crossover_index:]
        child_b = parent_b[:crossover_index] + parent_a[crossover_index:]
        
    return [child_a, child_b]


def mutation(individual, mutation_rate):
    for index in range(len(individual)):
        if (shouldMutate(mutation_rate)):
            individual[index] = 1 - individual[index]
        

def run(individual_size, population_size, number_of_iterations, crossover_rate, mutation_rate):
    population = [np.random.randint(0, 2, individual_size).tolist() for _ in range(population_size)]
    # Initialize the 'best'.
    best = 0
    best_fitness = fitness(population[0])
    
    for generation_index in range(number_of_iterations):
        print('Processing generaton {0}'.format(generation_index))
        print('Best individual is {0} with a fitness score of: {1}'.format(best, best_fitness))

        fitness_scores = [fitness(currentIndividual) for currentIndividual in population]
        
        print('Average fitness: {0}'.format(sum(fitness_scores) / len(fitness_scores)))
        
        for index in range(population_size):
            if fitness_scores[index] > best_fitness:
                best = population[index]
                best_fitness = fitness_scores[index]

        parents = [selection(population, fitness_scores) for _ in range(population_size)]

        children = list()
        for index in range(0, population_size, 2):
            parent_a = parents[index]
            parent_b = parents[index + 1]
            for child in reproduction(parent_a, parent_b, crossover_rate):
                mutation(child, mutation_rate)
                children.append(child)
                
        population = children
        
        print('')

    return best, best_fitness

#for currentIndividual in population:
#    print(currentIndividual)
#    print(fitness(currentIndividual))

run(15, 20, 20, 0.9, 0.1)
