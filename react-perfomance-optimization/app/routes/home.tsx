import { ProfileCardWrapper } from "~/components/profile-card-wrapper";
import { SearchUsers } from "~/components/search-users";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Memoization" },
    {
      name: "description",
      content: "React Perfomce Optimization using Memoization",
    },
  ];
}

export default function Home() {
  return (
    <div>
      <ProfileCardWrapper />
      <SearchUsers />
    </div>
  );
}
