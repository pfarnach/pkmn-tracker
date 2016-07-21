import json
import sys
import time
from geopy.distance import vincenty


class Catchem:

	def __init__(self):
		''' Init '''
		self.location = (45.51933087670564, -122.67473459243774)
		self.pokemon_near = []
		self.pokemon_near_filtered = []

		# JSON pulled from: https://gist.github.com/shri/9754992
		with open('pokedex.json') as json_file:
			self.pokedex = json.load(json_file)


	def loadem(self):
		''' Loads Pokemon Go API JSON '''
		self.pokemon = json.load(sys.stdin)['pokemon']


	def nameem(self):
		''' Looks up pokemon in pokedex list based on number and adds relevant info to new list '''
		for p in self.pokemon:
			pokemon = self.pokedex.get(p['pokemonId'])
			if pokemon:
				p['name'] = pokemon['name']
				p['distance_miles'] = vincenty(self.location, (p['latitude'], p['longitude'])).miles
				p['seconds_left'] = p['expiration_time'] - time.time()
				self.pokemon_near.append(p)


	def findem(self, max_seconds_left = 9999, max_distance = 1):
		''' Filters list of pokemon near by based on parameters '''
		self.pokemon_near_filtered = [p for p in self.pokemon_near if p['seconds_left'] < max_seconds_left and p['distance_miles'] < max_distance]
		[print(x['name']) for x in self.pokemon_near_filtered]


if __name__ == '__main__':
	catchem = Catchem()
	catchem.loadem()
	catchem.nameem()
	catchem.findem(max_seconds_left = 500, max_distance = 0.4)
