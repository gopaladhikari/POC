#include <string>
#include <exception>
#include <iostream>

using namespace std;

struct ErrorInfo
{
  string message;
  int statusCode;
  string description;
};

class OrderRejectionError : public exception
{
private:
  ErrorInfo errorInfo;

public:
  OrderRejectionError(const ErrorInfo &info) : errorInfo(info) {}

  const char *what() const noexcept override
  {
    return errorInfo.message.c_str();
  }

  const ErrorInfo &getErrorInfo() const noexcept
  {
    return errorInfo;
  }
};

int main()
{
  ErrorInfo err = {"Order Rejected", 500, "Insufficient inventory to fulfill request"};

  try
  {
    throw OrderRejectionError(err);
  }
  catch (const OrderRejectionError &e)
  {
    const ErrorInfo &info = e.getErrorInfo();
    cout << "Error: " << e.what() << "\n"
         << "Status Code: " << info.statusCode << "\n"
         << "Description: " << info.description << endl;
  }

  catch (const std::exception &e)
  {
    cout << "Standard exception: " << e.what() << endl;
  }

  return 0;
}