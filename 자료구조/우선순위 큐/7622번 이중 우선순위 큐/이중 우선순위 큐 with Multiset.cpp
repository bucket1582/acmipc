#include <iostream>
#include <set>
using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int op_num;
        cin >> op_num;

        multiset<int> q;
        for (int op_idx = 0; op_idx < op_num; op_idx++) {
            char op;
            int arg;
            cin >> op >> arg;
            if (op == 'I')
            {
                q.insert(arg);
            } else {
                if (op == 'D')
                {
                    if (q.empty())
                    {
                        continue;
                    }
                    
                    if (arg == 1)
                    {
                        q.erase(--q.end());
                    } else {
                        q.erase(q.begin());
                    }
                } 
            }
            /*
            cout << "Current Size: " << size << endl;
            cout << "Current Front Index: " << front << endl;
            cout << "After Operation [" << op << " " << arg << "]: ";
            for (int j = 0; j < size; j++)
            {
                cout << arr[front + j] << " ";
            }
            cout << "\n";
            */
        }
        if (q.empty())
        {
            cout << "EMPTY\n";
        } else {
            cout << *(--q.end()) << " " << *q.begin() << "\n";
        }
    }   
    return 0;
}