# 🚀 SupportTriage-OpenEnv: Enterprise-Grade Ticket Intelligence

[![Meta PyTorch Hackathon](https://img.shields.io/badge/Competition-Meta%20PyTorch%20Hackathon-orange?style=for-the-badge&logo=pytorch)](https://metapytorch.devpost.com/)
[![OpenEnv](https://img.shields.io/badge/OpenEnv-Compatible-brightgreen?style=for-the-badge)](https://github.com/openenv/openenv)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**SupportTriage-OpenEnv** is a high-fidelity simulation environment for training and evaluating AI agents in customer support triage. Developed as a modular and scalable solution for the **Meta PyTorch Hackathon**, it leverages the [![OpenEnv](https://img.shields.io/badge/OpenEnv-Compatible-brightgreen?style=for-the-badge&logo=github)](https://github.com/openenv/openenv)
 standard to provide a realistic, deterministic framework for complex agentic workflows.

## 📋 Table of Contents
- [📊 Evaluation & Benchmarks](#-evaluation--benchmarks)
- [⚙️ Environment Specification](#️-environment-specification)
- [💰 Reward Design Methodology](#-reward-design-methodology)
- [🏗️ System Architecture](#️-system-architecture)
- [🚀 Quick Start Guide](#-quick-start-guide)
- [🏆 Hackathon Submission](#-hackathon-submission)

---

## 📊 Evaluation & Benchmarks (v2.0)

Evaluated via the standardized inference baseline. Results demonstrate the agent's capacity for zero-shot reasoning under stochastic environmental constraints.

| Task ID | Level | Logic Objective | Success (0–1) | Reward | Result |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **ENV-T1** | 🟢 Low | Semantic Urgency Classification | **1.00** | **10.20** | ✅ PASSED |
| **ENV-T2** | 🟡 Mid | Intent-Based Functional Routing | **0.50** | **5.90** | ✅ PASSED |
| **ENV-T3** | 🔴 High | Multi-Turn Technical Resolution | **0.30** | **3.40** | ✅ PASSED |

> [!TIP]
> The performance decay observed in higher-tier tasks illustrates the environment's effectiveness in highlighting reasoning gaps in long-horizon dialogue and noisy contexts.

---

## ⚙️ Environment Specification

### 📥 Observation Space
Agents receive a high-fidelity `Observation` object:
- **`current_ticket`**: Comprehensive metadata + Ticket payload.
- **`history`**: Complete session dialogue log (Multi-turn support).
- **`memory`**: Persistent, agent-writable state for cross-step context preservation.
- **`error_logs`**: Diagnostic feedback for simulating system-level failures.

### 📤 Action Space
A clean, functional API for agentic interaction:
- **`classify(priority)`**: Categorize by business urgency.
- **`route(team)`**: Accurate dispatch to functional departments.
- **`respond(text)`**: Empathetic, context-aware customer communication.
- **`close()`**: State finalization and deterministic grading trigger.

---

## 💰 Reward Design Methodology

Our reward function is engineered to align agent behavior with enterprise KPIs:
- **Accuracy (The "North Star")**: Exponentially weighted by task complexity.
- **User Engagement**: `+0.5` bonus for actions that elicit constructive user replies.
- **Operational Efficiency**: `+0.1` incremental reward for valid workflow transitions.
- **Redundancy Penalty**: `-1.0` penalty to eliminate looping and redundant processing.

---

## 🏗️ System Architecture

A modular, decoupled structure optimized for developer experience and CI/CD integration.

```text
├── 📂 env/           # OpenEnv Core (Reset/Step/State)
├── 📂 graders/       # Hard-coded, deterministic validation logic
├── 📂 models/        # Type-safe schemas (Pydantic models)
├── 📂 tasks/         # Scenario registry & stochastic noise engine
├── 📂 scripts/       # Evaluation baselines & deployment tools
└── 📄 openenv.yaml   # Standardized environment manifest
```

---

## 🚀 Quick Start Guide

### 🧱 Environment Setup
```bash
git clone https://github.com/your-username/support-triage
cd support-triage
pip install -r requirements.txt  # (openai, pydantic, pyyaml)
```

### 🛰️ Running the Baseline
```bash
# Execute local evaluation using mock agent logic
python -m scripts.baseline
```

---

## 🏆 Hackathon Submission

**Project Goal**: 
> "Develop a production-ready OpenEnv compatible with standard agentic APIs to solve real-world industrial challenges."

### Developed by: Solo Warrior
**Vijayapandian T** | 📧 [vijayapandian112007@gmail.com](mailto:vijayapandian112007@gmail.com)  
*Proudly built for the Meta PyTorch Hackathon (Round 1).*

---

## 📄 License
This project is licensed under the MIT License.
