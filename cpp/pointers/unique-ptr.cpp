#include <iostream>
#include <memory>

using namespace std;

int main()
{

  unique_ptr<int> ptr(new int(10));

  unique_ptr<int> ptr2;

  ptr2.reset(new int(20));

  return 0;
}