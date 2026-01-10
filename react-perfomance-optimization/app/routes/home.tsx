import { useMemo, useState, useCallback } from "react";
import type { Route } from "./+types/home";
import { ProfileCard } from "~/components/profile-card";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "React Perfomce Optimization" },
    { name: "description", content: "React Perfomce Optimization" },
  ];
}

export default function Home() {
  const [value, setValue] = useState("");

  const [data, setData] = useState({
    name: "Gopal Adhikari",
    age: 25,
    email: "gopaladhikari@gmail.com",
    address: "Bangalore",
  });

  const [todos, setTodos] = useState([
    {
      id: 1,
      title: "Learn React",
      completed: false,
    },
    {
      id: 2,
      title: "Learn Next.js",
      completed: false,
    },
    {
      id: 3,
      title: "Learn Tailwind",
      completed: false,
    },
  ]);

  const userData = useMemo(() => {
    return data;
  }, []);

  const userTodo = useMemo(() => {
    return todos;
  }, [todos]);

  const handleDeleteTodo = useCallback((id: number) => {
    setTodos((prev) => prev.filter((todo) => todo.id !== id));
  }, []);

  const handleToggleTodoCompleted = useCallback((id: number) => {
    setTodos((prev) =>
      prev.map((todo) => {
        if (todo.id === id)
          return { ...todo, completed: !todo.completed };

        return todo;
      })
    );
  }, []);

  return (
    <div className="border max-w-3xl mx-auto mt-20 p-10 rounded-2xl space-y-4">
      <input
        type="text"
        value={value}
        className="border w-full rounded-xl h-10 px-3"
        onChange={(e) => setValue(e.target.value)}
      />

      <ProfileCard
        data={userData}
        todos={userTodo}
        handleDeleteTodo={handleDeleteTodo}
        handleToggleTodoCompleted={handleToggleTodoCompleted}
      />
    </div>
  );
}
