#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <queue>

#define debug 1

#ifdef debug
#define DEBUG(x) cout << x << endl;
#else
#define DEBUG(x)
#endif

using std::vector; using std::string; using std::istringstream;
using std::queue; using std::pair; 


using std::cout; using std::cin; //using std::endl;
#define endl "\n";



struct _point{
    int x;
    int y;
    int z;
};
typedef _point Point;

void bfs(vector<vector<vector<int>>>& adj, vector<vector<vector<bool>>>& visited)
{
	vector<vector<vector<bool>>> willVisit(visited);
    //adj.size(), vector<bool>(adj.front().size(), false));

    queue<Point> qToday, qTomorrow;
	int zMax = adj.size();
	int yMax = adj.front().size();
	int xMax = adj.front().front().size();


    for (int _z = 0; _z < zMax; _z++){
        for (int _y = 0; _y < yMax; _y++){
            for (int _x = 0; _x < xMax; _x++){
                if (adj[_z][_y][_x] == 1)
                    qTomorrow.push({_x, _y, _z});
            }
        }
    }

	vector<Point> direction = { {0, 0,1}, {0, 1,0}, {0, -1, 0}, {0, 0, -1}, {1, 0, 0},{-1,0,0}  }; // {y, x}
	int dayCount = 0;
	while ( ! (qTomorrow.empty() && qToday.empty()) )
	{
		if (qToday.empty())
		{
			std::swap(qToday, qTomorrow);
			dayCount++;
		}

		Point here = qToday.front();
		qToday.pop();
	    
        //cout << visited.size() << visited.front().size() << visited.front().front().size() << endl;
        //cout << "z"<< here.z << "," << "y"<<here.y << ","<< "x"<<here.x << "visited" << endl;

		visited[here.z][here.y][here.x] = true;
        //cout << "test"<<endl;
		for (int i = 0; i < direction.size(); i++)
		{
            //cout << "yeah " << endl;
			int nx = here.x + direction[i].x;
			int ny = here.y + direction[i].y;
			int nz = here.z + direction[i].z;

			do {
                //cout << "do" << endl;
				if (   (nz < 0) || (nz >= zMax)
					|| (ny < 0) || (ny >= yMax)
                    || (nx < 0) || (nx >= xMax)) // out of range ?
					break;
                
				if (  visited[nz][ny][nx]) break; // visited ?
				if (willVisit[nz][ny][nx]) break; // visited ?
				if (      adj[nz][ny][nx] != 0) break; // reachable ?

                //cout << "lets visit " << nx << ny << nz << endl;
				qTomorrow.push({nx, ny, nz});
				willVisit[nz][ny][nx] = true;
			} while (false);
		}
	}
	for (int _z = 0; _z < zMax; _z++)
	{
		for (int _y = 0; _y < yMax; _y++)
		{
            for(int _x = 0; _x < xMax; _x++)
            {
                if (visited[_z][_y][_x] == false && adj[_z][_y][_x] == 0)
                {
                    cout << -1 << endl;
                    return;
                }
            }
		}
	}
    //cout << "well?" << endl;

	cout << dayCount-1 << endl;
	//return order;
	return;
}


void parseFromCin(vector<vector<vector<int>>> &adj, vector<vector<vector<bool>>> &visited)
{

	int x = 0, y = 0, h = 0;

	string databuf, token;
	istringstream ss;
	
	getline(cin, databuf);
	ss.str(databuf);
	
	getline(ss, token, ' ');
	x = stoi(token);
	getline(ss, token, ' ');
	y = stoi(token);
	getline(ss, token, ' ');
	h = stoi(token);
	ss.clear();


    adj = vector<vector<vector<int>>>(h);
    for (int _h = 0; _h < h ; _h++)
    {
        adj[_h] = vector<vector<int>>(y);
        for (int i = 0; i < y; i++)
        {
            getline(cin, databuf);
            ss.str(databuf);
            while (std::getline(ss, token, ' '))
            {
                adj[_h][i].push_back(stoi(token));
                
            }
            ss.clear();
        }
    }
	visited = vector<vector<vector<bool>>>(h, vector<vector<bool>>(y, vector<bool>(x, false)));
	return;
}

int main()
{
	vector<vector<vector<int>>> adj;
	vector<vector<vector<bool>>> visited;
	parseFromCin(adj, visited);

    //cout << "----" <<endl;
    /*
	for (int _z = 0; _z < visited.size(); _z++)
	{
		for (int _y = 0; _y < visited.front().size(); _y++)
		{
            for(int _x = 0; _x < adj.front().front().size(); _x++)
            {
                cout << adj[_z][_y][_x] << " ";
            }
            cout << endl;
		}
	}
    */
    //cout << "visited size " << visited.size() << visited.front().size() << visited.front().front().size() << endl;	
    bfs(adj, visited);
	
    return 0;
}


