#-*- coding: utf-8 -*-

'''
Wildcard

파일명 선택을 위한 와일드카드로 ? 와 * 가 있다.
? 는 모든 글자와 대응된다고 가정하고, * 는 0글자 이상의 모든 문자열에도 대응된다고 가정한다.

ex ) 	he?p --> help(o) heap(o) helpp(x)
		*p* --> help(o), papa(o), hello(x)

파일명 집합이 주어질 때, 패턴에 대응되는 파일명을 찾애는 프로그램을 작성하라.
'''

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
'''.strip()

example = example.split('\n')
idx = 0
nCases = int(example[idx]); idx+=1

arrCache = [[-1 for i in range(101)] for j in range(101)]

S = ''
W = ''
#def wildcard( _PATTERN,  _EXAMPLE):
def wildcard( w,  s):
	global S, W
	#print 'W : {}, w : {}, S : {}, s : {}'.format(W, w, S, s)
	
	ret = arrCache[w][s]
	if ret != -1: return ret

	idx = 0
	while True: # 문자열 범위 내에 idx 가 있으면서, 문자열이 같거나, ? 인 경우 반복

		if (w < len(W)) and (s < len(S)) and ((W[w] == S[s]) or (W[w] == '?')):
			w+=1
			s+=1
		else:
			break

	if w == len(W):
		#print 'pattern over - return %d'%(s == len(S))
		arrCache[w][s] = (s == len(S))
		return s == len(S)
	
	# 별표인가 ?
	if W[w] == '*':
		for _ in range(s, len(S)+1):
			#print 'lets recursive'
			if wildcard(w+1, _):
				#print 'return true from recursive'
				arrCache[w][s] = True
				return True

	arrCache[w][s] = False
	return False

for case in range(0, nCases):

	global W, S
	result = 0
	pattern = example[idx]; idx+=1
	nData = int(example[idx]); idx+=1


	for _ in range(0,nData):
		#print idx
		#print '---'
		
		W = pattern
		S = example[idx]

		if wildcard(0, 0):
			print example[idx] + ' accepted'
			result += 1
		idx += 1
		

	#print "{} case result - {}".format(case, result)



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
'''
'''
def solver():
	global example
	#example = [i.strip() for i in example.strip().split('\n')]
	example = example[::-1]

	case = int(example.pop())
	#print 'case : %d'%case
	
	for nStage in range(1, case+1):
		#print '---'
		result = 0
		_pattern = example.pop()
		_nValue = int(example.pop())

		for _ in range(0, _nValue):
			_sample = example.pop()

			if wildcard(_pattern, _sample):
				result += 1
	
		#print 'result : %d'%result
	return


if __name__ == "__main__":
	#print "hi solver"
	solver()
'''


