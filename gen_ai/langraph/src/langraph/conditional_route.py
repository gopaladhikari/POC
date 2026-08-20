from typing_extensions import TypedDict, NotRequired
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

load_dotenv()

openai_client = OpenAI()
google_client = genai.Client()


class State(TypedDict):
    user_query: str
    llm_output: NotRequired[Optional[str]]
    is_good: NotRequired[Optional[bool]]


def openai_chatbot(state: State) -> State:
    res = openai_client.responses.create(
        model="gpt-4.1-mini",
        input=state.get("user_query"),
    )

    state["llm_output"] = res.output_text

    return state


def google_chatbot(state: State) -> State:
    res = google_client.interactions.create(
        model="gemini-3.7-flash",
        input=state.get("user_query"),
    )

    state["llm_output"] = res.output_text

    return state


def end_node(state: State) -> State:
    return state


def evaluate_response(state: State) -> Literal["end_node", "google_chatbot"]:
    if state.get("is_good"):
        return "end_node"
    return "google_chatbot"


graph_builder = StateGraph(State)


# Nodes
graph_builder.add_node("openai_chatbot", openai_chatbot)
graph_builder.add_node("google_chatbot", google_chatbot)
graph_builder.add_node("end_node", end_node)

# Edges
graph_builder.add_edge(START, "openai_chatbot")

# Conditional Edge
graph_builder.add_conditional_edges("openai_chatbot", evaluate_response)

# Edges
graph_builder.add_edge("google_chatbot", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()

updated_graph = graph.invoke(State({"user_query": "Hey, what is 2+2?"}))

print(updated_graph)
