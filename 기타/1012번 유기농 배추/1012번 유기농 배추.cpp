#include <iostream>
using namespace std;

void erase_neighbors(bool** field, int x, int y, int n, int m) {
    if ((x < 0) || (x > n - 1)) return ;
    if ((y < 0) || (y > m - 1)) return ;
    field[x][y] = 0;
    if ((x < n - 1) && (field[x + 1][y])) erase_neighbors(field, x + 1, y, n, m);
    if ((x > 0) && (field[x - 1][y])) erase_neighbors(field, x - 1, y, n, m);
    if ((y < m - 1) && (field[x][y + 1])) erase_neighbors(field, x, y + 1, n, m);
    if ((y > 0) && (field[x][y - 1])) erase_neighbors(field, x, y - 1, n, m); 
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n, m, k;
        cin >> n >> m >> k;

        // initialize
        bool** field = new bool*[n];
        for (int j = 0; j < n; j++)
        {
            field[j] = new bool[m];
            for (int y = 0; y < m; y++)
            {
                field[j][y] = false;
            }
        }
        
        for (int j = 0; j < k; j++)
        {
            int x, y;
            cin >> x >> y;
            field[x][y] = true;
        }

        int cnt = 0;
        for (int x = 0; x < n; x++)
        {
            for (int y = 0; y < m; y++) {
                if (field[x][y])
                {
                    cnt++;
                    erase_neighbors(field, x, y, n, m);
                }
            }
        }

        cout << cnt << "\n";
    }
    
    return 0;
}