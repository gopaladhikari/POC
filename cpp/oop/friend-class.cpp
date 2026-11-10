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

  void display() const
  {
    cout << "Tea: " << name << ", Price: " << price << endl;
  }

  friend bool comparePrice(const Tea &t1, const Tea &t2);
};

bool comparePrice(const Tea &t1, const Tea &t2)
{
  return t1.price > t2.price;
}

int main()
{
  Tea tea1("Green Tea", 50);
  Tea tea2("Black Tea", 40);

  if (comparePrice(tea1, tea2))
  {
    cout << "Green Tea is more expensive." << endl;
  }
  else
  {
    cout << "Black Tea is more expensive." << endl;
  }

  return 0;
}
