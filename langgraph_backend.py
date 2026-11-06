from langgraph.graph import StateGraph,START,END
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama 
from langchain_core.messages import BaseMessage,HumanMessage
# from dotenv import load_dotenv
from typing import  TypedDict, Annotated
from pydantic import BaseModel,Field
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

llm = ChatOllama(
    model="qwen2.5:latest"
)


class Chatstate(TypedDict):

    messages : Annotated[list[BaseMessage],add_messages]

def chat_node(state: Chatstate):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}

checkpointer = MemorySaver()

graph = StateGraph(Chatstate)

#add node 
graph.add_node('chat_node',chat_node)

#add edge
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)