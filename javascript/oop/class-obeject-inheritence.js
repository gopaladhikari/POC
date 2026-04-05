let car = {
  make: "toyota",
  model: "prius",
  start: function () {
    return `${this.make} ${this.model} started`;
  },
}; // object literal

console.log(car.start());

function Person(name, age) {
  this.name = name;
  this.age = age;
}

const gopal = new Person("John", 25);

console.log(gopal.name);
console.log(gopal.age);

function Animal(species) {
  this.species = species;
}

Animal.prototype.makeSound = function () {
  return `${this.species} makes a sound`;
};

Array.prototype.getDataset = function () {
  return `Datas are ${this}`;
};

const marks = [1, 3, 7];

console.log(marks.getDataset());

class Vehicle {
  constructor(model, year) {
    this.model = model;
    this.year = year;
  }

  honk() {
    return `${this.model} honks`;
  }
}

class Car extends Vehicle {
  drive() {
    return `${this.model} drives and this is an example of inheritance`;
  }
}

const tesla = new Car("tesla", 2020);

console.log(tesla.honk());
console.log(tesla.drive());

const vehicle1 = new Vehicle("tesla", 2020);
const vehicle2 = new Vehicle("toyota", 2020);

console.log(vehicle1.honk());
console.log(vehicle2.honk());
