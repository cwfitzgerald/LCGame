import os
import math
import random
import sys

class Map(object):


	def __init__(self, mapName, xSize, ySize):
		self.xSize = int(xSize)
		self.ySize = int(ySize)
		self.filename = mapName
		self.fileLocation = "/{}".format(mapName)
		self.mapContents = []
		self.xymapContents = []

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
			TempxSize = int(metadata[0])
			TempySize = int(metadata[1])

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
		self.xymapContents = self.ConvertMapContentsToXYValue(self.xSize,self.ySize,self.mapContents)




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

	#def ConvertMapContentsToXYValue(self, x=self.xSize,y=self.ySize, array=self.mapContents):
	def ConvertMapContentsToXYValue(self, x,y, array):
		newArray =[]
		xCounter = 0
		yCounter = 0
		if len(array) == x*y:
			for value in array:
				if xCounter == x-1:
					newArray.append([xCounter,yCounter,value])
					xCounter = 0
					yCounter += 1
				else:
					newArray.append([xCounter,yCounter,value])
					xCounter+=1
			return newArray
		else:
			print("Error, array passed is incorrect")
			print("x {}, y {}".format(x,y))
			print(len(array))

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

	def GenerateRandomMap(self, blockThreshhold = 50, smooth = True, times=4,numberOfNeighboursToKeepAlive=5 ):
		for y in range(self.ySize):
			for x in range(self.xSize):
				if x == 0 or x == self.xSize-1 or y == 0 or y == self.ySize-1:
					self.mapContents.append(1)
				elif random.randint(0,99) > blockThreshhold:
					self.mapContents.append(1)
				else:
					self.mapContents.append(0)
		if smooth:
			self.xymapContents = self.ConvertMapContentsToXYValue(self.xSize,self.ySize,self.mapContents)
			self.SmoothMap(times,numberOfNeighboursToKeepAlive)

	def NumberOfNeighbours(self, xPoint,yPoint, size=1):
		nieghbourScore = 0
		searchArray = []
		#TODO Make more effiecent, repeating myself here
		searchArray.append([[xPoint-1,yPoint+1],[xPoint,yPoint+1],[xPoint+1,yPoint+1],
							[xPoint-1,yPoint],[xPoint+1,yPoint],
							[xPoint-1,yPoint-1],[xPoint,yPoint-1],[xPoint+1,yPoint-1]])

		#Using xymapContents which is [[x,y,contents], ...] find Neighbours 
		for x,y,value in self.xymapContents:
			for i in searchArray:
				for xSearch, ySearch in i:
					if x==xSearch and y == ySearch:
						nieghbourScore += value
		return nieghbourScore

	def SmoothMap(self, times,numberOfNeighboursToKeepAlive):
		totalIterationOfBlocks = 0
		for i in range(times):
			counter =0
			for x,y, value in self.xymapContents:
				if self.NumberOfNeighbours(x,y) >= numberOfNeighboursToKeepAlive:
					self.mapContents[counter] = 1
				else:
					self.mapContents[counter]=0
				counter +=1
				totalIterationOfBlocks += 1
				if counter % 200 == 0:
					sys.stdout.write("\rSmoothing...completed:{} out of {}".format(totalIterationOfBlocks,times*self.xSize*self.ySize))
		sys.stdout.write("\rSmoothing...completed:{} out of {}".format(totalIterationOfBlocks,times*self.xSize*self.ySize))







level1 = Map("level1", 25,25)
level1.GenerateRandomMap()
level1.SaveMap()




