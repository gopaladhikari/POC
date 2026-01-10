import { initialState, type States } from "@/hooks/useForm";

type Action<T = unknown> =
  | { type: "PENDING" }
  | { type: "RESOLVED"; payload: T }
  | { type: "REJECTED"; payload: Error }
  | { type: "CUSTOM"; payload: States<T> }
  | { type: "RESET" };

export function reducer<T>(
  state: States<T>,
  action: Action<T>
): States<T> {
  switch (action.type) {
    case "PENDING":
      return { ...state, data: null, isLoading: true, error: null };

    case "REJECTED":
      return {
        ...state,
        data: null,
        isLoading: false,
        error: action.payload,
      };

    case "RESOLVED":
      return {
        ...state,
        data: action.payload,
        isLoading: false,
        error: null,
      };

    case "RESET":
      return initialState as States<T>;

    default:
      return state;
  }
}
