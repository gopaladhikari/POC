#include <iostream>
using namespace std;

int main()
{
  // Declare and initialize variables with different modifiers
  unsigned int unsignedIntVar = 42;
  long longVar = 1234567890;
  short shortVar = 32000;
  const int constIntVar = 100;
  volatile int volatileIntVar = 200;

  // Output the values of the variables
  cout << "Unsigned Integer: " << unsignedIntVar << endl;
  cout << "Long: " << longVar << endl;
  cout << "Short: " << shortVar << endl;
  cout << "Constant Integer: " << constIntVar << endl;
  cout << "Volatile Integer: " << volatileIntVar << endl;

  return 0;
}