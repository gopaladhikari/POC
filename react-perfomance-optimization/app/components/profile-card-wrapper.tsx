import { useMemo, useState, useCallback } from "react";
import { ProfileCard } from "./profile-card";

export function ProfileCardWrapper() {
  const [value, setValue] = useState("");

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

  const data = useMemo(
    () => ({
      name: "John Doe",
      age: 30,
      email: "john@example.com",
      address: "123 Main St, Anytown, USA",
    }),
    []
  );

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
    <div className="space-y-4">
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <ProfileCard
        data={data}
        todos={todos}
        handleDeleteTodo={handleDeleteTodo}
        handleToggleTodoCompleted={handleToggleTodoCompleted}
      />
    </div>
  );
}
