#include "../include/KeyValueStore.hpp"

void KeyValueStore::set(const std::string &key, const std::string &value)
{
  store_[key] = value;
}

std::optional<std::string> KeyValueStore::get(const std::string &key) const
{
  auto it = store_.find(key);
  if (it != store_.end())
  {
    return it->second;
  }
  return std::nullopt; // Clean way to represent "key not found" in C++17/20
}

bool KeyValueStore::remove(const std::string &key)
{
  return store_.erase(key) > 0;
}

std::size_t KeyValueStore::size() const noexcept
{
  return store_.size();
}