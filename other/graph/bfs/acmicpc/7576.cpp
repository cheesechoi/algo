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
	vector<vector<bool>> willVisit(adj.size(), vector<bool>(adj.front().size(), false));

	queue<pair<int, int>> qToday, qTomorrow;
	int yMax = adj.size();
	int xMax = adj.front().size();


	for (int _y = 0; _y < yMax; _y++)
	{
		for (int _x = 0; _x < xMax; _x++)
		{
			if (adj[_y][_x] == 1)
				qTomorrow.push(pair<int,int>(_y,_x));
		}
	}
	
	vector<pair<int, int>> direction = { {0,1}, {1,0}, {-1, 0}, {0, -1} }; // {y, x}
	int dayCount = 0;
	while ( ! (qTomorrow.empty() && qToday.empty()) )
	{
		if (qToday.empty())
		{
			std::swap(qToday, qTomorrow);
			dayCount++;
		}

		pair<int, int> here = qToday.front();
		qToday.pop();
		
		visited[here.first][here.second] = true;
		for (int i = 0; i < direction.size(); i++)
		{
			int ny = here.first + direction[i].first;
			int nx = here.second + direction[i].second;

			do {
				if ((ny < 0) || (ny >= adj.size())
					|| (nx < 0) || (nx >= adj.front().size())) // out of range ?
					break;

				if (visited[ny][nx]) break; // visited ?
				if (willVisit[ny][nx]) break; // visited ?

				if (adj[ny][nx] != 0) break; // reachable ?

				qTomorrow.push(pair<int, int>(ny, nx));
				willVisit[ny][nx] = true;
			} while (false);
		}
	}

	for (int _y = 0; _y < visited.size(); _y++)
	{
		for (int _x = 0; _x < visited.front().size(); _x++)
		{
			if (visited[_y][_x] == false && adj[_y][_x] == 0)
			{
				cout << -1 << endl;
				return;
			}
		}
	}

	cout << dayCount-1 << endl;
	//return order;
	return;
}


void parseFromCin(vector<vector<int>> &adj, vector<vector<bool>> &visited)
{

	int x = 0, y = 0;

	string databuf, token;
	istringstream ss;
	
	getline(cin, databuf);
	ss.str(databuf);
	
	getline(ss, token, ' ');
	x = stoi(token);
	getline(ss, token, ' ');
	y = stoi(token);
	ss.clear();

	adj = vector<vector<int>>(y);

	for (int i = 0; i < y; i++)
	{
		getline(cin, databuf);
		ss.str(databuf);
		while (std::getline(ss, token, ' '))
		{
			adj[i].push_back(stoi(token));
			
		}
		ss.clear();
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


