#include <iostream>

using namespace std;

using RiskModel = double (*)(double, double);

double fixedFractional(double balance, double stopDistance)
{
  // calculate position size on 1% risk per trade.
  double riskPercentage = 0.01;

  double riskAmount = balance * riskPercentage;

  return riskAmount / stopDistance; // position size based on stop distance
}

double conservativeQuant(double balance, double stopDistance)
{
  // calculate position size on 0.05% risk per trade.
  double riskPercentage = 0.0005;

  double riskAmount = balance * riskPercentage;

  return riskAmount / stopDistance; // position size based on stop distance
}

double executeRiskCheck(RiskModel riskModel, double balance, double stopDistance)
{
  return riskModel(balance, stopDistance);
}

int main()
{
  double balance = 1000.0;

  double stopDistance = 50.0;

  double positionSize1 = executeRiskCheck(fixedFractional, balance, stopDistance);
  cout << "Position size using fixed fractional model: " << positionSize1 << endl;

  double positionSize2 = executeRiskCheck(conservativeQuant, balance, stopDistance);
  cout << "Position size using conservative quant model: " << positionSize2 << endl;

  return 0;
}