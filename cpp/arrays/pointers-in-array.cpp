#include <iostream>
using namespace std;

int *prepareChai(int cups)
{
  int *orders = new int[cups];

  for (int i = 0; i < cups; i++)
  {
    orders[i] = (i + 1) * 10;
  }

  return orders;
}

int main()
{

  int cups = 5;

  int *orders = prepareChai(cups);

  for (int i = 0; i < cups; i++)
  {
    cout << "Order " << (i + 1) << ": " << orders[i] << " ml" << endl;
  }

  delete[] orders;

  return 0;
}
