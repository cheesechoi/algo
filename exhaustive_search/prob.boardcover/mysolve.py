import copy

case = 0
arrHeight = []
arrWidth = []
arrMaps = []

f = open('case.txt', 'r')

case = int(f.readline())
for i in range(0, case):

	line1 = f.readline().strip().split(' ')
	
	height = int(line1[0])
	width = int(line1[1])

	mapdata = []
	for j in range(0, height):
		mapdata.append(f.readline().strip())

	#print "%d*%d"%(width, height)
	#for data in mapdata: print data

	arrHeight.append(height)
	arrWidth.append(width)
	arrMaps.append(mapdata)	

f.close()

BLOCKS = [
			[(-1, -1), (0, -1), (0,0)],
			[(0, -1), (0,0), (-1, 0)],
			[(-1, -1), (-1,0), (0, 0)],
			[(-1, 0), (-1,-1), (0, -1)]
		]


def solver(maxx, maxy, x, y, mapdata):



	ret = 0

	if "." not in ''.join(mapdata):
		return 1
	if y > maxy:
		return 0

	print '==='
	for low in mapdata: print low
	print "x %d, y %d"%(x, y)
	print mapdata[y][x]
	#print mapdata[y]

	isFillFailed = True
	for block in BLOCKS:
		mapNext = copy.deepcopy(mapdata)
		canSet = True

		for pair in block:
			#print pair
			#print "%d %d"%(x+pair[0],y+pair[1])
			if mapNext[y+pair[1]][x+pair[0]] == "#":
				canSet = False
				break

			else:
				#mapNext[y+pair[1]][x+pair[0]] = "#"
				low = mapNext[y+pair[1]]
				#print '---'
				#print "%s, %d"%(low, x+pair[0])
				low = low[:x+pair[0]]+"#"+low[x+pair[0]+1:]
				#print low
				mapNext[y+pair[1]] = low

		if canSet:
			print 'lets paint '+str(block)

			isFillFailed = False
			ret += solver(maxx, maxy, x+1 if (x+1)<maxx else 1, y+1 if (x+1)>maxx else y, mapNext )
	
	if isFillFailed:
		print 'failed. next step!'

		ret += solver(maxx, maxy, x+2 if (x+2)<maxx else 1, y+1 if (x+2)>maxx else y, mapdata )

	return ret

def boardcover():

	print 'case : %d'%case
	for nStage in range(0, case):
		print 'solve %d'%nStage
		print 'width : %d, height : %d'%(arrWidth[nStage], arrHeight[nStage])
		print 'fairs : '+str(arrMaps[nStage])


		print solver(arrWidth[nStage]-1, arrHeight[nStage]-1, 1, 1, arrMaps[nStage])

	return


if __name__ == "__main__":
	print "hi solver"
	boardcover()
