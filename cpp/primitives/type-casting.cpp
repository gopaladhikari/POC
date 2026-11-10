#include <iostream>
using namespace std;

int main()
{
  float teaPrice = 3.999;

  int roundedPrice = (int)teaPrice;

  cout << "The rounded price of tea is: " << roundedPrice << endl;

  int teaQuantity = 5;

  double totalPrice = teaPrice * teaQuantity;

  cout << "The total price of tea is: " << totalPrice << endl;

  return 0;
}