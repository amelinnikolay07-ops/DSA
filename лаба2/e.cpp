#include <iostream>
#include <vector>

using namespace std;

bool good(const vector<int>& a, int k, int dist)
{
    int cows = 1;
    int last = a[0];

    for (int i = 1; i < a.size(); i++)
    {
        if (a[i] - last >= dist)
        {
            cows++;
            last = a[i];
        }
    }

    return cows >= k;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    int l = 0;
    int r = a[n - 1] - a[0] + 1;

    while (r - l > 1)
    {
        int m = (l + r) / 2;

        if (good(a, k, m))
            l = m;
        else
            r = m;
    }

    cout << l;

    return 0;
}
