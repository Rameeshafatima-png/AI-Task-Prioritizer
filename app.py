
import html
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from graph import build_graph

load_dotenv()

st.set_page_config(
    page_title="TaskFlow AI | Workspace",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- DESIGN SYSTEM --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #182b32;
    --muted: #71828a;
    --teal: #087f73;
    --teal-light: #e3f5ef;
    --line: #e5eceb;
    --paper: #ffffff;
}

.stApp {
    background: #f5f8f7;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding: 2.2rem 2.5rem 3rem;
}

[data-testid="stSidebar"] {
    background: #173b3a;
}

[data-testid="stSidebar"] * {
    color: #f2faf7;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #d0e4df;
}

[data-testid="stSidebar"] hr {
    border-color: #41615d;
}

.brand {
    font-size: 1.55rem;
    font-weight: 800;
    letter-spacing: -0.8px;
    color: #ffffff;
}

.brand-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 34px;
    height: 34px;
    border-radius: 11px;
    background: #a7f3d0;
    color: #173b3a;
    margin-right: 8px;
    font-weight: 800;
}

.sidebar-note {
    color: #bdd3cd !important;
    font-size: 0.83rem;
    line-height: 1.7;
}

.eyebrow {
    color: #087f73;
    text-transform: uppercase;
    font-weight: 800;
    letter-spacing: 2px;
    font-size: 0.72rem;
    margin-bottom: 10px;
}

.page-title {
    font-size: clamp(2rem, 4vw, 2.8rem);
    font-weight: 800;
    letter-spacing: -1.7px;
    line-height: 1.15;
    color: #182b32;
    margin: 0;
}

.page-subtitle {
    font-size: 1rem;
    color: #71828a !important;
    line-height: 1.8;
    margin-top: 12px;
}

.top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 28px;
}

.workspace-tag {
    padding: 9px 14px;
    border-radius: 30px;
    background: #e3f5ef;
    color: #087f73;
    font-size: 0.8rem;
    font-weight: 700;
}

.panel {
    background: #ffffff;
    border: 1px solid #e5eceb;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 5px 20px rgba(24, 43, 50, 0.035);
}

.panel-heading {
    font-size: 1.13rem;
    font-weight: 800;
    color: #182b32;
    margin-bottom: 5px;
}

.panel-description {
    font-size: 0.87rem;
    color: #71828a !important;
    line-height: 1.7;
    margin-bottom: 16px;
}

.stTextArea textarea {
    background: #fbfdfc !important;
    color: #182b32 !important;
    border: 1px solid #dce7e4 !important;
    border-radius: 13px !important;
    padding: 15px !important;
    font-size: 0.96rem !important;
    line-height: 1.7 !important;
}

.stTextArea textarea:focus {
    border-color: #087f73 !important;
    box-shadow: 0 0 0 2px rgba(8, 127, 115, 0.12) !important;
}

.stTextArea textarea::placeholder {
    color: #9aa9a9 !important;
}

.stApp h1, .stApp h2, .stApp h3 {
    color: #182b32;
}

.stApp label {
    color: #354d52;
}

.stButton button {
    border-radius: 11px;
    min-height: 43px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton button[kind="primary"] {
    background: #087f73;
    color: #ffffff;
    border: 1px solid #087f73;
}

.stButton button[kind="primary"]:hover {
    background: #06685f;
    border-color: #06685f;
    color: #ffffff;
}

div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e5eceb;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(24, 43, 50, 0.025);
}

div[data-testid="stMetricLabel"] {
    color: #71828a !important;
}

div[data-testid="stMetricValue"] {
    color: #182b32 !important;
    font-weight: 800;
}

[data-testid="stDataFrame"] {
    border: 1px solid #e5eceb;
    border-radius: 13px;
    overflow: hidden;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #e3f5ef;
    color: #087f73;
    width: 31px;
    height: 31px;
    border-radius: 10px;
    font-weight: 800;
    margin-right: 9px;
}

