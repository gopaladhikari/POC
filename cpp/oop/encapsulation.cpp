#include <iostream>

using namespace std;

class BankAccount
{
private:
  double balance;
  string accountNumber;

public:
  BankAccount(string accNum, double initialBalance)
  {
    accountNumber = accNum;
    balance = initialBalance;

    cout << "Bank account created" << endl;
    cout << "Account Number: " << accountNumber << ", Initial Balance: " << balance << endl;
  }

  void deposit(double amount)
  {
    if (amount > 0)
    {
      balance += amount;
      cout << "Deposited: " << amount << endl;
    }
    else
    {
      cout << "Deposit amount must be positive." << endl;
    }
  }

  void withdraw(double amount)
  {
    if (amount > 0 && amount <= balance)
    {
      balance -= amount;
      cout << "Withdrew: " << amount << endl;
    }
    else
    {
      cout << "Invalid withdrawal amount." << endl;
    }
  }

  double getBalance() const
  {
    return balance;
  }
};

int main()
{
  BankAccount account("123456", 1000.0);
  account.deposit(500.0);
  account.withdraw(200.0);
  cout << "Final balance: " << account.getBalance() << endl;
  return 0;
}