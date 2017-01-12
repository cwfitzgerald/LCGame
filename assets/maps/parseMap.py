import os

def parseMapFile(mapName):
	mapCordArray = []
	CurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	parseSucceed = False

	def actualParsingOfFile(filepath):
		tempLineArray = []
		with open(filepath, "r") as f: 
			for line in f:
				for x in line.split(","):
					x.strip()
					#I need to remove the " \n" but this no work at the moment
					if x.find(" \\n", 0) > -1:
						x = x.replace(" \\n", "")

					tempLineArray.append(x)
				mapCordArray.append(tempLineArray)
		return mapCordArray
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

	print(parseMapFile("map"))
