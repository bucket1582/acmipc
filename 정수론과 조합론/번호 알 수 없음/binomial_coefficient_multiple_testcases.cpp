#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

int get_binomial_coef(int n, int r) {
    // For indexing
    n++;
    r++;

    int** combination = new int*[n];
    for (int i = 0; i < n; i++)
    {
        combination[i] = new int[r];
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < r; j++)
        {
            if ((j > i) || (i == 0))
            {
                combination[i][j] = 0;
            } else if ((j == i) || (j == 0)) {
                combination[i][j] = 1;
            } else {
                combination[i][j] = combination[i - 1][j - 1] + combination[i - 1][j];
            }
            
        }
    }

    // To get result
    n--;
    r--;

    return combination[n][r];
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int N, M;
        cin >> N;
        cin >> M;
        int result = get_binomial_coef(M, N);
        cout << result << endl;
    }
    return 0;
}