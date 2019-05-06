#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <queue>


using std::vector; using std::string; using std::istringstream;
using std::queue; using std::pair; 


using std::cout; using std::cin; //using std::endl;
#define endl "\n";

void bfs(vector<vector<int>>& adj, vector<vector<bool>>& visited)
{
	// 중복제거를 위해, 이미 큐에 등록된 노드를 체크하기 위한 visited 변수 추가
	vector<vector<bool>> willVisit(adj.size(), vector<bool>(adj.front().size(), false));
    
	// 라운드를 셀 수 있도록! 큐는 두개 활용
	queue<pair<int, int>> qToday, qTomorrow;
	int yMax = adj.size();
	int xMax = adj.front().size();

	// 초기 진입값 확인
    qTomorrow.push(pair<int,int>(0,0));
	// 방향
	vector<pair<int, int>> direction = { {0,1}, {1,0}, {-1, 0}, {0, -1} }; // {y, x}
	int dayCount = 0;
	while ( ! (qTomorrow.empty() && qToday.empty()) )
	{
		if (qToday.empty())
		{
			// 한라운드가 끝나면 다음 큐로부터 복사
			std::swap(qToday, qTomorrow);
			dayCount++;
            //cout << "---" << dayCount << "---" << endl;
		}

		pair<int, int> here = qToday.front();
		qToday.pop();
		
        if (here.first == yMax-1 && here.second == xMax-1)
            break;
		
        visited[here.first][here.second] = true;
        //cout << "visited [x:" <<here.second << ":, y:"<<here.first << "]" << endl; 
		for (int i = 0; i < direction.size(); i++)
		{
			int ny = here.first + direction[i].first;
			int nx = here.second + direction[i].second;

			do {
				if ((ny < 0) || (ny >= adj.size())
					|| (nx < 0) || (nx >= adj.front().size())) // out of range ?
					break;

				if (visited[ny][nx]) break; // visited ?
				if (willVisit[ny][nx]) break; // already registered on next round queue ?
				if (adj[ny][nx] != 1) break; // reachable ?

				qTomorrow.push(pair<int, int>(ny, nx));
				willVisit[ny][nx] = true;
			} while (false);
		}
	}

	cout << dayCount << endl;
	return;
}


//cin 으로부터 파싱하고 데이터 만들기
void parseFromCin(vector<vector<int>> &adj, vector<vector<bool>> &visited)
{

	int x = 0, y = 0;

	string databuf, token;
	istringstream ss;
	
	getline(cin, databuf);
	ss.str(databuf);
	
	getline(ss, token, ' ');
	y = stoi(token);
	getline(ss, token, ' ');
	x = stoi(token);
	ss.clear();

	adj = vector<vector<int>>(y);


	for (int i = 0; i < y; i++)
	{
        //cout << i << endl;
		getline(cin, databuf);
		for(auto c: databuf)
		{
			adj[i].push_back(c-0x30);
		}
	}

	visited = vector<vector<bool>>(y, vector<bool>(x, false));
	return;
}

int main()
{
	
	vector<vector<int>> adj;
	vector<vector<bool>> visited;
	parseFromCin(adj, visited);
	
	bfs(adj, visited);
	
    return 0;
}
