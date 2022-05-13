#include <iostream>
#include <numeric>
#include <string>
using namespace std;

string get_reduced_fraction_of_two_cranks(int std_crank, int comp_crank){
    int gcd_val = gcd(std_crank, comp_crank);
    int numerator = std_crank / gcd_val;
    int divisor = comp_crank / gcd_val;

    return to_string(numerator) + "/" + to_string(divisor);
}

int main() {
    int N;
    cin >> N;

    int* crank_arr = new int[N - 1];

    int std_crank;
    cin >> std_crank;

    for (int i = 0; i < N - 1; i++) {
        cin >> crank_arr[i];
    }

    for (int i = 0; i < N - 1; i++)
    {
        cout << get_reduced_fraction_of_two_cranks(std_crank, crank_arr[i]) << endl;
    }
    return 0;
}