#include <iostream>
#include <string>
using namespace std;

class Tea
{
protected:
  string teaName;
  int serving;

public:
  Tea(string name, int servings) : teaName(name), serving(servings) {}

  virtual void brew() const
  {
    cout << "Brewing " << teaName << " tea..." << endl;
  }

  virtual void serveCup() const
  {
    cout << "Serving " << serving << " cups of " << teaName << " tea." << endl;
  }

  virtual ~Tea()
  {
    cout << "Destroying Tea object: " << teaName << endl;
  }
};

class GreenTea : public Tea
{
public:
  GreenTea(string name, int servings) : Tea(name, servings) {}

  void brew() const override
  {
    cout << "Brewing from derived class: " << teaName << " tea..." << endl;
  }
};

int main()
{
  GreenTea greenTea("Green Tea", 5);
  greenTea.brew();
  greenTea.serveCup();

  return 0;
}