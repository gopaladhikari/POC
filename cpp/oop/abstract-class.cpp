#include <iostream>
using namespace std;

class Tea
{
public:
  virtual void getIngredients() = 0; // pure virtual function

  virtual void bew() = 0; // pure virtual function

  virtual void serve() = 0; // pure virtual function

  void makeTea()
  {
    getIngredients();
    bew();
    serve();
  }
};

// Derived class for Green Tea

class GreenTea : public Tea
{
public:
  void getIngredients() override
  {
    cout << "Getting green tea ingredients..." << endl;
  }

  void bew() override
  {
    cout << "Brewing green tea..." << endl;
  }

  void serve() override
  {
    cout << "Serving green tea..." << endl;
  }
};

int main()
{
  GreenTea greenTea;
  greenTea.makeTea();

  return 0;
}