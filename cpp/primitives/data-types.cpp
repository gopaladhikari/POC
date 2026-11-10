#include <iostream>
using namespace std;

int main()
{
  // Declare and initialize variables of different data types
  int integerVar = 42;
  float floatVar = 3.14f;
  double doubleVar = 2.71828;
  char charVar = 'A';
  bool boolVar = true;

  // Output the values of the variables
  cout << "Integer: " << integerVar << endl;
  cout << "Float: " << floatVar << endl;
  cout << "Double: " << doubleVar << endl;
  cout << "Character: " << charVar << endl;
  cout << "Boolean: " << boolalpha << boolVar << endl;

  return 0;
}