import os

def parseMapFile(mapName):
	mapCordArray = []
	CurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	parseSucceed = False

	def actualParsingOfFile(filepath):
		tempLineArray = []
		with open(filepath, "r") as f: 
			mapCordArray.append([[blockType, int(xCord), int(yCord)] for blockType, xCord, yCord in [[element.strip() for element in line] for line in [line.split(',') for line in f]]])	
			return mapCordArray
			
#This code didnt freaking work...........took me 2 hours to realise that >_<
			# for line in f:
			# 	for x in line.split(","):
			# 		x.strip()
			# 		#I need to remove the " \n" but this no work at the moment
			# 		if x.find(" \\n", 0) > -1:
			# 			x = x.replace(" \\n", "")

					#tempLineArray.append(x)
				#mapCordArray.append(tempLineArray)
			
#All of this is to make sure that I'm giving the map name correctly
#If not, it returns false, []
	if os.path.exists(mapName):
		actualParsingOfFile(mapName)
		parseSucceed = True
	#This might be entirely Redundent Checkbacklater
	elif os.path.exists(CurrentDirectory + "\%s" % (mapName)):
		actualParsingOfFile(CurrentDirectory + "\%s" % (mapName))
		parseSucceed = True
	elif os.path.exists(CurrentDirectory + "\%s.txt" % (mapName)):
		actualParsingOfFile(CurrentDirectory + "\%s.txt" % (mapName))
		parseSucceed = True
	else:
		return parseSucceed, mapCordArray
	return parseSucceed, mapCordArray

def saveMapFile(mapName, mapCordArray):
	print(mapCordArray)
	#with open(mapName, "w") as f:
	# for x in mapCordArray:
	# 	tempArrayforLine =[]
	# 	for i in x:
	# 		for y in i:
	# 			print(i)
	# 			tempArrayforLine.append(i)
			
	# 		#f.write("%s,%i,%i \n" % (blockType, xCord, yCord))
	# 	print(tempArrayforLine)

if __name__ == '__main__':
	# mapCordArray = []
	# tempLineArray = []
	# with open("map2.txt", "r") as f: 
	# 	for line in f:
	# 		for x in line.split(","):
	# 			x.strip()
	# 			#I need to remove the " \n" but this no work at the moment
	# 			if x.find(" \\n", 0) > -1:
	# 				x = x.replace(" \\n", "")

	# 			tempLineArray.append(x)
	# 		mapCordArray.append(tempLineArray)

	temp = 0
	temp2 = []

	print(parseMapFile("map2.txt"))

	# saveMapFile("map2.txt", temp2)