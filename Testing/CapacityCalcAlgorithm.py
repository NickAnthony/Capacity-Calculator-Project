class capacityCalculator:
	"""
	Consumes: the temperature values for sensors 1, 2, 3
	Produces: current number of people in the building
	"""
	_clearCounter = 0
	_capacity = 0
	_trigger_list = []
	_line_check = False
	_line_counter = 0
	_readingsCount = 0

	def __init__(self):
		""" Constuctor - does nothing
		"""


	def getCapacity(self):
		return self._capacity

	def analyzeData(self, plist):
		"""Consumes: an array of 3 arrays of temperature data
		plist[0] = sensor 1
		plist[1] = sensor 2
		plist[2] = sensor 3
		Produces current capacity
		"""
		p1 = plist[0]
		p2 = plist[1]
		p3 = plist[2]
		# Get list of which sensors went off
		sensor_list = self.humanCheck(p1, p2, p3)
		# If no human is registered
		if sensor_list[0] == False and sensor_list[1] == False and sensor_list[2] == False:
			self._clearCounter += 1
			if self._clearCounter >= 4:
				self._trigger_list = []

		line_check = 0
		# Set checks to true if a human is registered
		# For trigger list: 1 is sensor 1, 2 is sensor 2, and 3 is sensor 3
		if sensor_list[0] == True:
			self._trigger_list.append(1)
			line_check += 1
		if sensor_list[1] == True:
			self._trigger_list.append(2)
			line_check += 1
		if sensor_list[2] == True:
			self._trigger_list.append(3)
			line_check += 1

		# Check if there is a line, if there is, add one person every 6 seconds
		# and ignore regular counting methods
		if line_check == 3:
			self._line_check = True
		else if line_check <= 1:
			self._line_check = False
			self._line_counter = 0
		if line_check > 0:
			self._clearCounter = 0

		line_check = 0
		# if there is a line
		if self._line_check:
			self._line_counter += 1
			if self._line_counter >= 6:
				self._capacity += 1
				self._line_counter = 0
			return self._capacity
		# if there is no line:
		else:
			if len(self._trigger_list) >= 3:
				last = self._trigger_list[len(self._trigger_list) - 1]
				if self._trigger_list[0] == 1 and last == 3:
					self._capacity += 1
					self._trigger_list = []
					return self._capacity
				if self._trigger_list[0] == 3 and last == 1 and self._capacity != 0:
					self._capacity -= 1
					self._trigger_list = []
					return self._capacity


	def humanCheck(self, p1, p2, p3):
		"""
		Consumes: the temperature values for sensors 1, 2, 3
		Produces: list of booleans for each sensor
		"""
		p1_check = False
		p2_check = False
		p3_check = False	

		# Check if there is a human in sensor 1
		counter = 0
		for temp in p1:
			if temp >= 32.5 and temp <= 35.5:
				counter += 1
		if counter >= 3:
			p1_check = True

		# Check if there is a human in sensor 2
		counter = 0
		for temp in p2:
			if temp >= 32.5 and temp <= 35.5:
				counter += 1
		if counter >= 3:
			p2_check = True

		# Check if there is a human in sensor 3
		counter = 0
		for temp in p3:
			if temp >= 32.5 and temp <= 35.5:
				counter += 1
		if counter >= 3:
			p3_check = True

		return [p1_check, p2_check, p3_check]


