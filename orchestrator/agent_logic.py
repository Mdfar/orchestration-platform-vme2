from typing import TypedDict, List, Annotated from langgraph.graph import StateGraph, END import operator

class AgentState(TypedDict): messages: Annotated[List[str], operator.add] next_step: str is_verified: bool context: dict

def reasoning_agent(state: AgentState): # Logic for LLM to plan the task return {"messages": ["Plan generated"], "next_step": "tool_execution"}

def verification_agent(state: AgentState): # Logic to detect hallucinations or schema errors last_msg = state['messages'][-1] is_valid = "Plan" in last_msg # Simplified check return {"is_verified": is_valid}

workflow = StateGraph(AgentState) workflow.add_node("reasoning", reasoning_agent) workflow.add_node("verifier", verification_agent)

workflow.set_entry_point("reasoning") workflow.add_edge("reasoning", "verifier")

def router(state): if state["is_verified"]: return END return "reasoning"

workflow.add_conditional_edges("verifier", router) app = workflow.compile()