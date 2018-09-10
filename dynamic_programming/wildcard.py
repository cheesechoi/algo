#-*- coding: utf-8 -*-

'''
Wildcard

파일명 선택을 위한 와일드카드로 ? 와 * 가 있다.
? 는 모든 글자와 대응된다고 가정하고, * 는 0글자 이상의 모든 문자열에도 대응된다고 가정한다.

ex ) 	he?p --> help(o) heap(o) helpp(x)
		*p* --> help(o), papa(o), hello(x)

파일명 집합이 주어질 때, 패턴에 대응되는 파일명을 찾애는 프로그램을 작성하라.
'''

from pwn import *

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


