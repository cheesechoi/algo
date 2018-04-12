

case = 0
nFriends = []
nFairs = []
arrFairs = []

f = open('case.txt', 'r')


case = int(f.readline())
for i in range(0, case):

	line1 = f.readline().strip().split(' ')
	line2 = f.readline().strip().split(' ')

	nfrnd = int(line1[0])
	nfair = int(line1[1])

	arrTemp = []
	for j in range(0, 2*nfair, 2):
		arrTemp.append( [line2[j], line2[j+1]] )

	nFriends.append(nfrnd)
	nFairs.append(nfair)
	arrFairs.append(arrTemp)	

f.close()

def solver():


	return

def picnic():

	print 'case : %d'%case
	for nStage in range(0, case):
		print 'solve %d'%nStage
		print 'frnds : %d, fairs : %d'%(nFriends[nStage], nFairs[nStage])
		print 'fairs : '+str(arrFairs[nStage])


	return


if __name__ == "__main__":
	print "hi solver"
	picnic()
