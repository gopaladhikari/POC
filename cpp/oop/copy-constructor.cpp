#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MyClass
{
public:
  string *teaName;
  int serving;
  vector<string> ingredients;

  // parameterized constructor
  MyClass(string name, int size, vector<string> ingr)
  {
    teaName = new string(name);
    serving = size;
    ingredients = ingr;
  }

  MyClass(const MyClass &other)
  {
    teaName = new string(*other.teaName); // Deep copy of teaName
    serving = other.serving;
    ingredients = other.ingredients; // Vector has its own copy constructor
  }

  ~MyClass()
  {
    delete teaName;

    cout << "Destructor called for tea: " << endl;
  }

  void printTeaInfo() const
  {
    cout << "Tea Name: " << *teaName << endl;
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
  MyClass myTea("Black Tea", 2, {"Black Tea Leaves", "Water", "Milk"});

  MyClass copiedTea(myTea); // Copy constructor is called here

  copiedTea.printTeaInfo();

  return 0;
}