# 🚀 FlowGenie — Natural Language Automation for Business
Turn plain English into automated business workflows.

FlowGenie is an **enterprise multi-agent automation system** that converts natural language requests (e.g.  
“Send a message to Slack and log the issue in Sheets”) into **end-to-end automated actions** across different tools.

It is built for **non-technical business teams** — no scripting, no UI clicking, just chat.

---

## 🌟 Key Features

| Capability | Description |
|-----------|-------------|
| Multi-Agent Architecture | Planner → Evaluator → Executor → Tool Agents → Memory |
| Natural Language Automation | “Send Slack message”, “Append row to Sheet”, “Schedule a meeting”, etc |
| Real API Integrations | Slack, Google Sheets, Gmail, Google Calendar |
| Long-Term Memory | Remembers user identity, preferences and past chats |
| Session Management | Persistent via SQLite (auto restored across restarts) |
| Automated Workflow Evaluation | Evaluates workflow safety & completeness |
| A2A Execution | Agents call each other to complete actions |

FlowGenie replaces manual business tasks — status updates, ticket creation, reminders, emails — with **fully automated workflows** triggered simply by chat.

---

## 🧠 How It Works
User → Router → (Chat agent OR Automation agents)
Automation Flow:
Planner → Evaluator → Executor → Tool Agents (Slack / Sheets / Gmail / Calendar)
Chat Flow:
Chat Agent + Memory (SQLite) → natural conversation



---

## 🧩 Example Workflows

| Natural Language | Automation Performed |
|------------------|---------------------|
| "Send a Slack message to #support saying deployment successful" | Slack notification |
| "Add a new record to my sheet: (004, Priya, Login issue, resolved)" | Append row to Google Sheets |
| "Send email to manager with subject (Update) body (Deployment completed)" | Gmail |
| "Schedule a meeting tomorrow 2–3 PM titled Sprint Demo" | Google Calendar |

---

## 🗂 Multi-Agent System Used

| Role | Agent | Responsibility |
|------|--------|----------------|
| Routing | `intent_router` | Classifies chat vs automation |
| Planning | `workflow_planner` | Turns prompt into workflow JSON |
| Evaluation | `workflow_evaluator` | Scores workflow quality |
| Execution | `workflow_executor` | Builds step-by-step tool plan |
| Tools | `slack_agent`, `sheets_agent`, `gmail_agent`, `calendar_agent` | Run external APIs |
| Chat | `chat_assistant` | Normal conversation + memory |

---

## 🛠 Supported Real APIs

| System | Action |
|--------|--------|
| Slack | Send channel notification |
| Google Sheets | Append row |
| Gmail | Send email |
| Google Calendar | Create event |

> Full configuration instructions are in [`SETUP.md`](./SETUP.md)

---

## 🧪 Quick Start (Notebook)

Run the notebook and then test:

```python
prompt = "Send a Slack notification to #new-channel now, saying I am Anchal and grateful!"
result = await handle_user_input(prompt, session_id="demo")
print(result)

Or chat normally:

prompt = "Hi, I am Kajal."
print(await handle_user_input(prompt, session_id="demo"))


## TODO LIST

## Deployment (Cloud Run example)

This project can be containerized and deployed to a managed runtime like **Cloud Run**:

# Build container
gcloud builds submit --tag gcr.io/PROJECT_ID/flowgenie

# Deploy to Cloud Run
gcloud run deploy flowgenie \
  --image gcr.io/PROJECT_ID/flowgenie \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated


The container runs the Streamlit UI on port 8080.
You can configure environment variables (GOOGLE_API_KEY, SLACK_WEBHOOK_URL, etc.)
via the Cloud Run console or --set-env-vars.