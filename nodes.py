
import os
from typing import TypedDict

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY missing. Add it to your project's .env file."
    )


# -------------------- DATA MODELS --------------------

class ExtractedTask(BaseModel):
    title: str = Field(description="Short, clear task name")
    deadline: str = Field(
        description="Deadline stated by the user, or Not specified"
    )


class ExtractedTasks(BaseModel):
    tasks: list[ExtractedTask]


class PrioritizedTask(BaseModel):
    title: str
    deadline: str
    priority: str = Field(
        description="One of High, Medium, or Low"
    )
    reason: str = Field(
        description="Brief explanation for the assigned priority"
    )


class PrioritizedTasks(BaseModel):
    tasks: list[PrioritizedTask]


class TaskState(TypedDict, total=False):
    user_input: str
    tasks: list[dict]
    formatted_output: str


# -------------------- GROQ MODEL --------------------

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0,
    max_retries=2,
)


# -------------------- NODE 1: EXTRACT TASKS --------------------

def extract_tasks(state: TaskState):
    structured_llm = llm.with_structured_output(ExtractedTasks)

    result = structured_llm.invoke([
        (
            "system",
            "Extract every actionable task from the user's message. "
            "Preserve deadlines as stated. Do not invent dates. "
            "If no deadline is mentioned, use 'Not specified'. "
            "Return an empty task list if no actionable tasks exist."
        ),
        ("human", state["user_input"]),
    ])

    return {
        "tasks": [
            task.model_dump()
            for task in result.tasks
        ]
    }


# -------------------- NODE 2: PRIORITIZE TASKS --------------------

def prioritize_tasks(state: TaskState):
    tasks = state.get("tasks", [])

    if not tasks:
        return {"tasks": []}

    structured_llm = llm.with_structured_output(PrioritizedTasks)

    result = structured_llm.invoke([
        (
            "system",
            "You are a task prioritization assistant. "
            "Assign each task High, Medium, or Low priority. "
            "Consider deadlines, urgency, and importance. "
            "High means urgent or important, Medium means moderately "
            "important, and Low means less urgent. "
            "Preserve every task title and deadline exactly. "
            "Do not invent deadlines. Provide a short reason for each "
            "priority. Return one result for every input task."
        ),
        (
            "human",
            f"Original user message:\n{state['user_input']}\n\n"
            f"Tasks to prioritize:\n{tasks}"
        ),
    ])

    # Normalize priorities before returning state.
    normalized_tasks = []

    for task in result.tasks:
        item = task.model_dump()
        priority = str(item.get("priority", "Medium")).capitalize()

        if priority not in {"High", "Medium", "Low"}:
            priority = "Medium"

        item["priority"] = priority
        normalized_tasks.append(item)

    return {"tasks": normalized_tasks}


# -------------------- NODE 3: FORMAT RESULTS --------------------

def format_tasks(state: TaskState):
    tasks = state.get("tasks", [])

    if not tasks:
        return {
            "formatted_output": (
                "No actionable tasks were found. "
                "Please describe the things you need to do."
            )
        }

    lines = [
        "YOUR ORGANIZED TO-DO LIST",
        "=" * 28,
        "",
    ]

    for index, task in enumerate(tasks, start=1):
        lines.extend([
            f"{index}. {task['title']}",
            f"   Deadline: {task['deadline']}",
            f"   Priority: {task['priority']}",
            f"   Reason: {task['reason']}",
            "",
        ])

    return {"formatted_output": "\n".join(lines)}
