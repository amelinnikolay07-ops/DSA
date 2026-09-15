#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

void countingSort(std::vector<int> &arr) {
    int max = *std::max_element(arr.begin(), arr.end());
    std::vector <int> count(max + 1);

    for (int i = 0; i < arr.size(); i++) {
        count[arr[i]]++;
    }

    int index = 0;
    for (int i = 0; i < count.size(); i++) {
        while (count[i] > 0) {
            arr[index++] = i;
            count[i]--;
        }
    }
}

int main(){
    std::vector <int> arr;
    int x;
    
    while (std::cin >> x) {
        if (x < 0 || x > 100) {
            std::exit(1);
        } else {
            arr.push_back(x);
        }
    }

    countingSort(arr);
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
