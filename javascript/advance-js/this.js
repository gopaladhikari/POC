const person = {
  name: "John",
  age: 30,
  sayHi: function () {
    console.log("Hi, my name is " + this.name);
  },
};

person.sayHi();

const sayHi = person.sayHi.bind({ name: "Gopal" });

sayHi();

// bind, apply and call
