#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

class CustomError : public std::exception
{
private:
  string message;
  int error;

public:
  CustomError(const string &msg, const int err) : message(msg), error(err) {}

  const char *what() const noexcept override
  {
    return message.c_str();
  }

  int error() const noexcept
  {
    return error;
  }
};

int main()
{
  try
  {
    throw CustomError("This is a custom error message.", 500);
  }
  catch (const CustomError &e)
  {
    cout << "Caught CustomError: " << e.what() << endl;
    cout << "Error Code: " << e.error() << endl;
  }
  catch (const std::exception &e)
  {
    cout << "Caught std::exception: " << e.what() << endl;
  }

  return 0;
}