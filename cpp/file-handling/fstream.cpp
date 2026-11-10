#include <fstream>
#include <iostream>

using namespace std;

int main()
{
  string line;
  // Create an output file stream
  ofstream out("sample.txt");

  out << "Hello, World!" << endl;

  ifstream in("sample.txt");
  in >> line;

  cout << line << endl;

  getline(in, line);

  cout << line << endl;

  return 0;
}