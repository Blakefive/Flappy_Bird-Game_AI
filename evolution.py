import pygame, random
import numpy as np
from copy import deepcopy
from game import game_main
from genome import Genome

N_POPULATION = 50
N_BEST = 5
N_CHILDREN = 3
PROB_MUTATION = 0.6

WIN_WIDTH = 284 * 2     
WIN_HEIGHT = 512

pygame.init()
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Flappy Bird Game')
score_font = pygame.font.SysFont(None, 32, bold=True)
clock = pygame.time.Clock()
        
# generate 1st population
genomes = [Genome() for _ in range(N_POPULATION)]
best_genomes = None

n_gen = 0
while True:
  n_gen += 1

  for i, genome in enumerate(genomes):
    game = game_main(genome, display_surface, score_font, clock)
    try:
      game.main()
    except TypeError:
      pass
    display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    genome.fitness = game.fitness
    genome.score = game.score
    print("genome.fitness, genome.score", genome.fitness, genome.score)

  if best_genomes is not None:
    genomes.extend(best_genomes)
  genomes.sort(key=lambda x: x.fitness, reverse=True)

  print('===== Generaton #%s Best Fitness %s Score %s =====' % (n_gen, genomes[0].fitness, genomes[0].score))

  best_genomes = deepcopy(genomes[:N_BEST])

  # crossover
  for i in range(N_CHILDREN):
    new_genome = deepcopy(best_genomes[0])
    a_genome = random.choice(best_genomes)
    b_genome = random.choice(best_genomes)

    cut = random.randint(0, new_genome.w1.shape[1])
    new_genome.w1[i, :cut] = a_genome.w1[i, :cut]
    new_genome.w1[i, cut:] = b_genome.w1[i, cut:]

    cut = random.randint(0, new_genome.w2.shape[1])
    new_genome.w2[i, :cut] = a_genome.w2[i, :cut]
    new_genome.w2[i, cut:] = b_genome.w2[i, cut:]

    cut = random.randint(0, new_genome.w3.shape[1])
    new_genome.w3[i, :cut] = a_genome.w3[i, :cut]
    new_genome.w3[i, cut:] = b_genome.w3[i, cut:]

    cut = random.randint(0, new_genome.w4.shape[1])
    new_genome.w4[i, :cut] = a_genome.w4[i, :cut]
    new_genome.w4[i, cut:] = b_genome.w4[i, cut:]

    cut = random.randint(0, new_genome.w5.shape[1])
    new_genome.w5[i, :cut] = a_genome.w5[i, :cut]
    new_genome.w5[i, cut:] = b_genome.w5[i, cut:]
    

    cut = random.randint(0, new_genome.b1.shape[0])
    new_genome.b1[:cut] = a_genome.b1[:cut]
    new_genome.b1[cut:] = b_genome.b1[cut:]

    cut = random.randint(0, new_genome.b2.shape[0])
    new_genome.b2[:cut] = a_genome.b2[:cut]
    new_genome.b2[cut:] = b_genome.b2[cut:]

    cut = random.randint(0, new_genome.b3.shape[0])
    new_genome.b3[:cut] = a_genome.b3[:cut]
    new_genome.b3[cut:] = b_genome.b3[cut:]

    cut = random.randint(0, new_genome.b4.shape[0])
    new_genome.b4[:cut] = a_genome.b4[:cut]
    new_genome.b4[cut:] = b_genome.b4[cut:]

    cut = random.randint(0, new_genome.b5.shape[0])
    new_genome.b5[:cut] = a_genome.b5[:cut]
    new_genome.b5[cut:] = b_genome.b5[cut:]

    best_genomes.append(new_genome)

  # mutation
  genomes = []
  for i in range(int(N_POPULATION / (N_BEST + N_CHILDREN))):
    for bg in best_genomes:
      new_genome = deepcopy(bg)

      mean = 20
      stddev = 10

      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.w1 += new_genome.w1 * np.random.normal(mean, stddev, size=(3, 1)) / 100 * np.random.randint(-1, 2, (3, 1))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.w2 += new_genome.w2 * np.random.normal(mean, stddev, size=(10, 15)) / 100 * np.random.randint(-1, 2, (10, 15))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.w3 += new_genome.w3 * np.random.normal(mean, stddev, size=(15, 20)) / 100 * np.random.randint(-1, 2, (15, 20))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.w4 += new_genome.w4 * np.random.normal(mean, stddev, size=(20, 10)) / 100 * np.random.randint(-1, 2, (20, 10))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.w5 += new_genome.w5 * np.random.normal(mean, stddev, size=(10, 1)) / 100 * np.random.randint(-1, 2, (10, 1))

      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.b1 += new_genome.b1 * np.random.normal(mean, stddev, size=(1)) / 100 * np.random.randint(-1, 2, (1))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.b2 += new_genome.b2 * np.random.normal(mean, stddev, size=(15)) / 100 * np.random.randint(-1, 2, (15))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.b3 += new_genome.b3 * np.random.normal(mean, stddev, size=(20)) / 100 * np.random.randint(-1, 2, (20))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.b4 += new_genome.b4 * np.random.normal(mean, stddev, size=(10)) / 100 * np.random.randint(-1, 2, (10))
      if random.uniform(0, 1) < PROB_MUTATION:
        new_genome.b5 += new_genome.b5 * np.random.normal(mean, stddev, size=(1)) / 100 * np.random.randint(-1, 2, (1))

      genomes.append(new_genome)
