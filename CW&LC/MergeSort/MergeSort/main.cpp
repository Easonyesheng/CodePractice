//
//  main.cpp
//  MergeSort
//
//  Created by zhangyesheng on 2019/3/7.
//  Copyright © 2019 zhangyesheng. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[]) {
    class Solution {
    public:
        
        vector<int> mergeSortedArray(vector<int> &A, vector<int> &B)
        {
            // write your code here
            vector<int> C;
            int i = 0;//a's pin
            int p = 0;//B's pin
            long int I ;
            I = A.size();
            while(i < A.size() && p < B.size())
            {
                if(A[i]<B[p])
                {
                    C.push_back(A[i]);
                    i++;
                }
                else
                {
                    C.push_back(B[p]);
                    p++;
                }
            }
            if(i == A.size())
            {
                for(int j = p;j < B.size();j++)
                {
                    C.push_back(B[j]);
                }
            }
            else
            {
                for(int j = i;j < A.size();j++)
                {
                    C.push_back(A[j]);
                }
            }
            
            return C;
        }
    };
  
    Solution S;
    int n[] = {1,2,3,4,5,6,7,8};
    //int b[] = {2,4,6,8};
    vector<int> a(n,n+1); // 1,2,3,4
    vector<int> b(n,n+1); // 3,4,5
    vector<int> C;
    C = S.mergeSortedArray(a,b);
    //c = S.mergeSortedArray(a,b);
   // cout << C;
    int j;
    for(j = 0; j < a.size(); j++)
    {
        cout << a[j] << " ";
        
    }
    cout << endl;
    for(j = 0; j < b.size(); j++)
    {
        cout << b[j] << " ";
        
    }
    cout << endl;
    for(j = 0; j < C.size(); j++)
    {
        cout << C[j] << " ";
    }


}
