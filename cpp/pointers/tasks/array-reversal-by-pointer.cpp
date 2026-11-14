#include <iostream>

using namespace std;

void reversePrices(double *start, double *end)
{
  while (start < end)
  {
    double temp = *start;
    *start = *end;
    *end = temp;
    start++;
    end--;
  }
}

int main()
{

  double prices[] = {10.5, 20.0, 30.75, 40.25, 50.0};

  const int SIZE = sizeof(prices) / sizeof(prices[0]);

  cout << "Original prices: ";
  for (int i = 0; i < SIZE; i++)
  {
    cout << prices[i] << " ";
  }

  cout << endl;

  reversePrices(prices, prices + SIZE - 1);

  cout << "Reversed prices: ";
  for (int i = 0; i < SIZE; i++)
  {
    cout << prices[i] << " ";
  }
  cout << endl;

  return 0;
}