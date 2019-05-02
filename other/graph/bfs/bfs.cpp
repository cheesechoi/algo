// dfs.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <queue>

using std::vector; using std::string; using std::queue;

using std::cout; using std::cin; //using std::endl;
#define endl "\n";

//vector<int> bfs(vector<vector<int>>& adj, int start)
void bfs(vector<vector<int>>& adj, vector<bool>& visited, int start)
{
	//vector<bool> discovered(adj.size(), false);
	queue<int> q;
	vector<int> order;

	q.push(start);
	while (!q.empty())
	{
		int here = q.front();
		q.pop();
		order.push_back(here);
		for (int i=0; i < adj[here].size(); i++)
		{
			if (!visited[adj[here][i]])
			{
				q.push(adj[here][i]);
				visited[adj[here][i]]=true;
			}
		}
	}

	//return order;
	return;
}


void parseFromCin(vector<vector<int>> &adj, vector<bool> &visited)
{

	int nComputer = 0, nEdge = 0;

	string databuf;
	getline(cin, databuf);
	nComputer = stoi(databuf);

	getline(cin, databuf);
	nEdge = stoi(databuf);

	adj = vector<vector<int>>(nComputer + 1);

	for (int i = 0; i < nEdge; i++)
	{
		getline(cin, databuf);
		std::istringstream ss(databuf);
		string token;

		getline(ss, token, ' ');
		int nfrom = stoi(token);
		getline(ss, token, ' ');
		int nto = stoi(token);

		adj[nfrom].push_back(nto);
		adj[nto].push_back(nfrom);
	}

	visited = vector<bool>(adj.size(), false);
	return;
}

int main()
{
	//7
	//6
	//1 2
	//2 3
	//1 5
	//5 2
	//5 6
	//4 7
	//*/
	
	vector<vector<int>> adj;
	vector<bool> visited;
	parseFromCin(adj, visited);
	
	bfs(adj, visited, 1);
	
	int nResult = 0;
	for (auto c : visited)
		if (c) nResult++;

	cout << nResult-1 << endl;
    return 0;
}

