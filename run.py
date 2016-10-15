from robots import insect
from buildings import room

if __name__ == "__main__":
	roomX, roomY = map(int, raw_input().strip().split(" "))
	roomObj = room(roomX, roomY)
	while True:
		insectCoordinates = raw_input().strip().split(" ")
		if len(insectCoordinates) != 3:
			break
		insectInstructions = raw_input()
		if insectInstructions == "":
			break
		insectObj = insect(int(insectCoordinates[0]), int(insectCoordinates[1]), insectCoordinates[2])
		insectObj.navigate(insectInstructions)
		finalCoordinates = insectObj.coordinates
		print finalCoordinates[0], finalCoordinates[1], finalCoordinates[2]
