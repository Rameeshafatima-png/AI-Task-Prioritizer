
from langgraph.graph import StateGraph, START, END
from nodes import (
    TaskState,
    extract_tasks,
    prioritize_tasks,
    format_tasks,
)


def build_graph():
    workflow = StateGraph(TaskState)

    workflow.add_node("extract_tasks", extract_tasks)
    workflow.add_node("prioritize_tasks", prioritize_tasks)
    workflow.add_node("format_tasks", format_tasks)

    workflow.add_edge(START, "extract_tasks")
    workflow.add_edge("extract_tasks", "prioritize_tasks")
    workflow.add_edge("prioritize_tasks", "format_tasks")
    workflow.add_edge("format_tasks", END)

    return workflow.compile()
