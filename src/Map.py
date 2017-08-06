import os
import math
import random

class Map(object):
	def __init__(self, mapName, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.filename = mapName
		self.fileLocation = "/{}".format(mapName)
		self.mapContents = []

	#TODO Add some error handling to exit if load fails
	#add support for files outside maps folder
	def LoadMap(self, mapName, location="Default"):
		cwd = os.path.dirname(os.path.realpath(__file__))
		if location == "Default":
			mapFolder = cwd.replace("src","assets")
			mapFolder += "/maps"
		if not os.path.exists(mapFolder):
			print("File Doesn't Exist.")
			quit()
		with open((mapFolder + "/%s"%mapName), "r") as f:
			#Parsing first line
			metadata = f.readline()
			metadata = metadata.split(",")
			TempxSize = metadata[0]
			TempySize = metadata[1]

			#Parsing Map Contents
			yLineCounter = 0 
			temporaryMapContents=[]
			for line in f:
				#check to see if the line has as many chars as the meta data suggests
				#no idea why len adds one..oh wait maybe the new line \n
				if (len(line)-1) == int(TempxSize):
					for x in line:
						if x != "\n":
							temporaryMapContents.append(x)
				else:
					print("Problem loading map, line #%i is %i chars not %i."%(yLineCounter,len(line-1),int(TempxSize)))
					quit()
				yLineCounter+=1
			f.close()

		if yLineCounter != int(TempySize):
			print("Problem loading map, there should be %i map rows, there are %i."%(int(TempySize), yLineCounter))

		#We should be confident that everything is right by here
		self.xSize = TempxSize
		self.ySize = TempySize
		#self.filename = Tempfilename
		self.mapContents=temporaryMapContents




	#check to see if file already exists, ask to overwrite
	def SaveMap(self, location="Default"):
		cwd = os.path.dirname(os.path.realpath(__file__))
		if location == "Default":
			mapFolder = cwd.replace("src","assets")
			mapFolder += "/maps"
		else:
			mapFolder = location
		if not os.path.exists(mapFolder):
			os.makedirs(mapFolder)

		with open(os.path.join(mapFolder,self.filename), "w+") as f:
			#meta data
			f.write("{0.xSize},{0.ySize},{0.filename} \n".format(self))
			
			#blocks
			blockString = ''
			stringCounter = 0
			for index, value in enumerate(self.mapContents):
				blockString += str(value)
				stringCounter+=1 
				if stringCounter==self.xSize:
					f.write(blockString)
					f.write("\n")
					blockString = ''
					stringCounter = 0


	def GenerateSingleBlockMap(self, blocktype):
		for x in range(self.xSize):
			for y in range(self.ySize):
				self.mapContents.append(blocktype)
	
	#TODO fix problem where it changes halfway through mid point
	def GenerateBasicFlatMap(self, sky, ground):
		for x in range(self.xSize):
			blocktype=''
			if x/self.xSize < .5:
				blocktype = sky
			else:
				blocktype= ground
			blocktype = blocktype*self.ySize
			
			for block in blocktype:
				self.mapContents.append(block)
	def GenerateRandomMap(self):
		blockThreshhold = 70
		for y in range(self.ySize):
			for x in range(self.xSize):
				if x == 0 or x == self.xSize-1 or y == 0 or y == self.ySize-1:
					self.mapContents.append(1)
				elif random.randint(0,99) > blockThreshhold:
					self.mapContents.append(1)
				else:
					self.mapContents.append(0)


	def NumberOfNeighbours(self, place):
		nieghbourScore = 0
		place = int(place)
		y = int(self.ySize)
		#if mapContents[place] != 
		if (place - y - 1) >= 0:
			nieghbourScore += int(self.mapContents[place - y - 1])
			print("1")
		if (place - y) >= 0:
			nieghbourScore += int(self.mapContents[place- y])
			print("2")
		if (place - y + 1) >= 0:
			nieghbourScore += int(self.mapContents[place - y + 1])
			print("3")
		if (place -1) >=0:
			nieghbourScore += int(self.mapContents[place -1])
			print("4")
		if (place + 1) <= len(self.mapContents) and (place + 1)%y !=0:
			nieghbourScore += int(self.mapContents[place + 1])
			print("5")
		if (place + y - 1) <= len(self.mapContents) and (place + y - 1)%y !=0:
			nieghbourScore += int(self.mapContents[place + y - 1])
			print("6")
		if (place + y) <= len(self.mapContents):
			nieghbourScore += int(self.mapContents[place + y])
			print("7")
		if (place + y+1) <= len(self.mapContents):
			nieghbourScore += int(self.mapContents[place + y+1])
			print("8")
		return nieghbourScore

	def SmoothMap(self, times=4):
		for x in range(times):
			for index, value in enumerate(self.mapContents):
				if self.NumberOfNeighbours(value) >= 4:
					self.mapContents[index] = 1
				else:
					self.mapContents[index]=0





	
level1 = Map("level1", 10,10)
#level1.LoadMap("level1")
#print(level1.mapContents)
level1.GenerateRandomMap()
#level1.SmoothMap(1)
print(level1.NumberOfNeighbours(0))
#print(level1.mapContents)
level1.SaveMap()




