#include <iostream>
#include <string>
using namespace std;

class Set {
    private:
        bool count_arr[21];
    public:
        Set();

        void add(int e);
        void remove(int e);
        int check(int e);
        void toggle(int e);
        void all();
        void empty();
};

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    int cases;
    cin >> cases;

    Set x = Set();
    for(int i = 0; i < cases; i++) {
        string op;
        cin >> op;
        if (op == "add") {
            int arg;
            cin >> arg;
            
            x.add(arg);
        } else if (op == "remove") {
            int arg;
            cin >> arg;

            x.remove(arg);
        } else if (op == "check") {
            int arg;
            cin >> arg;

            cout << x.check(arg) << "\n";
        } else if (op == "toggle") {
            int arg;
            cin >> arg;

            x.toggle(arg);
        } else if (op == "all") {
            x.all();
        } else {
            x.empty();
        }
    }

    return 0;
}

Set::Set() {
    for(int i = 0; i < 21; i++) {
        count_arr[i] = false;
    }
}

void Set::add(int e) {
    if (count_arr[e]) {
        return;
    }

    count_arr[e] = true;
}

void Set::remove(int e) {
    if (count_arr[e]) {
        count_arr[e] = false;
        return;
    }
}

int Set::check(int e) {
    if (count_arr[e]) {
        return 1;
    }

    return 0;
}

void Set::toggle(int e) {
    if (count_arr[e]) {
        count_arr[e] = false;
        return;
    }

    count_arr[e] = true;
    return;
}

void Set::all() {
    for(int i = 0; i < 21; i++) {
        count_arr[i] = true;
    }
}

void Set::empty() {
    for(int i = 0; i < 21; i++) {
        count_arr[i] = false;
    }
}
