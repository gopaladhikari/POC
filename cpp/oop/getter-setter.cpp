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

  // Getter methods
  string getName() const
  {
    return name;
  }

  int getPrice() const
  {
    return price;
  }

  // Setter methods
  void setName(const string n)
  {
    name = n;
  }

  void setPrice(int p)
  {
    price = p;
  }

  void display() const
  {
    cout << "Tea: " << name << ", Price: " << price << endl;
  }
};

int main()
{
  Tea tea("Green Tea", 50);
  tea.display();

  tea.setPrice(60);
  tea.display();

  return 0;
}
