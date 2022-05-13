#include <stdio.h>
#include <vector>
#include <numeric>
#include <stdlib.h>
#include <algorithm>
#include <math.h>
using namespace std;

vector<int> get_divisors(int n) {
    vector<int> factors;
    for (int i = 2; i < sqrt(n) + 1; i++)
    {
        if (n % i == 0)
        {
            factors.push_back(i);
            factors.push_back(n / i);
        }
    }
    factors.push_back(n);
    return factors;
}

int main() {
    int N;
    scanf("%d", &N);

    vector<int> delta;
    int latest = 0;
    for(int i = 0; i < N; i++) {
        int new_input;
        scanf("%d", &new_input);
        if (latest != 0)
        {
            delta.push_back(abs(new_input - latest));
        }
        latest = new_input;
    }

    int gcd_val = delta[0];
    for (int i = 1; i < N - 1; i++)
    {
        gcd_val = gcd(gcd_val, delta[i]);
    }

    vector<int> divisor = get_divisors(gcd_val);
    sort(divisor.begin(), divisor.end());
    divisor.erase(unique(divisor.begin(), divisor.end()), divisor.end());
    int divisor_vector_size = divisor.size();
    for (int i = 0; i < divisor_vector_size - 1; i++)
    {
        printf("%d ", divisor[i]);
    }
    printf("%d", divisor[divisor_vector_size - 1]);
}