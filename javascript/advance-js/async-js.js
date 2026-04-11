console.log("hello world");

function sayHello() {
  console.log("hello");
}

setTimeout(() => {
  sayHello();
}, 1000);

for (let index = 0; index < 10; index++) {
  console.log(index);
}
