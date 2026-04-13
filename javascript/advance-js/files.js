const fs = require("fs");
const filePath = "./javascript/advance-js/tasks.json";

const command = process.argv[2];
const args = process.argv[3];

const loadTasks = () => {
  try {
    const dataBuffer = fs.readFileSync(filePath);
    const dataJson = dataBuffer.toString();
    return JSON.parse(dataJson);
  } catch (error) {
    console.error("loadtask error", error);
    return [];
  }
};

const saveTasks = (tasks) => {
  try {
    fs.writeFileSync(filePath, JSON.stringify(tasks));
  } catch (error) {
    console.error("savetask error", error);
  }
};

const addTask = (task) => {
  const tasks = loadTasks();
  tasks.push({ task });
  saveTasks(tasks);
  console.log("Task added", task);
};

const listTasks = () => {
  const tasks = loadTasks();
  tasks.forEach((task) => {
    console.log(task.task);
  });
};

const removeTask = (task) => {
  const tasks = loadTasks();
  const index = tasks.findIndex((task) => task.task === task);

  if (index !== -1) {
    tasks.splice(index, 1);
    saveTasks(tasks);
    console.log("Task removed", name);
  }
};

if (command === "add") addTask(args);
else if (command === "list") listTasks();
else if (command === "remove") removeTask(parseInt(args));
else console.log("Invalid command");
