import matplotlib.pyplot as plt
import numpy as np
from math import log as ln
from decimal import *

# arguments: bits of hash outputted, probability to find collision
def p(bits, probability):


	# Calculates the probabilities of bday attack
	probabilities = [i / 10000 for i in range(1, 10000)]
	hashes = [(2**bits * 2 * ln(1 / (1 - p)))**(1/2) for p in probabilities]
	ans = (2**bits * 2 * ln(1 / probability))**(1/2)

	# plots the probabilities vs the number of hashes
	plt.plot(probabilities, hashes, '-gD', markevery= (probability, ans))
	plt.plot(probability, ans, color= 'red')
	plt.xlabel('Probability')
	plt.ylabel('Number of hashes')
	plt.title('Probability of collision (' + str(bits) + ' bits)')
	plt.text(probability, ans / 2, '(0.5, ' + str(Decimal(str(ans)).normalize()) + ')')
	plt.show()

