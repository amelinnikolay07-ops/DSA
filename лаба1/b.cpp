#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int> &A) {
	int n = A.size();
	for (int i = 1; i < n; i++) {
		int key = A[i];
		int j = i;
		while (j >= 1 && A[j - 1] > key ){
			A[j] = A[j - 1];
			j--;
		}
		A[j] = key;
	}
}
	
int main() {
    vector<int> arr;
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }

    InsertionSort(arr);


    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}	
