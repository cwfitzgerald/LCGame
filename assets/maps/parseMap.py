import os

def parseMapFile(mapName):
	mapCordArray = []
	CurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	parseSucceed = False

	def actualParsingOfFile(filepath):
		tempLineArray = []
		with open(filepath, "r") as f: 
			mapCordArray = [[blockType, int(xCord), int(yCord)] for blockType, xCord, yCord in [[element.strip() for element in line] for line in [line.split(',') for line in f]]]	
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
		mapCordArray = actualParsingOfFile(mapName)
		parseSucceed = True
	#This might be entirely Redundent Checkbacklater
	elif os.path.exists(CurrentDirectory + "\%s" % (mapName)):
		mapCordArray = actualParsingOfFile(CurrentDirectory + "\%s" % (mapName))
		parseSucceed = True
	elif os.path.exists(CurrentDirectory + "\%s.txt" % (mapName)):
		mapCordArray = actualParsingOfFile(CurrentDirectory + "\%s.txt" % (mapName))
		parseSucceed = True
	else:
		return parseSucceed, mapCordArray
	return parseSucceed, mapCordArray

def saveMapFile(mapName, mapCordArray):
	#with open(mapName, "w") as f:
	#print([item for sublist in mapCordArray for item in sublist])
	for x in mapCordArray:
		print(x)
		for item in x:
			print(item)
	 		#print("%s,%i,%i \n" % (blockType, xCord, yCord))

			#f.write("%s,%i,%i,%i \n" % (filename, elo, wins, losses))

if __name__ == '__main__':

	temp = 0
	temp2 = []

	temp, temp2 = parseMapFile("thinngs.txt")
	saveMapFile("thinngs.txt", temp2)