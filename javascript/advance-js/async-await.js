function fetchUserData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;
      if (success) resolve("hello world");
      else reject("Promise rejected");
    }, 1000);
  });
}
async function fetchData() {
  const userData = await fetchUserData();
  console.log(userData);
}

fetchData();
