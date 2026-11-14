#include <memory>
#include <iostream>

using namespace std;

int main()
{
  shared_ptr<int> p1 = make_shared<int>(10);
  cout << "p1: " << *p1 << endl;

  weak_ptr<int> wp = p1; // Creating weak_ptr from shared_ptr
  cout << "Use count of p1: " << p1.use_count() << endl;
  cout << "Use count of wp: " << wp.use_count() << endl;

  if (auto sp = wp.lock())
  { // Locking weak_ptr to get shared_ptr
    cout << "Locked weak_ptr to shared_ptr: " << *sp << endl;
  }
  else
  {
    cout << "weak_ptr is expired." << endl;
  }

  p1.reset(); // Resetting p1
  cout << "After resetting p1:" << endl;
  cout << "Use count of p1: " << p1.use_count() << endl;
  cout << "Use count of wp: " << wp.use_count() << endl;

  if (auto sp = wp.lock())
  { // Attempting to lock weak_ptr again
    cout << "Locked weak_ptr to shared_ptr: " << *sp << endl;
  }
  else
  {
    cout << "weak_ptr is expired." << endl;
  }

  return 0;
}