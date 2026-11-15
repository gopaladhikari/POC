#include <iostream>
using namespace std;

void isAdult(int age)
{
  if (age < 18)
    throw "Not an adult";
  else
    cout << "You are an adult." << endl;
}

int main()
{
  int n = 10;
  int m = 0;

  try
  {
    isAdult(15);
  }
  catch (const char *msg)
  {
    cout << "Error: " << msg << endl;
  }

  try
  {
    if (m == 0)
      throw "Division by zero";
    cout << "Answer: " << n / m;
  }
  catch (const char *msg)
  {
    cout << "Error: " << msg;
  }

  int x = 7;
  try
  {
    if (x % 2 != 0)
    {

      // Throwing int
      throw -1;
    }
  }

  // Catching int
  catch (int e)
  {
    cout << "Exception Caught: " << e;
  }
  return 0;
}