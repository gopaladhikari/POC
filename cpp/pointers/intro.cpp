#include <iostream>
using namespace std;

int main()
{
  int a = 10;
  int *ptr = &a; // Pointer to an integer

  cout << "Value of a: " << a << endl;                    // Output the value of a
  cout << "Address of a: " << &a << endl;                 // Output the address of a
  cout << "Value of ptr (address of a): " << ptr << endl; // Output the value of ptr (address of a)
  cout << "Value pointed to by ptr: " << *ptr << endl;    // Output the value pointed to by ptr

  return 0;
}