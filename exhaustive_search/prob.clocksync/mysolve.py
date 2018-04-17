import copy
import time

case = 0
arrClocks = []

f = open('case.txt', 'r')

case = int(f.readline())
for i in range(0, case):

	line1 = f.readline().strip().split(' ')
	clocks = [int(timeval) for timeval in line1 ]
	arrClocks.append(clocks)

f.close()

SWITCH = [
			[0,1,2],
			[3,7,9,11],
			[4,10,14,15],
			[0,4,5,6,7],
			[6,7,8,10,12],
			[0,2,14,15],
			[3,14,15],
			[4,5,7,14,15],
			[1,2,3,4,5],
			[3,4,5,9,13],
		]

def is12clockAll(clocks):
	
	for clock in clocks:
		if clock != 0:
			return False
	#print 'TRUE!'+ str(clocks)
	return True

# clock : [12, 12, 12, 3, .... ] # current clock status
# psuhed : [2, 1, 0, 2, 3, ... ] # count which clicked 
def pushSwitch(clocks, pushed):

	nMin = 0xffffffff

	nSelectSwitch = len(pushed)
	if nSelectSwitch >= len(SWITCH): return nMin

	if is12clockAll(clocks):
		print 'SET!'+ str(pushed)

		return sum(pushed)

	for i in range(0, 4):

		switch = SWITCH[nSelectSwitch]

		for idx in switch:
			clocks[idx] = (clocks[idx]+(3*i))%12
		pushed.append(i)
		
		result = pushSwitch(clocks, pushed)
		nMin = min(nMin, result)

		for idx in switch:
			clocks[idx] = (clocks[idx]+(3*(4-i)))%12
		pushed.pop()

	return nMin


def clocksync():

	print 'case : %d'%case
	for nStage in range(0, case):

		global MIN
		MIN = 0
		print 'solve %d'%nStage
		print 'clocks arrange %s'%str(arrClocks[nStage])
		print 'result : %d'%pushSwitch(arrClocks[nStage], [])

	return


if __name__ == "__main__":
	startTime = time.time()

	print "hi solver"
	clocksync()

	endTime = time.time() - startTime
	print(endTime) 