.footer {
    color: #8a9a9b;
    font-size: 0.8rem;
    text-align: center;
    padding-top: 25px;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1.3rem 1rem 2rem;
    }

    .panel {
        padding: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- WORKFLOW --------------------

@st.cache_resource
def get_workflow():
    return build_graph()


# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown(
        '<div class="brand"><span class="brand-mark">✓</span>'
        'TaskFlow AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="sidebar-note">A calmer way to plan your day.</p>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Your workflow")

    st.markdown("""
    <p><span class="step-number">01</span> Extract tasks</p>
    <p><span class="step-number">02</span> Set priorities</p>
    <p><span class="step-number">03</span> Build your plan</p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Priority guide")

    st.markdown("""
    <p>🔴 <b>High</b><br>
    <span class="sidebar-note">Urgent or important</span></p>
    <p>🟡 <b>Medium</b><br>
    <span class="sidebar-note">Needs attention</span></p>
    <p>🟢 <b>Low</b><br>
    <span class="sidebar-note">Less urgent</span></p>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown(
        '<p class="sidebar-note">Powered by Groq and LangGraph</p>',
        unsafe_allow_html=True,
    )

    if st.button("Clear task results", use_container_width=True):
        st.session_state.pop("organized_tasks", None)
        st.session_state.pop("formatted_output", None)
        st.rerun()


# -------------------- HEADER --------------------

st.markdown("""
<div class="top-row">
    <div>
        <div class="eyebrow">YOUR PERSONAL WORKSPACE</div>
        <h1 class="page-title">Make room for what matters.</h1>
        <p class="page-subtitle">
            Capture your thoughts. Let AI turn them into an actionable plan.
        </p>
    </div>
    <div class="workspace-tag">AI POWERED PLANNING</div>
</div>
""", unsafe_allow_html=True)


# -------------------- TASK INPUT --------------------

st.markdown("""
<div class="panel">
    <div class="panel-heading">Create your task plan</div>
    <div class="panel-description">
        Write naturally. Include deadlines, upcoming events, and priorities.
    </div>
</div>
""", unsafe_allow_html=True)

example = (
    "Finish my AI assignment tomorrow, buy groceries today, "
    "and prepare for my Python interview on Friday."
)

left, right = st.columns([5, 1])

with left:
    st.markdown("**Your tasks**")

with right:
    if st.button("Load example", use_container_width=True):
        st.session_state["task_input"] = example

user_input = st.text_area(
    "Task description",
    key="task_input",
    height=155,
    label_visibility="collapsed",
    placeholder=(
        "For example: Finish my project by Friday, "
        "review my notes tomorrow, and call my teacher next week..."
    ),
)

st.caption(
    "Tip: Mention deadlines and urgency for more useful prioritization."
)

if st.button(
    "Organize my tasks  →",
    type="primary",
    use_container_width=True,
):
    if not user_input.strip():
        st.warning("Please enter a description of your tasks.")

    else:
        try:
            with st.spinner("Organizing your tasks with AI..."):
                workflow = get_workflow()

                result = workflow.invoke({
                    "user_input": user_input.strip(),
                    "tasks": [],
                    "formatted_output": "",
                })

                tasks = result.get("tasks", [])

                normalized = []

                for task in tasks:
                    priority = str(
                        task.get("priority", "Medium")
                    ).capitalize()

                    if priority not in {"High", "Medium", "Low"}:
                        priority = "Medium"

                    normalized.append({
                        "title": str(task.get("title", "Untitled task")),
                        "deadline": str(
                            task.get("deadline", "Not specified")
                        ),
                        "priority": priority,
                        "reason": str(
                            task.get("reason", "Not specified")
                        ),
                    })

                st.session_state["organized_tasks"] = normalized
                st.session_state["formatted_output"] = result.get(
                    "formatted_output", ""
                )

            if normalized:
                st.success(
                    f"Your plan is ready — {len(normalized)} tasks organized."
                )
            else:
                st.info("No actionable tasks were found in your message.")

        except Exception as exc:
            st.error("We couldn't organize your tasks.")

            message = str(exc).lower()

            if "429" in message or "rate_limit" in message:
                st.warning(
                    "Groq API rate limit reached. Please wait or check "
                    "your account limits at console.groq.com."
                )
            elif "401" in message or "authentication" in message:
                st.warning(
                    "Check your GROQ_API_KEY in the project's .env file."
                )

            with st.expander("Technical error details"):
                st.exception(exc)


# -------------------- RESULTS --------------------

tasks = st.session_state.get("organized_tasks", [])

if tasks:
    st.markdown("---")

    st.markdown("""
    <div class="eyebrow">YOUR ACTION PLAN</div>
    <h2 style="font-size:1.8rem; font-weight:800; letter-spacing:-0.7px;">
        Tasks at a glance
    </h2>
    <p style="color:#71828a;">
        Review your priorities and export your organized list.
    </p>
    """, unsafe_allow_html=True)

    high = sum(t["priority"] == "High" for t in tasks)
    medium = sum(t["priority"] == "Medium" for t in tasks)
    low = sum(t["priority"] == "Low" for t in tasks)

    a, b, c, d = st.columns(4)

    a.metric("Total tasks", len(tasks))
    b.metric("High priority", high)
    c.metric("Medium priority", medium)
    d.metric("Low priority", low)

    st.write("")

    # Priority filter
    filter_options = ["All tasks", "High", "Medium", "Low"]

    selected_filter = st.selectbox(
        "Filter tasks by priority",
        filter_options,
    )

    filtered_tasks = (
        tasks
        if selected_filter == "All tasks"
        else [
            t for t in tasks
            if t["priority"] == selected_filter
        ]
    )

    # Task cards
    for index, task in enumerate(filtered_tasks, start=1):
        if task["priority"] == "High":
            color, bg = "#b91c1c", "#fef2f2"
        elif task["priority"] == "Medium":
            color, bg = "#a16207", "#fffbeb"
        else:
            color, bg = "#047857", "#ecfdf5"

        title = html.escape(task["title"])
        deadline = html.escape(task["deadline"])
        reason = html.escape(task["reason"])
        priority = html.escape(task["priority"])

        st.markdown(f"""
        <div style="
            background:#ffffff;
            border:1px solid #e5eceb;
            border-radius:15px;
            padding:20px;
            margin:10px 0;
            box-shadow:0 4px 12px rgba(24,43,50,0.025);
        ">
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:flex-start;
                flex-wrap:wrap;
                gap:12px;
            ">
                <div style="
                    font-size:1.02rem;
                    font-weight:700;
                    color:#182b32;
                ">
                    {index:02d} &nbsp; {title}
                </div>
                <span style="
                    color:{color};
                    background:{bg};
                    border-radius:8px;
                    padding:6px 11px;
                    font-size:0.78rem;
                    font-weight:800;
                ">
                    {priority}
                </span>
            </div>
            <div style="
                margin-top:13px;
                font-size:0.88rem;
                color:#71828a;
            ">
                <b style="color:#354d52;">Deadline:</b> {deadline}
            </div>
            <div style="
                margin-top:7px;
                font-size:0.88rem;
                color:#71828a;
                line-height:1.6;
            ">
                <b style="color:#354d52;">Why:</b> {reason}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Export
    st.write("")
    st.markdown("### Export your plan")

    export_df = pd.DataFrame([
        {
            "Task": t["title"],
            "Deadline": t["deadline"],
            "Priority": t["priority"],
            "Reason": t["reason"],
        }
        for t in tasks
    ])

    st.download_button(
        "Download tasks as CSV",
        data=export_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="taskflow_plan.csv",
        mime="text/csv",
        use_container_width=True,
    )

    with st.expander("View all tasks in table format"):
        st.dataframe(
            export_df,
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("View formatted task list"):
        st.text(
            st.session_state.get("formatted_output", "")
        )


# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
    TaskFlow AI · Plan intentionally. Work confidently.
</div>
""", unsafe_allow_html=True)
