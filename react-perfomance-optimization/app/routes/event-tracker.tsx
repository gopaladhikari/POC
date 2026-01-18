import { useState } from "react";
import type { Route } from "./+types/event-tracker";

export const meta: Route.MetaFunction = () => {
  return [
    { title: "Memoization" },
    {
      name: "description",
      content: "React Perfomce Optimization using Memoization",
    },
  ];
};

export default function Page() {
  const [events, setEvents] = useState([
    {
      id: 1,
      name: "onChange",
      count: 0,
    },
    {
      id: 2,
      name: "onClick",
      count: 0,
    },
    {
      id: 3,
      name: "onSubmit",
      count: 0,
    },
  ]);

  const handleEvent = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setEvents((prev) => {
      const event = events.find((event) => event.name === "onSubmit");

      if (!event) return prev;

      const newEvent = events.map((event) => {
        if (event.name === "onSubmit")
          return { ...event, count: event.count + 1 };

        return event;
      });

      return newEvent;
    });
  };

  const handleClick = () => {
    setEvents((prev) => {
      const event = events.find((event) => event.name === "onClick");

      if (!event) return prev;

      const newEvent = events.map((event) => {
        if (event.name === "onClick")
          return { ...event, count: event.count + 1 };

        return event;
      });

      return newEvent;
    });
  };

  return (
    <>
      <div className="space-y-4">
        {events.map((event) => (
          <div key={event.id}>
            <p>{event.name}</p>
            <p>{event.count}</p>
          </div>
        ))}
      </div>
      <form action="" onSubmit={handleEvent} onClick={handleClick}>
        <input
          type="text"
          onChange={() => {
            setEvents((prev) =>
              prev.map((event) => {
                if (event.name === "onChange")
                  return { ...event, count: event.count + 1 };

                return event;
              })
            );
          }}
        />
      </form>
    </>
  );
}
