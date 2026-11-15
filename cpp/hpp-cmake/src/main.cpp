#include <iostream>
#include "../include/KeyValueStore.hpp"

int main()
{
  KeyValueStore db;

  db.set("city", "Vilnius");
  db.set("role", "Quant Dev");

  if (auto val = db.get("city"))
  {
    std::cout << "Found city: " << *val << "\n";
  }

  if (!db.get("missing_key"))
  {
    std::cout << "missing_key -> (nil)\n";
  }

  std::cout << "Total keys in RAM: " << db.size() << "\n";

  return 0;
}