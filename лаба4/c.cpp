
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class MinHeap {
private:
    vector<int> heap = {0};
    int len = 0;

    void shiftUp(int i) {
        while (i > 1 && heap[i] < heap[i / 2]) {
            swap(heap[i], heap[i / 2]);
            i /= 2;
        }
    }

    int indMinChild(int i) {
        if (i * 2  > len) {
            return i * 2;
        }

        if (heap[i * 2] < heap[i * 2 + 1]) {
            return i * 2;
        }

        return i * 2 + 1;
    }

    void shiftDown(int i) {
        while (i * 2 <= len) {
            int j = indMinChild(i);

            if (heap[i] > heap[j]) {
                swap(heap[i], heap[j]);
                i = j;
            } else {
                break;
            }
        }
    }

public:
    void insert(int x) {
        heap.push_back(x);
        len++;
        shiftUp(len);
    }

    void extract() {
        if (len == 0) {
            cout << "CANNOT\n";
            return;
        }

        cout << heap[1] << '\n';

        heap[1] = heap[len];
        heap.pop_back();
        len--;

        if (len > 0) {
            shiftDown(1);
        }
    }

    void clear() {
        heap.clear();
        heap.push_back(0);
        len = 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    MinHeap heap;
    string command;

    while (cin >> command) {
        if (command == "ADD") {
            int x;
            cin >> x;
            heap.insert(x);
        }
        else if (command == "EXTRACT") {
            heap.extract();
        }
        else if (command == "CLEAR") {
            heap.clear();
        }
    }

    return 0;
}
