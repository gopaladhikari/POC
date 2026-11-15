#include <iostream>
#include <stdexcept>

using namespace std;

double calculatePositionSize(double accountBalance, double riskPercentage, double stopLossDistance)
{
  if (accountBalance <= 0)
    throw invalid_argument("Account balance must be greater than zero.");
  if (riskPercentage <= 0 || riskPercentage > 100)
    throw invalid_argument("Risk percentage must be between 0 and 100.");
  if (stopLossDistance <= 0)
    throw invalid_argument("Stop loss distance must be greater than zero.");

  double riskAmount = accountBalance * (riskPercentage / 100.0);

  double positionSize = riskAmount / (stopLossDistance);

  return positionSize;
}

int main()
{
  double accountBalance = 10000.0; // Example account balance
  double riskPercentage = 0.0;     // Example risk percentage
  double stopLossDistance = 50.0;  // Example stop loss distance

  try
  {
    double positionSize = calculatePositionSize(accountBalance, riskPercentage, stopLossDistance);
    cout << "Calculated Position Size: " << positionSize << endl;
  }
  catch (const invalid_argument &e)
  {
    cout << "Error: " << e.what() << endl;
  }

  return 0;
}