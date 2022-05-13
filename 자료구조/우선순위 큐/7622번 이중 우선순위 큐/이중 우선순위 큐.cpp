#include <iostream>
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

        int* arr = new int[op_num];
        int front = 0;
        int size = 0;
        for (int op_idx = 0; op_idx < op_num; op_idx++) {
            char op;
            int arg;
            cin >> op >> arg;
            if (op == 'I')
            {
                size++;
                arr[front + size - 1] = arg;
                for (int j = front + size - 1; j > front; j--)
                {
                    if (arr[j] < arr[j - 1]) {
                        int tmp = arr[j - 1];
                        arr[j - 1] = arr[j];
                        arr[j] = tmp;
                    } else {
                        break;
                    }
                }
            } else {
                if (op == 'D')
                {
                    if (size <= 0)
                    {
                        continue;
                    } 
                    if (arg == 1)
                    {
                        size--;
                    }
                    if (arg == -1)
                    {
                        size--;
                        front++;
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
        if (size <= 0) {
            cout << "EMPTY\n";
        } else {
            cout << arr[front + size - 1] << " " << arr[front];
        }
    }   
    return 0;
}