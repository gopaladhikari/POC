import type { Route } from "./+types/home";
import { formatDate } from "@repo/utils";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App" },
    { name: "description", content: "Welcome to React Router!" },
  ];
}

export default function Home() {
  return <p>{formatDate(new Date())}</p>;
}
