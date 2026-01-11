import { SearchUsers } from "~/components/search-users";
import type { Route } from "./+types/debounce";
import { useEffect, useState } from "react";
import { useDebounce } from "~/hooks/use-debounce";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Debounce" },
    {
      name: "description",
      content: "React Perfomce Optimization using Debounce",
    },
  ];
}

export default function Debounce() {
  const [value, setValue] = useState("");

  const debounceQuery = useDebounce(value);

  useEffect(() => {
    console.log("Debounced value", debounceQuery);
  }, [debounceQuery]);

  return (
    <div className="border max-w-3xl mx-auto mt-20 p-10 rounded-2xl space-y-4">
      <h1>React Perfomance Optimzation using Debounce</h1>
      <input
        type="text"
        value={value}
        className="border w-full rounded-xl h-10 px-3"
        onChange={(e) => setValue(e.target.value)}
      />
      <SearchUsers query={debounceQuery} />
    </div>
  );
}
