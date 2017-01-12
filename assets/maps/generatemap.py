import os
#Howdy! This is a basic script that makes a 10x10 map, filled with one block.
#To do, make map size custom
#Maybe add a random, so block is random at each point?
#Make better name for function

#Function that writes the given a filename blocktype. WARNING, b/c of w+ it will
#OVERWRITE if called...so yeah
def makeTheStuffInMapFile(filename, blockType):
	with open(filename, "w+") as f:
		yCord=0
		xCord=0
		for i in range(10):
			xCord=0
			for x in range(10):
				f.write("%s,%i,%i \n" % (blockType, xCord, yCord))
				xCord+=1
			yCord +=1


if __name__ == '__main__':
	
	filename= input("Map name? (Please add file extension at the end =P)\n")
	blockType = input("BlockName? (This will make the entire map this type)\n")
	CurrentDirectory = os.path.dirname(os.path.realpath(__file__))

	if os.path.exists(CurrentDirectory + "\%s" % (filename)):
		if input("Are you sure? This will overwrite that file. [y,n]\n") == "y":
			makeTheStuffInMapFile(blockType)
		else:
			print("kk, I'll keep that alone.\n")
			quit()
	else:
		print("No File found, I'll make you one though! =D\n")
		makeTheStuffInMapFile(blockType)

