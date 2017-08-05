
import os
import math

class Map(object):
	def __init__(self, mapName, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.filename = mapName
		self.fileLocation = "/{}".format(mapName)
		self.mapContents = []

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
level1.GenerateBasicFlatMap("a","g")
print(level1.mapContents)
level1.SaveMap()

# if __name__ == '__main__':
	
# 	filename= input("Map name? (Please add file extension at the end =P)\n")
# 	blockType = input("BlockName? (This will make the entire map this type)\n")
# 	CurrentDirectory = os.path.dirname(os.path.realpath(__file__))

# 	if os.path.exists(CurrentDirectory + "\%s" % (filename)):
# 		if input("Are you sure? This will overwrite that file. [y,n]\n") == "y":
# 			makeTheStuffInMapFile(filename, blockType)
# 		else:
# 			print("kk, I'll keep that alone.\n")
# 			quit()
# 	else:
# 		print("No File found, I'll make you one though! =D\n")
# 		makeTheStuffInMapFile(filename, blockType)

