import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def generate_base_pop(size, min_length, max_length):
	population = []
	while size > 0:
		child = []
		for i in range(random.choice(range(min_length, int(max_length)+1))):
			child.append(random.choice(letters))
		population.append(child)
		size -= 1
	return population

def compare(child, target):
	n = 0
	n += abs(len(child) - len(target))
	for c in child:
		if c not in target:
			n += 1
	return n

def new_gen(population, target):
	new_pop = sorted(population, key=lambda child: compare(child, target))
	return new_pop[:math.ceil(len(new_pop)/2)]

def mate(population):
	for i in range(len(population)):
		par1 = population[math.floor(random.random() * len(population))]
		par2 = population[math.floor(random.random() * len(population))]
		low = math.floor(random.random() * len(par1))
		up = math.floor(random.random() * len(par2))
		population.append(par1[low:] + par2[:up])
	return population

def mutate(population, mutate_chance, mutations):
	for child in population:
		if random.random() < mutate_chance:
			for i in range(mutations):
				index = math.floor(random.random() * len(child))
				child[index] = random.choice(letters)
	return population

def run(target, pop_size, mutate_chance, mutations):
	population = generate_base_pop(pop_size, len(target), len(target)*1.5)
	n = 0
	while target not in population:
		mutate(population, mutate_chance, mutations)
		population = new_gen(population, target)
		population = mate(population)
		n += 1
	print('took {0} generations to mutate to {1}'.format(n, target))

if __name__ == '__main__':
	run(list('hello'), 20, .2, 2)
