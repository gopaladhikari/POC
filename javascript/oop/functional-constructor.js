function Person(name, age) {
  this.name = name;
  this.age = age;
}

function Car(model, year) {
  this.model = model;
  this.year = year;
}

const gopal = new Person("gopal", 25);
const tesla = new Car("tesla", 2020);

console.log(tesla.model);
console.log(tesla.year);

function animal(species) {
  this.species = species;
}

animal.prototype.makeSound = function () {
  console.log(this.species);
};

const cat = new animal("cat");
cat.makeSound();
