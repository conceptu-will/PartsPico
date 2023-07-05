import numpy as np



class Algorithm:
    def __init__(self, number_of_chromosomes, population_size, crossover_rate, mutation_rate, selection_pool_size):
        self.population = Population(selection_pool_size);
        for _ in range(population_size):
            self.population.add(Individual(number_of_chromosomes, mutation_rate))
        self.generation_number = 0
        self.crossover_rate = crossover_rate

    def get_population(self):
        return self.population
    
    def set_population(self, population):
        self.population = population

    def get_generation_number(self):
        return self.generation_number

    def set_generation_number(self, generation_number):
        self.generation_number = generation_number

    def increment_generation_number(self):
        self.set_generation_number(self.get_generation_number() + 1)

    def get_fittest(self):
        return self.population.get_fittest()
    
    def should_crossover(self):
        return np.random.rand() < self.crossover_rate

    def reproduction(self, parents):
        parent_a = parents[0]
        parent_b = parents[1]
        
        # Default...if no crossover...is to have the child be a copy of the first parent.
        child = parent_a.clone()
        
        # If crossover occurs, the child will be a mix of the two parents.
        if (self.should_crossover()):
            child = parent_a.reproduce_with(parent_b)
            
        return child

    def spawn_next_generation(self):
        self.increment_generation_number()
        
        # Randomly select 'fitter' individuals from the population.
        reproducing_parents = [self.get_population().selection() for _ in range(self.population.size())]

        children = Population(self.get_population().get_selection_pool_size())

        for _ in range(len(reproducing_parents)):
            # Choose two random parents
            reproducing_pair = np.random.choice(reproducing_parents, 2, False)
            child = self.reproduction(reproducing_pair)
            child.mutate()
            children.add(child)

        self.set_population(children)
    
    def run(self, number_of_generations):
        for _ in range(number_of_generations):
            self.spawn_next_generation()
            population = self.get_population()
            print("Generation: {0:0>3}, \t Average fitness: {1:.2f}, \t Fittest: {2:0>3}".format(self.get_generation_number(), population.get_average_fitness(), (population.get_fittest()).get_fitness()))




class Population:
    def __init__(self, selection_pool_size):
        self.individuals = list()
        self.selection_pool_size = selection_pool_size
    
    def get_individuals(self):
        return self.individuals
    
    def set_individuals(self, individuals):
        self.individuals = individuals
    
    def get_selection_pool_size(self):
        return self.selection_pool_size
    
    def add(self, individual):
        self.individuals.append(individual)
    
    def get_individual(self, index):
        return self.individuals[index]
    
    def size(self):
        return len(self.individuals)

    def get_average_fitness(self):
        fitness_scores = [current_individual.get_fitness() for current_individual in self.get_individuals()]
        return sum(fitness_scores) / len(fitness_scores)

    def get_fittest(self):
        current_best = None; # to be replaced with the best individual
        
        for individual in self.get_individuals():
            if ((current_best is None) or individual.get_fitness() > current_best.get_fitness()):
                current_best = individual

        return current_best

    def selection(self):
        # Choose 'k' number of random individuals, without duplication.
        random_individuals = np.random.choice(self.individuals, self.get_selection_pool_size(), False)
        
        # Find the fittest of this subset.
        fittest_individual = None
        for current_individual in random_individuals:
            if (
                (fittest_individual is None)
                or (current_individual.get_fitness() > fittest_individual.get_fitness())
            ):
                fittest_individual = current_individual

        return fittest_individual




class Individual:
    def __init__(self, number_of_chromosomes, mutation_rate):
        self.chromosomes = np.random.randint(0, 2, number_of_chromosomes).tolist()
        self.mutation_rate = mutation_rate
        self.fitness = 0

    def get_chromosomes(self):
        return self.chromosomes

    def set_chromosomes(self, chromosomes):
        self.chromosomes = chromosomes

    def get_mutation_rate(self):
        return self.mutation_rate

    def get_fitness(self):
        if (self.fitness == 0):
            self.calculate_fitness()
        return self.fitness
    
    def calculate_fitness(self):
        self.fitness = sum(self.chromosomes)
    
    def clone(self):
        cloned_individual = Individual(len(self.chromosomes), self.get_mutation_rate())
        cloned_individual.set_chromosomes(self.get_chromosomes())
        return cloned_individual
    
    def should_mutate(self):
        return np.random.rand() < self.mutation_rate

    def mutate(self):
        for index in range(len(self.chromosomes)):
            if (self.should_mutate()):
                self.chromosomes[index] = 1 - self.chromosomes[index]

    def reproduce_with(self, an_individual):
        child = Individual(len(self.get_chromosomes()), self.get_mutation_rate())

        crossover_index = np.random.randint(1, len(an_individual.get_chromosomes()) - 2)
        
        child.set_chromosomes(
            (self.get_chromosomes())[:crossover_index]
            + (an_individual.get_chromosomes())[crossover_index:]
        )
        
        return child



algorithm = Algorithm(
    140, # number_of_chromosomes,
    100, # population_size,
    0.9, # crossover_rate,
    0.2, # mutation_rate,
    10 # selection_pool_size
)

algorithm.run(
    1000 # number_of_generations
)

