from CapacityCalcAlgorithm import *

def test_1():
	""" Test capacity when a person enters and then a person leaves
	"""
	yes = [20.3, 20.4, 21.4, 34.3, 34.3, 34.4, 34.0, 20.3]
	no = [20.3, 20.4, 21.4, 24.3, 24.3, 24.4, 24.0, 20.3]

	nothing = [no, no, no]
	sensor1 = [yes,no,no]
	sensor2 = [no,yes,no]
	sensor3 = [no,no,yes]
	
	test_1_list = [nothing, nothing, nothing, nothing, sensor1, sensor2, sensor3, nothing, nothing]

	myCalc = capacityCalculator()

	for reading in test_1_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 1 entering = %s") %(myCalc.getCapacity())

	test_2_list = [nothing, nothing, nothing, nothing, sensor3, sensor2, sensor1, nothing, nothing]

	for reading in test_2_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 1 leaving = %s") %(myCalc.getCapacity())

def test_2():
	""" Test capacity when a 5 people enter and then 3 leave
	"""
	yes = [20.3, 20.4, 21.4, 34.3, 34.3, 34.4, 34.0, 20.3]
	no = [20.3, 20.4, 21.4, 24.3, 24.3, 24.4, 24.0, 20.3]

	nothing = [no, no, no]
	sensor1 = [yes,no,no]
	sensor2 = [no,yes,no]
	sensor3 = [no,no,yes]

	myCalc = capacityCalculator()
	
	test_1_list_1 = [nothing, nothing, sensor1, sensor2, sensor3, nothing, nothing]
	test_1_list_2 = [nothing, nothing, nothing, sensor1, sensor2, sensor3, sensor1, sensor2, sensor3, nothing]
	test_1_list_3 = [sensor1, sensor2, sensor3, nothing, nothing, nothing, sensor1, sensor2, sensor3, nothing]
	test_1_list = test_1_list_1 + test_1_list_2 +test_1_list_3

	for reading in test_1_list:
		myCalc.analyzeData(reading)

	test_2_list_1 = [nothing, nothing, sensor3, sensor2, sensor1, nothing, nothing]
	test_2_list_2 = [nothing, nothing, nothing, sensor3, sensor2, sensor1, sensor3, sensor2, sensor1, nothing]
	test_2_list = test_2_list_1 + test_2_list_2

	for reading in test_2_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 5 enter and 3 leave = %s") %(myCalc.getCapacity())

def test_3():
	""" Test if someone leaves when capacity is 0 and test if someone enters halfway
	"""
	yes = [20.3, 20.4, 21.4, 34.3, 34.3, 34.4, 34.0, 20.3]
	no = [20.3, 20.4, 21.4, 24.3, 24.3, 24.4, 24.0, 20.3]

	nothing = [no, no, no]
	sensor1 = [yes,no,no]
	sensor2 = [no,yes,no]
	sensor3 = [no,no,yes]

	myCalc = capacityCalculator()
	
	test_1_list = [nothing, nothing, sensor3, sensor2, sensor1, nothing, nothing]
	for reading in test_1_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 1 leaves with no capacity = %s") %(myCalc.getCapacity())

	test_2_list = [nothing, nothing, sensor1, sensor2, sensor2, sensor3, sensor2, sensor1, nothing]
	for reading in test_2_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 1 goes all the way and back = %s") %(myCalc.getCapacity())

	test_3_list = [nothing, sensor1, sensor2, sensor2, sensor2, sensor1, nothing, nothing]
	for reading in test_3_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 1 goes halfway and back = %s") %(myCalc.getCapacity())

def test_line():
	""" Test capacity when there is line
	"""
	yes = [20.3, 20.4, 21.4, 34.3, 34.3, 34.4, 34.0, 20.3]
	no = [20.3, 20.4, 21.4, 24.3, 24.3, 24.4, 24.0, 20.3]

	nothing = [no, no, no]
	all_sensors = [yes,yes,yes]
	two_sensors = [no,yes,yes]
	sensor1 = [yes,no,no]
	sensor2 = [no,yes,no]
	sensor3 = [no,no,yes]

	myCalc = capacityCalculator()
	test_4_list = [nothing, nothing]
	for i in range(0,65):
		if i == 6 or i ==23:
			test_4_list.append(two_sensors)
		else:
			test_4_list.append(all_sensors)

	for reading in test_4_list:
		myCalc.analyzeData(reading)

	print ("Capacity after 65 seconds of a line is = %s") %(myCalc.getCapacity())



if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_line()
