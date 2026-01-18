import {
  type RouteConfig,
  index,
  route,
} from "@react-router/dev/routes";

const routes: RouteConfig = [
  index("routes/home.tsx"),
  route("debounce", "./routes/debounce.tsx"),
  route("throttle", "./routes/throttle.tsx"),
  route("event-tracker", "./routes/event-tracker.tsx"),
];

export default routes;
