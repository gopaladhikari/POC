import { ProfileCardWrapper } from "~/components/profile-card-wrapper";
import type { Route } from "./+types/home";

export const meta: Route.MetaFunction = () => {
  return [
    { title: "Memoization" },
    {
      name: "description",
      content: "React Perfomce Optimization using Memoization",
    },
  ];
};

export default function Home() {
  return (
    <div>
      <ProfileCardWrapper />
    </div>
  );
}
