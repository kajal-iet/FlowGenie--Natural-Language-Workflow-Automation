# ⚙️ FlowGenie — Natural-Language Workflow Automation Designer

### Track: Enterprise Agents  
### Tech: Gemini 🔹 Google ADK 🔹 Multi-Agent 🔹 A2A 🔹 Evaluation 🔹 Sessions 🔹 Tools

FlowGenie converts **plain English workflow requests** into **machine-ready automation pipelines** (JSON), evaluates them, and simulates execution.

> “When a new support ticket arrives, add it to Google Sheets, email the support lead, and notify Slack.”

FlowGenie detects:
- **Trigger**
- **Action sequence**
- **Required systems (Sheets / Slack / Gmail / Calendar)**
- **Execution order**
- **Simulation status & summary**

---

## 🚀 Why FlowGenie
Enterprise teams use 7–20 SaaS tools but workflows aren’t automated because:
| Barrier | Reality |
|--------|---------|
| Manual work | Repetitive and slow |
| No-code tools | Still require workflow logic knowledge |
| APIs | Technical knowledge required |
| Automation engineers | Limited bandwidth |

FlowGenie removes the barrier → **describe a workflow as text → produce a working automation plan**.

---

## 🧠 Architecture Overview

┌──────────────┐
│ User Prompt  │
└───────┬──────┘
        ▼
┌─────────────────────┐
│ Planner Agent       │ → JSON Workflow (trigger + actions)
└─────────────────────┘
        ▼
┌─────────────────────┐
│ Evaluator Agent     │ → Score, risks, suggested changes
└─────────────────────┘
        ▼
┌──────────────────────────────────────────────┐
│ Executor Agent (A2A Plan Generator)          │
│   Determines which tool agent handles action │
│   Generates execution plan + simulation      │
└──────────────────────────────────────────────┘
        ▼
┌─────────────────────────────────────────────┐
│ Action Router (A2A runtime)                 │
│   Calls: Slack | Sheets | Gmail | Calendar  │
└─────────────────────────────────────────────┘
        ▼
┌────────────────────┐
│ Final JSON Summary │
└────────────────────┘




---

## 🔑 Features & Capstone Requirements Checklist

| Requirement | Implemented |
|------------|-------------|
| Multi-agent | ✔ (Planner, Evaluator, Executor + 4 Tool Agents) |
| A2A messaging | ✔ (Executor → Tool Agents) |
| Tools | ✔ (Slack, Sheets, Gmail, Calendar) |
| GeminI LLM agent | ✔ |
| Sessions & Memory | ✔ (`InMemorySessionService`) |
| Long-running simulation | ✔ (simulate_workflow_execution) |
| Evaluation metrics | ✔ |
| Observability | ✔ (`run_debug` per agent) |
| Deployment optional | Stub and API ready |

---

## 👁 Example Output

```json
{
  "workflow": { ... },
  "evaluation": { "overall_score": 8, "verdict": "ACCEPT" },
  "action_plan": [
    {"action_index": 1, "agent": "sheets_agent", "parameters": {...}},
    {"action_index": 2, "agent": "gmail_agent", "parameters": {...}},
    {"action_index": 3, "agent": "slack_agent", "parameters": {...}}
  ],
  "action_results": [
    {"action_index": 1, "status": "skipped", "reason": "missing_credentials"},
    {"action_index": 2, "status": "skipped", "reason": "missing_credentials"},
    {"action_index": 3, "status": "success_stub"}
  ],
  "simulation": { "status": "completed", "total_steps": 3 },
  "summary": "Workflow successfully executed in simulation mode."
}



# Setup (no credentials required)
pip install -U google-adk
pip install python-dotenv
