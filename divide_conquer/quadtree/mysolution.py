
 # -*- coding: utf-8 -*-. 
case = 0
arrCubes = []

f = open('case.txt', 'r')

case = int(f.readline())

def parseCube(arrDefCube):
	retarr = []

	currData = arrDefCube.pop(0)
	if currData != 'x':
		return [currData]

	for part in range(0, 4):
		if arrDefCube[0] != 'x':
			currData = arrDefCube.pop(0)
			retarr.append(currData)
		else:
			nextnode = parseCube(arrDefCube)
			retarr.append(nextnode)

	return retarr

for i in range(0, case):
	line = list(f.readline().strip())
	print "line : %s"%str(line)
	arrCubes.append( parseCube( line ) )
	#print "parse result : %s"%arrCubes[i]
	
f.close()

result = 0

def setter(arrSolved):
	ret = []
	for i in arrSolved:

		if len(i) == 1:
			ret.append(i)
		else:
			ret.append('x')
			ret += setter(i)
	
	return ret

def solver(partsCube):

	#print "n : %d // arrSet : %s // arrFair : %s"%(n, arrSet, arrFair)
	#print partsCube
	if len(partsCube) < 4:
		return partsCube

	solver(partsCube[0])
	solver(partsCube[1])
	solver(partsCube[2])
	solver(partsCube[3])

	#print 'swap 0 : %s, 2 : %s'%(partsCube[0], partsCube[2])
	#print 'swap 1 : %s, 3 : %s'%(partsCube[1], partsCube[3])
	partsCube[0], partsCube[2] = partsCube[2], partsCube[0]
	#print 'afterchange 1 : '+str(partsCube)

	partsCube[1], partsCube[3] = partsCube[3], partsCube[1]
	#print 'afterchange 2 : '+str(partsCube)
	return partsCube

def quadtree():
	global result
	print 'case : %d'%case
	for nStage in range(0, case):
		result = 0
		print 'solve %d'%nStage
		print 'arrCubes : '+str(arrCubes[nStage])
		result = solver(arrCubes[nStage])
		print 'result :: ' + ''.join(setter(result))
	return


if __name__ == "__main__":
	print '---'
	print "hi solver"
	quadtree()
