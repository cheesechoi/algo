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
#print example

idx = 0

nCases = int(example[idx]); idx+=1


'''
# this is the code written first. nothing needed thinking for code. of course it's shame, but I do not want to write code like this again.

def wildcard(pattern, contents):
	print ''
	print '{} {}'.format(pattern, contents)
	iPattern = 0

	for c in contents:
		if iPattern == len(pattern):
			print '  - {}  -->false..'.format(c)
			return False

		#if '*' == pattern[iPattern] == pattern[iPattern+1]: iPattern += 1
		cp = pattern[iPattern]

		print '  {} {}'.format(c, cp)
		if   cp == '?':
			iPattern += 1
			#pass
		elif cp == '*':
			if iPattern == len(pattern)-1:
				print 'true - last wildcard'; return True

			nextcp = pattern[iPattern+1]
			if (nextcp == c):
				iPattern += 2

			if (iPattern == len(pattern)-1) and pattern[iPattern] == '*':
				print 'True'; return True
				
			else:
				pass

		elif cp == c:
			iPattern += 1
		else:
			iPattern = 0


	print 'result : {}'.format(len(pattern) == iPattern)
	return len(pattern) == iPattern
'''

def wildcard( _PATTERN,  _EXAMPLE):
	#print 'p : {}, s : {}'.format(_PATTERN, _EXAMPLE)
	idx = 0
	while True: # 문자열 범위 내에 idx 가 있으면서, 문자열이 같거나, ? 인 경우 반복
		#print idx
		#print '{} {}'.format(idx<len(_PATTERN), idx<len(_EXAMPLE))
		
		if (idx < len(_PATTERN)) and (idx < len(_EXAMPLE)) and ((_PATTERN[idx] == _EXAMPLE[idx]) or (_PATTERN[idx] == '?')):
			idx += 1
		else:
			break

	# 별표가 아니면 글자 마지막 도달이겠지. 두 글자의 마지막이 같은가 ?
	# ==> 여기서, 와일드카드 패턴이 끝난경우 / 샘플이 끝난경우 처리가 달라야 한다. 
	#	  샘플이 다 도달했을때는 와일드카드가 있지는 않았는지 체크해야 한다.
	#     패턴이 끝난경우는 무조건 샘플이 같이 끝나야 한다. 
	#     그래서 아래의 코드는 취소
	'''
	if idx == len(_PATTERN)-1 and idx == len(_EXAMPLE)-1 and (_PATTERN[idx] == _EXAMPLE[idx]): 
		print 'yes its True!'
		return True
	'''
	if idx == len(_PATTERN):
		#print 'pattern over - return %d'%(idx == len(_EXAMPLE))
		return idx == len(_EXAMPLE)
	
	# 별표인가 ?
	if _PATTERN[idx] == '*':
		for _ in range(idx, len(_EXAMPLE)+1):
			#print 'lets recursive'
			if wildcard(_PATTERN[idx+1:], _EXAMPLE[_:]):
				return True



	#print 'not same now. {} vs {}, idx {}'.format(_PATTERN, _EXAMPLE, idx)
	return False

for case in range(0, nCases):

	result = 0
	pattern = example[idx]; idx+=1
	nData = int(example[idx]); idx+=1

	for _ in range(0,nData):
		#print idx
		#print '---'
		if wildcard(pattern, example[idx]):
			print example[idx]
			result += 1
		idx += 1
		

	#print "{} case result - {}".format(case, result)





