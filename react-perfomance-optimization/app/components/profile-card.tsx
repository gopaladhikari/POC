import { useRef, memo } from "react";

type Props = {
  data: {
    name: string;
    age: number;
    email: string;
    address: string;
  };

  todos: {
    id: number;
    title: string;
    completed: boolean;
  }[];

  handleDeleteTodo: (id: number) => void;

  handleToggleTodoCompleted: (id: number) => void;
};

function profileCard({
  data,
  todos,
  handleDeleteTodo,
  handleToggleTodoCompleted,
}: Props) {
  const renders = useRef(0);
  renders.current++;

  return (
    <div>
      <p>
        Hello {data.name}! I'm a profile card. I've been rendered{" "}
      </p>
      <p>Render count: {renders.current}</p>
      <p>Age: {data.age}</p>
      <p>Email: {data.email}</p>
      <p>Address: {data.address}</p>

      <h2 className="border-t py-4 mt-4 text-2xl font-semibold">
        Todos
      </h2>

      <div className="space-y-4">
        {todos.map((todo) => (
          <div
            key={todo.id}
            className="flex justify-between bg-stone-900 p-4 rounded-2xl"
          >
            <p>{todo.title}</p>
            <p className="text-sm">{todo.completed ? "✅" : "❌"}</p>

            <div className="text-sm space-x-6">
              <button
                className="bg-red-700 p-2 rounded-2xl"
                onClick={() => handleDeleteTodo(todo.id)}
              >
                Delete
              </button>
              <button
                onClick={() => handleToggleTodoCompleted(todo.id)}
                className={
                  todo.completed
                    ? "bg-green-500 p-2 rounded-2xl"
                    : "bg-orange-500 p-2 rounded-2xl"
                }
              >
                Mark as {todo.completed ? "incomplete" : "complete"}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export const ProfileCard = memo(profileCard);
