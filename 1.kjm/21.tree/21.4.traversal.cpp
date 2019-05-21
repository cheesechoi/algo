#include <iostream>
#include <vector>

using namespace std;

vector<int> split(const vector<int>& vi, unsigned long begin, unsigned long end)
{
    return vector<int>(vi.begin() + begin, vi.begin()+end);
}

void Traversal(const vector<int>& preorder, const vector<int>& inorder)
{
    
    if (preorder.size()==0) return ;
    if (inorder.size()==0) return ;
    
    int root = preorder[0];
    int idx = std::find(inorder.begin(), inorder.end(), root) - inorder.begin();
    
    
    Traversal( split (preorder, 1, idx+1 ),
               split (inorder, 0, idx));
    Traversal( split(preorder, idx+1, preorder.size()),
               split (inorder, idx+1, inorder.size()));
    
    

    cout << root << ' ';
}



/*
 1
 7
 27 16 9 12 54 36 72
 9 12 16 27 36 54 72
*/
int main()
{
    
    int C=0;
    cin >> C;
    
    
    for (int i=0; i<C; i++)
    {
        int N = 0, tmp;
        vector<int> preorder, inorder, postorder;
        
        cin >> N;
        for (int j=0; j<N; j++)
        {
            cin >> tmp;
            preorder.push_back(tmp);
        }
        
        for (int j=0; j<N; j++)
        {
            cin >> tmp;
            inorder.push_back(tmp);
        }
        
        Traversal(preorder, inorder);
    }
}

