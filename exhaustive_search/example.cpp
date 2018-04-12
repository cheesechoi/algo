#include <iostream>
#include <vector>
using namespace std;

void printNode(vector<int>& lists)
{
	for (vector<int>::size_type i = 0 ; i < lists.size() ; i++)
		cout << lists[i] << " ";
	cout << endl;
	return;
}

void pick(int n, vector<int>& lists, int topick){

	if ( 0 == topick ) { printNode(lists); return; }

	int smallest = lists.empty() ? 0 : lists.back()+1;

	for(int next = smallest; next < n ; next ++)
	{
		lists.push_back(next);
		pick(n, lists, topick-1);
		lists.pop_back();
	}
	
	return;
}

int main(int argc, char** argv)
{
	cout << "hi all" << endl;
	vector<int> v;
	pick(10, v, 3);
	return 0;
}
