#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin >> n;

    priority_queue<int, vector<int>, less<int>> less_q;
    priority_queue<int, vector<int>, greater<int>> greater_q;
    int median;
    cin >> median;
    for(int i = 1; i < n; i++) {
        cout << median << "\n";
        int new_element;
        cin >> new_element;
        
        if (i == 1) {
            if (new_element > median) {
                greater_q.push(new_element);
            } else {
                greater_q.push(median);
                median = new_element;
            }
            continue;
        }

        if (i == 2) {
            if (new_element > median) {
                less_q.push(median);
                if (new_element > greater_q.top())
                {
                    median = greater_q.top();
                    greater_q.pop();
                    greater_q.push(new_element);
                } else {
                    median = new_element;
                }
            } else {
                less_q.push(new_element);
            }
            continue;
        }

        int less_median = less_q.top();
        int greater_median = greater_q.top();

        if (i % 2 == 0) {
            if (new_element < median) {
                less_q.push(new_element);
            } else if (new_element > greater_median) {
                less_q.push(median);
                median = greater_median;
                greater_q.pop();
                greater_q.push(new_element);
            } else {
                less_q.push(median);
                median = new_element;
            }
        } else {
            if (new_element > median) {
                greater_q.push(new_element);
            } else if (new_element < less_median) {
                greater_q.push(median);
                median = less_median;
                less_q.pop();
                less_q.push(new_element);
            } else {
                greater_q.push(median);
                median = new_element;
            }
        }
    }
    cout << median << "\n";

    return 0;
}
