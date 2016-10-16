from robots import insect
from buildings import room

if __name__ == "__main__":
	try:
		roomX, roomY = map(int, raw_input().strip().split(" "))
		while True:
			insectCoordinates = raw_input().strip().split(" ")
			if len(insectCoordinates) != 3:
				break
			insectInstructions = raw_input()
			if insectInstructions == "":
				break
			insectObj = insect(room=room(roomX, roomY), initialX=int(insectCoordinates[0]),
							   initialY=int(insectCoordinates[1]), initialDirection=insectCoordinates[2])
			insectObj.navigate(insectInstructions)
			finalCoordinates = insectObj.coordinates
			print finalCoordinates[0], finalCoordinates[1], finalCoordinates[2]
	except Exception as e:
		print e, " some problem"  # just log it
