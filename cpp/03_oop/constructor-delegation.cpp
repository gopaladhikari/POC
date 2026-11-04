#include <iostream>
#include <string>

using namespace std;

class Tea
{
private:
  string name;
  int price;

public:
  Tea(string n, int p) : name(n), price(p) {}

  Tea() : Tea("Default Tea", 10) {} // Delegating constructor

  void display() const
  {
    cout << "Tea: " << name << ", Price: " << price << endl;
  }
};

int main()
{
  Tea tea1("Green Tea", 50);
  Tea tea2;

  tea1.display();
  tea2.display();

  return 0;
}
