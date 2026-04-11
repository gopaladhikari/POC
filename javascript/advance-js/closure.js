// Closures are the function that remember the environment in which it was created.

function outer() {
  let counter = 4;
  return function inner() {
    counter++;
    return counter;
  };
}

const increment = outer();

console.log(increment());
console.log(increment());
console.log(increment());
console.log(increment());
