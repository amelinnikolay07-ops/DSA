#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool good(const vector<int>& a, int k, int len)
{
    int count = 0;

    for (int rope : a)
    {
        count += rope / len;

        if (count >= k)
            return true;
    }

    return false;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    int l = 0;
    int r = *max_element(a.begin(), a.end()) + 1;

    while (r - l > 1)
    {
        int m = l + (r - l) / 2;

        if (good(a, k, m))
            l = m;
        else
            r = m;
    }

    cout << l;

    return 0;
}
