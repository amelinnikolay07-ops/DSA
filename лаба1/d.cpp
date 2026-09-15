#include <iostream>
#include <vector>

void bubbleSort(std::vector<int> &arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size() - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int k = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = k;
                count++;
            }
        }
    }
    std::cout << count << std::endl;
}

int main() {
    int n;
    std::cin >> n;
    std::vector <int> arr(n);

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    bubbleSort(arr);
}
