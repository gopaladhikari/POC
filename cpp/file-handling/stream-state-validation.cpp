#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct TradeRecord
{
  int id;
  double price;
  double volume;
};

int main()
{
  string filename = "trades.bin";

  ofstream outFile(filename, ios::binary);

  if (!outFile)
  {
    cerr << "Failed to open output file.\n";
    return 1;
  }

  vector<TradeRecord> trades = {
      {101, 45000.50, 1.5},
      {102, 45100.25, 2.0},
      {103, 44950.00, 0.5}};

  cout << "Writing binary data to disk...\n";

  for (const auto &trade : trades)
  {

    outFile.write(reinterpret_cast<const char *>(&trade), sizeof(TradeRecord));
  }

  outFile.close();

  ifstream inFile(filename, ios::binary);

  if (!inFile)
  {
    cerr << "Failed to open input file.\n";
    return 1;
  }

  cout << "\nReading binary data from disk...\n";
  TradeRecord tempTrade;

  while (true)
  {

    inFile.read(reinterpret_cast<char *>(&tempTrade), sizeof(TradeRecord));

    if (!inFile)
    {
      if (inFile.eof())
      {
        cout << "-> Successfully reached the end of the binary file.\n";
      }
      else if (inFile.bad())
      {
        cerr << "-> Fatal hardware error: Stream corrupted.\n";
      }
      else if (inFile.fail())
      {
        cerr << "-> Logical error: File truncated or memory mismatch.\n";
      }
      break;
    }

    cout << "Read Trade ID: " << tempTrade.id
         << " | Price: $" << tempTrade.price
         << " | Volume: " << tempTrade.volume << "\n";
  }

  return 0;
}
