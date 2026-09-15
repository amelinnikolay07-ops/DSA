#include <iostream>
#include <vector>

void bubbleSort(std::vector<int> &arr) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size() - 1 - i; j++) {
            if (arr[j] < arr[j + 1]) {
                int k = arr[j]; 
                arr[j] = arr[j + 1];
                arr[j + 1] = k;
            }
        }
    }
}

int main() {
    std::vector <int> arr;
    int x;
    while (std::cin >> x) {
        arr.push_back(x);
    }
    
    bubbleSort(arr);

    for (int i =0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
