#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

int main() {
    int N, K;
    cin >> N;
    cin >> K;

    // For indexing
    N++;
    K++;

    int** combination = new int*[N];
    for (int i = 0; i < N; i++)
    {
        combination[i] = new int[K];
    }
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < K; j++)
        {
            if ((j > i) || (i == 0))
            {
                combination[i][j] = 0;
            } else if ((j == i) || (j == 0)) {
                combination[i][j] = 1;
            } else {
                combination[i][j] = (combination[i - 1][j - 1] + combination[i - 1][j]) % (10007);
            }
            
        }
    }

    // To get result
    N--;
    K--;

    cout << combination[N][K];
    return 0;
}