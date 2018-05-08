 # -*- coding: utf-8 -*-. 
case = 0
arrnBlocks = []
arrBlocks = []

f = open('case.txt', 'r')

case = int(f.readline())

for i in range(0, case):
	nblock = f.readline().strip()

	blockWidths = f.readline().strip().split(' ')
	blockWidths = [int(i) for i in blockWidths]
	arrnBlocks.append(int(nblock)-1)
	arrBlocks.append( blockWidths ) 
	#print "parse result : %s"%arrBlocks[i]
	
f.close()


result = 0
def solver(Blocks, left, right):

	idxHalf = (right-left)/2 + left

	if right - left <= 2:
		return max(Blocks[left], Blocks[right], (right-left)*min(Blocks[left], Blocks[right]))

	leftmax = solver(Blocks, left, idxHalf)
	rightmax = solver(Blocks, idxHalf, right)

	maxval = Blocks[idxHalf]
	idxleft = idxright = idxHalf
	while (left < idxleft) and (idxright < right):
		if Blocks[idxleft-1] > Blocks[idxright+1]:
			idxleft -= 1
		else:
			idxright += 1

		maxval = max(maxval, (idxright-idxleft)*min(Blocks[idxleft:idxright]))

	maxval = max(leftmax, rightmax, maxval)
	return maxval


def fence():
	global result
	print 'all case : %d'%case
	for nStage in range(0, case):
		result = 0
		print '[case %d]'%nStage
		print '<-- arrBlocks : '+str(arrBlocks[nStage])
		result = solver(arrBlocks[nStage], 0, arrnBlocks[nStage])
		print '--> result :: %d'%(result)
	return


if __name__ == "__main__":
	print '---'
	print "hi solver"
	fence()
