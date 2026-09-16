#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

sing namespace std;

void countingSort(vector<int> &arr) {
    int max = *max_element(arr.begin(), arr.end());
    vector <int> count(max + 1);

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
    vector <int> arr;
    int x;
    
    while (cin >> x) {
        if (x < 0 || x > 100) {
            exit(1);
        } else {
            arr.push_back(x);
        }
    }

    countingSort(arr);
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
