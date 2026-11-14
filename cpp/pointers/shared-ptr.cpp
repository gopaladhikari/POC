#include <memory>
#include <iostream>

using namespace std;

int main()
{
  shared_ptr<int> p1 = make_shared<int>(10);
  cout << "p1: " << *p1 << endl;

  shared_ptr<int> p2 = p1; // Copying shared_ptr
  cout << "p2: " << *p2 << endl;

  cout << "Use count of p1: " << p1.use_count() << endl;
  cout << "Use count of p2: " << p2.use_count() << endl;

  p1.reset(); // Resetting p1
  cout << "After resetting p1:" << endl;
  cout << "Use count of p1: " << p1.use_count() << endl;
  cout << "Use count of p2: " << p2.use_count() << endl;
  return 0;
}