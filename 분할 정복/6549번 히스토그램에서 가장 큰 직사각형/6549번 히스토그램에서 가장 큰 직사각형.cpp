#include <iostream>
using namespace std;

int quick_pow_2(int n) {
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return 2;
    }
    if (n % 2 == 0) {
        int sqrt = quick_pow_2(n / 2);
        return sqrt * sqrt;
    }
    int sqrt = quick_pow_2((n - 1) / 2);
    return sqrt * sqrt * 2;
}

int get_tree_size(int n) {
    int log2_n_ceil = 0;
    int tmp = n;
    while(tmp > 0) {
        tmp /= 2;
        log2_n_ceil++;
    }
    return quick_pow_2(log2_n_ceil + 1);
}

int* new_binary_tree(int tree_size) {
    return new int[tree_size];
}

int init_segment_tree(long long* histo, int* tree, int node, int start, int end) {
    if (start == end) {
        tree[node] = start;
        return tree[node];
    }
    int left_value = init_segment_tree(histo, tree, 2 * node, start, (start + end) / 2);
    int right_value = init_segment_tree(histo, tree, 2 * node + 1, (start + end) / 2 + 1, end);
    if (histo[left_value] < histo[right_value]) {
        tree[node] = left_value;
        return left_value;
    }
    tree[node] = right_value;
    return right_value;
}

int min_value_pos(long long* histo, int* tree, int node, int start, int end, long left, long right) {
    if (left > end || right < start) {
        return -1;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }
    int left_min = min_value_pos(histo, tree, 2 * node, start, (start + end) / 2, left, right);
    int right_min = min_value_pos(histo, tree, 2 * node + 1, (start + end) / 2 + 1, end, left, right);
    if (left_min == -1) {
        return right_min;
    }
    if (right_min == -1) {
        return left_min;
    }
    if (histo[left_min] < histo[right_min]) {
        return left_min;
    }
    return right_min;
}

int min_value_pos(long long* histo, int* tree, int n, long left, long right) {
    return min_value_pos(histo, tree, 1, 0, n - 1, left, right);
}

long long max_area(long long* histo, int* tree, int n, long left, long right) {
    // 탐색하지 않는 영역
    if (left > right) {
        return 0;
    }
    
    // 높이의 위치 찾기
    int height_pos = min_value_pos(histo, tree, n, left, right);
    
    
    // 너비가 1임.
    if (left == right) {
        return histo[height_pos];
    }
    long long area_with_height = histo[height_pos] * (right - left + 1);
    long long right_max = max_area(histo, tree, n, height_pos + 1, right);
    long long left_max = max_area(histo, tree, n, left, height_pos - 1);

    if (area_with_height > right_max)
    {
        if (area_with_height > left_max) {
            return area_with_height;
        }
        return left_max;
    }

    if (right_max > left_max) {
        return right_max;
    }

    return left_max;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    while(n != 0) {
        // 데이터 입력
        long long* histo = new long long[n];
        for(int i = 0; i < n; i++){
            cin >> histo[i];
        }

        // 트리 구성
        int* segment_tree = new_binary_tree(get_tree_size(n));
        segment_tree[0] = 0; // 0번 인덱스는 dummy;
        init_segment_tree(histo, segment_tree, 1, 0, n - 1);

        // 분할 정복
        long long area = max_area(histo, segment_tree, n, 0, n - 1);

        // 결과 도출 및 다음 입력
        cout << area << "\n";
        cin >> n;
    }
    return 0;
}