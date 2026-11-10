#include <iostream>
#include <vector>

using namespace std;

class Chai
{
public:
  // attributes
  string teaName;
  int serving;
  vector<string> ingredients;

  // methods

  void displayDetails()
  {
    cout << "Tea Name: " << teaName << endl;
    cout << "Serving: " << serving << endl;

    for (string ingredient : ingredients)
    {
      cout << "Ingredient: " << ingredient << endl;
    }
  }
};

int main()
{

  Chai myChai;

  myChai.teaName = "Lemon Tea";
  myChai.serving = 2;
  myChai.ingredients = {"Water", "Tea Leaves", "Lemon", "Sugar"};

  myChai.displayDetails();

  return 0;
}
