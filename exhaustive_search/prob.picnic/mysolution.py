
 # -*- coding: utf-8 -*-. 
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

result = 0



# if 모든 애기들이 선택되었는가: 성공! return
# for 남은 번호쌍들 :
#	if 번호쌍의 애가 이미 선택된애가 아니라면:
#		애기들을 줄세우고
#		solver()
#		애기들 나오고

# 아규먼트 : 전체 애기들 숫자, 선택된 애들, 남은 애들 번호쌍
def solver(n, arrSet, arrFair):

	#print "n : %d // arrSet : %s // arrFair : %s"%(n, arrSet, arrFair)
	global result
	if len(arrSet) == n:
		result+=1
		print 'solution : %s'%arrSet
		return

	for idx, fair in enumerate(arrFair):
		if (fair[0] not in arrSet) and (fair[1] not in arrSet):
			arrSet.append(fair[0])
			arrSet.append(fair[1])
			solver(n, arrSet, arrFair[idx+1:])
			arrSet.pop()
			arrSet.pop()

	return

def picnic():
	global result
	print 'case : %d'%case
	for nStage in range(0, case):
		result = 0
		print 'solve %d'%nStage
		print 'frnds : %d, fairs : %d'%(nFriends[nStage], nFairs[nStage])
		print 'fairs : '+str(arrFairs[nStage])

		solver(nFriends[nStage], [], arrFairs[nStage])
		print result
	return


if __name__ == "__main__":
	print "hi solver"
	picnic()
