#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <string>

using namespace std;

struct Employee
{
  int id;
  string name;
  double salary;

  Employee(int i, string n, double s) : id(i), name(n), salary(s) {}
};

void printEmployees(const Employee &employee)
{
  cout << "ID: " << employee.id << ", Name: " << employee.name << ", Salary: " << employee.salary << endl;
}

int main()
{
  vector<Employee> employees = {
      Employee(1, "Alice", 50000),
      Employee(2, "Bob", 60000),
      Employee(3, "Charlie", 55000),
      Employee(4, "David", 70000),
      Employee(5, "Eve", 65000)};

  sort(employees.begin(), employees.end(), [](const Employee &a, const Employee &b)
       { return a.salary < b.salary; });

  cout << "Employees sorted by salary highest -> lowest:" << endl;

  for_each(employees.begin(), employees.end(), printEmployees);

  vector<Employee> highEarners;

  copy_if(
      employees.begin(),
      employees.end(),
      back_inserter(highEarners),
      [](const Employee &e)
      {
        return e.salary > 60000;
      });

  cout << "\nEmployees with salary greater than 60000:" << endl;

  for_each(highEarners.begin(), highEarners.end(), printEmployees);

  double totalSalary = accumulate(
      employees.begin(),
      employees.end(),
      0.0,
      [](double total, const Employee &e)
      {
        return total + e.salary;
      });

  cout << "\nTotal salary of all employees: " << totalSalary << endl;

  return 0;
}