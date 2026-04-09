// Encapsulation Polymorhism Abstract Getter and Setter

// Encapsulation
class Bank {
  #balance = 0;

  deposit(amount) {
    this.#balance += amount;
    return this.#balance;
  }

  getBalance() {
    return `$ ${this.#balance}`;
  }
}

const account = new Bank();
account.deposit(100);

console.log(account.getBalance());

// Abstraction

class CoffeeMachine {
  start() {
    // call db
    // filter
    return "Searchhing";
  }
  stop() {
    // complex logic
    return "Stopping";
  }

  brewCoffee() {
    const message = this.start();
    const result = this.stop();
    return `${message} \n${result}`;
  }
}

const myMachine = new CoffeeMachine();

// console.log(myMachine.start());
console.log(myMachine.brewCoffee());

// Polymorphism

class Bird {
  fly() {
    return "I'm flying";
  }
}

class Penguin extends Bird {
  fly() {
    return "Penguin can't fly";
  }
}

const bird = new Bird();
const penguin = new Penguin();

console.log(bird.fly());
console.log(penguin.fly());

// Static

class Calculator {
  age = 20;
  static address = "123 Main Street";
  static add(a, b) {
    return a + b;
  }
}

// const calc = new Calculator();
// console.log(calc.add(10, 20));

console.log(Calculator.add(10, 20));

// Getter and Setter

class Employee {
  #salary;

  constructor(name, salary) {
    this.name = name;
    this.#salary = salary;
  }

  get salary() {
    return "You cannot get salary";
  }

  set salary(value) {
    if (value < 0) return "You cannot set negative salary";

    this.salary = value;
  }
}

let employee = new Employee("John", -1000);

console.log(employee.salary);
