#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        int max_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] >= A[max_idx]) {
                max_idx = j;
            }
        }
        swap(A[i], A[max_idx]);
    }
}

int main() {
    vector<int> data;

    int x;
    while (cin >> x) {
        data.push_back(x);
    }

    SelectionSort(data);

    for (int i = 0; i < data.size(); i++) {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}
