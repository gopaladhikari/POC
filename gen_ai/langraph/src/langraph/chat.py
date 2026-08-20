from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model="gpt-4.1-mini", model_provider="openai")


class State(TypedDict):
    message: Annotated[list, add_messages]


def chat(state: State) -> State:
    res = llm.invoke(state.get("message"))

    return {"message": [res]}


graph_builder = StateGraph(State)


graph_builder.add_node("chat", chat)


graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", END)


graph = graph_builder.compile()

updated_graph = graph.invoke(State({"message": ["Hi, My name is gopuadks."]}))

print(updated_graph)
