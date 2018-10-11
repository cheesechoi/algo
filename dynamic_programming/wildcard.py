#-*- coding: utf-8 -*-

'''
Wildcard

파일명 선택을 위한 와일드카드로 ? 와 * 가 있다.
? 는 모든 글자와 대응된다고 가정하고, * 는 0글자 이상의 모든 문자열에도 대응된다고 가정한다.

ex ) 	he?p --> help(o) heap(o) helpp(x)
		*p* --> help(o), papa(o), hello(x)

파일명 집합이 주어질 때, 패턴에 대응되는 파일명을 찾애는 프로그램을 작성하라.
'''

#from pwn import *

example = '''
	3
	he?p
	3
	help
	heap
	helpp
	*p*
	3
	help
	papa
	hello
	*bb*
	1
	babbbc
	'''

def nop(): return

def Wildcard(pattern, sample):
	print 'pattern : %s, sample : %s'%(pattern, sample)

	pidx = sidx = 0
	while ( (pidx < len(pattern)) and (sidx < len(sample)) ) \
			and ((pattern[pidx] == '?') or (pattern[pidx] == sample[sidx])):

		pidx += 1
		sidx += 1




	if (pidx >= len(pattern)) or (sidx >= len(sample)):
		return (pidx >= len(pattern)) and (sidx >= len(sample))

	print '%s vs %s'%(pattern[pidx:], sample[sidx:])


	return True

def solver():
	global example
	example = [i.strip() for i in example.strip().split('\n')]
	example = example[::-1]

	case = int(example.pop())
	print 'case : %d'%case
	
	for nStage in range(1, case+1):
		print '---'
		result = 0
		_pattern = example.pop()
		_nValue = int(example.pop())

		for _ in range(0, _nValue):
			_sample = example.pop()

			if Wildcard(_pattern, _sample):
				result += 1

		#print 'solve %d'%nStage
		#print 'frnds : %d, fairs : %d'%(nFriends[nStage], nFairs[nStage])
		#print 'fairs : '+str(arrFairs[nStage])

		
		print 'result : %d'%result
	return


if __name__ == "__main__":
	print "hi solver"
	solver()



