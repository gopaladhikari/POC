import { NavLink } from "react-router";

export function Nav() {
  return (
    <header>
      <nav className="max-w-3xl mx-auto bg-stone-700 p-4 mt-4 rounded-2xl">
        <ul className="flex gap-6">
          <li>
            <NavLink
              to="/"
              className={({ isActive }) => {
                return isActive ? "text-blue-500" : "text-stone-300";
              }}
            >
              Home
            </NavLink>
          </li>

          <li>
            <NavLink
              to="/debounce"
              className={({ isActive }) => {
                return isActive ? "text-blue-500" : "text-stone-300";
              }}
            >
              Debounce
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/throttle"
              className={({ isActive }) => {
                return isActive ? "text-blue-500" : "text-stone-300";
              }}
            >
              Throttle
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/event-tracker"
              className={({ isActive }) => {
                return isActive ? "text-blue-500" : "text-stone-300";
              }}
            >
              Event Tracker
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
}
