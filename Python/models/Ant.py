#!/user/bin/python
# coding: utf8

class Ant:
	"""docstring for Ant"""
	def __init__(self):
		self._id = arg
		self._generation = generation
		self._age = 0
		self._maxAge = maxAge
		self._future =  future
		self._religious = religious
		self._state = state
		self._life = 100
		
	def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Ant: id({}), generation({}), age({}), maxAge({}), future({}), \
        religious({}), state({}), life({})".format(self.id, self.generation, \
        self.age, self.maxAge, self.future, self.religious, self.state, \
        self.life)

	def __del__(self):
		pass

	def __getattr__(self, attr):
		pass

	def __setattr__(self, name_attr, val_attr):
		pass

	## def id
	def _get_id(self):
		return self._id

	def _set_id(self, id):
		self._id = id

	## def generation
	def _get_generation(self):
		return self._generation

	def _set_generation(self, generation):
		self._generation = generation

	## def age
	def _get_age(self):
		return self._age

	def _set_age(self, age):
		self._age = age

	## def maxAge
	def _get_maxAge(self):
		return self._maxAge

	def _set_maxAge(self, maxAge):
		self._maxAge = maxAge

	## def future
	def _get_future(self):
		return self._future

	def _set_future(self, future):
		self._future = future

	## def religious
	def _get_religious(self):
		return self._religious

	def _set_religious(self, religious):
		self._religious = religious

	## def state
	def _get_state(self):
		return self._state

	def _set_state(self, state):
		self._state = state

	## def life
	def _get_life(self):
		return self._life

	def _set_life(self, life):
		self._life = life