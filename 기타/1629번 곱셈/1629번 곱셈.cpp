#include <stdio.h>

long long pow_with_mod(int a, int b, int c);

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    long long ans = pow_with_mod(a, b, c);
    printf("%d", ans);
    return 0;
}

long long pow_with_mod(int a, int b, int c) {
    if (b == 0) {
        return 1;
    }
    if (b == 1) {
        return a % c;
    }

    if (b % 2 == 0) {
        long long sqrt_ans = pow_with_mod(a % c, b / 2, c);
        return sqrt_ans % c * sqrt_ans % c % c;
    }

    long long sqrt_ans = pow_with_mod(a % c, (b - 1) / 2, c);
    return sqrt_ans % c * sqrt_ans % c * a % c % c;
}