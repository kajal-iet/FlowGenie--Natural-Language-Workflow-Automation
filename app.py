# app.py
#  This is the main Streamlit app for FlowGenie, we'll build UI in futur on top of this
import json
import streamlit as st

from flowgenie_core.engine import handle_user_input_sync

st.set_page_config(
    page_title="FlowGenie – Workflow Automation Assistant",
    page_icon="⚙️",
    layout="centered",
)

st.title("FlowGenie 🧠⚙️")
st.caption("Turn plain English into automated business workflows – or just chat normally.")

st.markdown(
    """
**Examples you can try:**

- _\"Add a row to my spreadsheet with (003, Kajal, Login Issue, Unable to log in) and notify me on Slack.\"_  
- _\"Send an email to my Gmail saying (FlowGenie test) with subject (Testing automations).\"_  
- _\"Hi, I'm Kajal and I work as a software engineer.\"_ (will be stored in memory and used in chat mode)
"""
)

with st.form("flow_form"):
    user_prompt = st.text_area(
        "Write your request in plain English",
        height=160,
        placeholder="Example: When a new customer signs up, add a row in Sheets and send me a Slack alert.",
    )
    session_id = st.text_input(
        "Session ID (for chat memory continuity)",
        value="web_user_1",
        help="Use the same session ID to let the chat agent remember you over time.",
    )
    submitted = st.form_submit_button("Run FlowGenie")

if submitted and user_prompt.strip():
    with st.spinner("Thinking with agents..."):
        result = handle_user_input_sync(user_prompt, session_id=session_id or "web_user_1")

    st.subheader("Detected mode")
    st.code(result.get("mode", "unknown"), language="text")

    if result.get("mode") == "chat":
        st.subheader("Assistant reply")
        st.write(result.get("reply", ""))

    else:
        # Automation mode
        st.subheader("Workflow summary")
        st.write(result.get("summary", ""))

        st.subheader("Workflow JSON")
        st.json(result.get("workflow", {}))

        with st.expander("Evaluation details"):
            st.json(result.get("evaluation", {}))

        with st.expander("Execution plan (A2A)"):
            st.json(result.get("action_plan", []))

        with st.expander("Tool execution results"):
            st.json(result.get("action_results", []))

else:
    st.info("Type a request above and click **Run FlowGenie** to get started.")
