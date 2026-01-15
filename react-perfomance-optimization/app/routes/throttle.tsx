import { useEffect, useRef, useState } from "react";
import type { Route } from "./+types/throttle";
import { useThrottle } from "~/hooks/use-throttlle";

export const meta: Route.MetaFunction = () => {
  return [
    { title: "Thhrottle" },
    {
      name: "description",
      content: "React Perfomce Optimization using Throttle",
    },
  ];
};

export default function Page() {
  const [scrollY, setScrollY] = useState(0);

  const throttledScrollY = useThrottle(scrollY, 3000);

  const renders = useRef(0);
  renders.current++;

  useEffect(() => {
    const handleScrollY = () => {
      setScrollY(window.scrollY);
    };

    window.addEventListener("scroll", handleScrollY);

    return () => {
      window.removeEventListener("scroll", handleScrollY);
    };
  }, [scrollY]);

  return (
    <div className="relative">
      <p className="sticky inset-0 text-xl font-bold">
        Scroll Y: {scrollY} <br />
        Throttled Y: {throttledScrollY}
      </p>
      <p>Render count: {renders.current}</p>

      <div className="w-full h-screen bg-red-300"></div>
      <div className="w-full h-screen bg-red-300"></div>
      <div className="w-full h-screen bg-red-300"></div>
      <div className="w-full h-screen bg-red-300"></div>
      <div className="w-full h-screen bg-red-300"></div>
      <div className="w-full h-screen bg-red-300"></div>
    </div>
  );
}
