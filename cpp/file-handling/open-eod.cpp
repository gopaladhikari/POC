#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ofstream outFile;
  outFile.open("sample.txt");

  if (!outFile)
  {
    cerr << "Error opening file for writing." << endl;
    return 1;
  }

  outFile << "Hello, World!" << endl;

  outFile.close();
  return 0;
}