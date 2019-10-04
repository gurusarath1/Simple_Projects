#Birth Death Simulator
#3rd Sep 2019
#Guru Sarath

import random
import time

print(random.random())

BirthRate = 0.5
DeathRate = 0.5
Population = 0

for i in range(100000000000000):

	if random.random() < BirthRate:
		Population += 1

	if random.random() < DeathRate and Population > 0:
		Population -= 1

	if i % 10000000 == 0:
		print(i, Population)

print(i, Population)
