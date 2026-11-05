#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <ctime>
#include <deque>
#include <unordered_set>
#include <unordered_map>

using namespace std;

struct User
{
  int id;
  string userName;
  string email;
};

struct Product
{
  int id;
  string productName;
  string category;
};

struct Order
{
  int id;
  int productId;
  int quantity;
  int userId;
  time_t orderDate;
};

int main()
{

  vector<Product> products = {
      {1, "Laptop", "Electronics"},
      {2, "Smartphone", "Electronics"},
      {3, "Headphones", "Electronics"},
      {4, "Shoes", "Fashion"},
      {5, "T-shirt", "Fashion"}};

  vector<User> users = {
      {1, "Alice", "alice@example.com"},
      {2, "Bob", "bob@example.com"}};

  deque<string> recentCustomer = {"Alice", "Bob", "Charlie"};

  list<Order> orderHistory;

  orderHistory.push_back({1, 1, 1, 1, time(0)});
  orderHistory.push_back({2, 2, 2, 2, time(0)});

  set<string> categories;

  for (const auto &product : products)
  {
    categories.insert(product.category);
  }

  map<int, int> productStock = {
      {1, 10},
      {2, 20},
      {3, 15},
      {4, 5},
      {5, 30}};

  multimap<int, Order> customerOrders;

  for (const auto &order : orderHistory)
  {
    customerOrders.insert({order.userId, order});
  }

  unordered_map<int, User> userMap = {
      {1, {1, "Alice", "alice@example.com"}},
      {2, {2, "Bob", "bob@example.com"}}};

  unordered_set<string> uniqueEmails = {
      "alice@example.com",
      "bob@example.com"};

  cout << "Products in the store:" << endl;
  return 0;
}