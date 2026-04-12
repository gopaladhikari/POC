// Prototype Inheritence

function Animal(name) {
  this.name = name;
}

Animal.prototype.makeSound = function () {
  console.log("The animal name is: ", this.name);
};

const dog = new Animal("Dog");
dog.makeSound();
