#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MyClass
{
public:
  string teaName;
  int serving;
  vector<string> ingredients;

  // default constructor
  MyClass()
  {
    teaName = "Green Tea";
    serving = 1;
    ingredients = {"Green Tea Leaves", "Water", "Sugar"};
  }

  void printTeaInfo() const
  {
    cout << "Tea Name: " << teaName << endl;
    cout << "Serving Size: " << serving << endl;
    cout << "Ingredients: ";
    for (const auto &ingredient : ingredients)
    {
      cout << ingredient << ", ";
    }
    cout << endl;
  }
};

int main()
{
  MyClass myTea;

  myTea.printTeaInfo();
  return 0;
}