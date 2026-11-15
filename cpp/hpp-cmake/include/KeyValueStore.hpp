#pragma once

#include <string>
#include <unordered_map>
#include <optional>

class KeyValueStore
{
private:
  std::unordered_map<std::string, std::string> store_;

public:
  void set(const std::string &key, const std::string &value);

  std::optional<std::string> get(const std::string &key) const;

  bool remove(const std::string &key);

  std::size_t size() const noexcept;
};