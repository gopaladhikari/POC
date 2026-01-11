import {
  type RouteConfig,
  index,
  route,
} from "@react-router/dev/routes";

const routes: RouteConfig = [
  index("routes/home.tsx"),
  route("debounce", "./routes/debounce.tsx"),
];

export default routes;
