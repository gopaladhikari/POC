// Prototypes: inheriting properties from parent objects

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

function User() {}

User.prototype.sayHi = function () {};

const gopal = new User();
const gopal2 = new User();

console.log("gopal", Object.getPrototypeOf(gopal));
console.log("gopal2", gopal2.__proto__);

function Car() {}

Car.prototype.honk = function (model) {
  this.model = model;

  console.log(this.model);
};

const toyota = new Car();
const tesla = new Car();

toyota.honk("toyota");
tesla.honk("tesla");

console.log(Car.prototype === Object.getPrototypeOf(toyota));
console.log(Car.prototype === Object.getPrototypeOf(tesla));
