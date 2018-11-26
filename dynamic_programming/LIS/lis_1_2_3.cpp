
/*
	lis 를 단순 계산으로 처리.
	리스트가 주어졌을 때, 해당 리스트로부터 조합 가능한 모든 경우의 수를 계산한다.
	lis 의 리턴은 부분합의 최댓값(lis)이기 때문에, 마지막 ret 는 앞으로 찾게 될 lis 의 값에 1을 더한 값이 된다.
	시간 복잡도는 부분 문제의 개수가 O(n)개, 한 문제가 O(n^2) 의 반복문을 순회.
	그러므로 O(n^3) 를 가진다.
*/

int lis(const vector<int> & A){
	// 기저사례 A 가 비어 있는 경우
	if(A.empty()) return 0;
	int ret = 0;

	for (int i = 0; i<A.size(); ++i)
	{
		vector<int> B;
		for(int j = i+1; j<A.size(); ++j)
			if(A[i]<A[j])
				B.push_back(A[j]);
		ret = max(ret, 1+lis(B));
	}
	return ret;
}


/*-----*/
/*
	위의 문제를 메모이제이션을 활용해서 좀 더 심플하게 고친다.
	기저사례 없음. 입력을 숫자로 바꿈으로써 이중루프를 단루프로 변경.
	시간 복잡도는 O(n^2)
*/

int n;
int cache[100], S[100];

int lis2(int start)
{
	int& ret = cache[start];
	if (ret != -1) return ret;

	//S[start]에서 시작하는 증가 부분 수열 중 최대 길이
	ret = 1;
	for (int next = start+1; next<n; ++next)
		if (S[start] < S[next])
			ret = max(ret, lis2(next)+1)
	return ret;
}

// 아래는 lis2 의 도입부를 위해 필요한 반복문이다. 매번 시작위치를 정해줘야 하기 때문에..
int maxLen = 0;
for(int begin=0; begin<n; ++begin)
	maxLen = max(maxLen, lis2(begin));


/*-------*/
/*
	위 도입부의 반복문을 만드는게 귀찮음. S[-1] == -INF 라고 가정하면 lis2(-1) 이렇게 호출해도 모든 경우의 수를 알 수 있음. 이를 통한 변형이 lis3
*/

int n;
int cache[101], S[100];

int lis3(int start)
{
	int& ret = cache[start+1];
	if(ret != -1) return ret;

	ret = 1;
	for(int next = start+1; next < n; ++next)
		if (start == -1 || S[start] < S[next])
			ret = max(ret, lis3(next) + 1)

	return ret;
}
