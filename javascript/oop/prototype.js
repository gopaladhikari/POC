const computer = {
  cpu: 12,
  ram: 8,
  screen: 16,
  os: "windows",
};

const lenovo = {
  cpu: 12,
  ram: 8,
  screen: 16,
  os: "windows",
};

const macbook = {};

Object.setPrototypeOf(macbook, computer);

console.log("computers", computer.__proto__);
console.log("macbook", macbook.__proto__);

console.log("macbook cpu", Object.getPrototypeOf(macbook));
