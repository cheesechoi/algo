import copy
import time

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
			[(0, 0), (0, 1), (-1,1)],
			[(0, 0), (1,0), (1, 1)],
			[(0, 0), (0,1), (1, 1)],
			[(0, 0), (1,0), (0, 1)]
		]


def solver(maxx, maxy, mapdata):

	#maxy = 6

	nBlank = ''.join(mapdata).count('.')

	if nBlank%3 != 0: return 0
	if nBlank == 0: return 1

	ptX = (''.join(mapdata).find('.')%len(mapdata[0]))
	ptY = (''.join(mapdata).find('.')/len(mapdata[0]))

	#print mapdata[ptY][ptX]
	#return 1
	ret = 0

	print '==='
	for low in mapdata: print low
	print "x %d, y %d"%(ptX, ptY)



	for block in BLOCKS:
		mapNext = copy.deepcopy(mapdata)

		canSet = True
		for pair in block:
			#print pair
			#print "%d %d"%(x+pair[0],y+pair[1])
			if mapNext[ptY+pair[1]][ptX+pair[0]] == "#":
				canSet = False
				break

			low = mapNext[ptY+pair[1]]
			low = low[:ptX+pair[0]]+"#"+low[ptX+pair[0]+1:]
			mapNext[ptY+pair[1]] = low

		if canSet:
			isFillFailedAll = False
			ret += solver(maxx, maxy, mapNext )


	return ret

def boardcover():

	print 'case : %d'%case
	for nStage in range(0, case):
		print 'solve %d'%nStage
		print 'width : %d, height : %d'%(arrWidth[nStage], arrHeight[nStage])
		print '- fairs '
		for i in arrMaps[nStage]: print i

		print 'result : %d'%solver(arrWidth[nStage]-1, arrHeight[nStage]-1, arrMaps[nStage])

	return


if __name__ == "__main__":
	startTime = time.time()

	print "hi solver"
	boardcover()

	endTime = time.time() - startTime
	print(endTime) 

