import os
import math

class Map(object):
	def __init__(self, mapName, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.filename = mapName
		self.fileLocation = "/{}".format(mapName)
		self.mapContents = []


	def LoadMap(self, mapName, location="Default"):
		cwd = os.path.dirname(os.path.realpath(__file__))
		if location == "Default":
			mapFolder = cwd.replace("src","assets")
			mapFolder += "/maps"
		if not os.path.exists(mapFolder):
			print("File Doesn't Exist.")
			return False
		
		with open((mapFolder + "/%s"%mapName), "r") as f:
			metadata = f.readline()
			metadata = metadata.split(",")
			self.xSize = metadata[0]
			self.ySize = metadata[1]
			self.filename = metadata[2]
			
			yLineCounter = 0 
			temporaryMapContents=[]
			for line in f:
				#check to see if the line has as many chars as the meta data suggests
				#no idea why len adds one..oh wait maybe the new line \n
				if len(line)+1 == self.xSize:
					print(line)
					temporaryMapContents.append(line)
					yLineCounter+=1
			print(temporaryMapContents)



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
			for index, value in enumerate(self.mapContents):
				blockString += value
				if index%self.xSize == 0:
					f.write(blockString)
					f.write("\n")
					blockString = ''


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

	
level1 = Map("level1", 50,25)
#level1.GenerateBasicFlatMap("a","g")
print(level1.mapContents)
#level1.SaveMap()
level1.LoadMap("level1")



