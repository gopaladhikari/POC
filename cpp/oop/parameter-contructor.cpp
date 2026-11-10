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

  // parameterized constructor
  MyClass(string name, int size, vector<string> ingr)
  {
    teaName = name;
    serving = size;
    ingredients = ingr;
  }

  void printTeaInfo()
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
  MyClass customTea("Black Tea", 2, {"Black Tea Leaves", "Water", "Milk"});

  customTea.printTeaInfo();
  return 0;
}