#include <iostream>
#include <algorithm>

using namespace std;

bool good(int time, int n, int x, int y)
{
    int first = min(x, y);

    if (time < first)
        return false;

    return 1 + (time - first) / x + (time - first) / y >= n;
}

int main()
{
    int n, x, y;
    cin >> n >> x >> y;

    int l = 0;
    int r = n * min(x, y);

    while (r - l > 1)
    {
        int m = l + (r - l) / 2;

        if (good(m, n, x, y))
            r = m;
        else
            l = m;
    }

    cout << r;

    return 0;
}
