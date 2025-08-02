# MedBridge 🏥

MedBridge is a modular Python project built using Microsoft's [AutoGen](https://github.com/microsoft/autogen) framework. It orchestrates multiple intelligent agents and human-in-the-loop workflows to analyze patient symptoms, diagnose conditions, and generate personalized treatment plans.

---

## 🧠 Project Overview

MedBridge is structured around four core teams:

### 1. `med_core_symptom_team`
- Comprises a **Symptom Agent**
- Integrates **human feedback asynchronously** to clarify symptoms

### 2. `med_core_diagnosis_team`
- Comprises a **Diagnosis Agent**
- Uses patient history and symptom data
- Asks for additional user input if needed

### 3. `Treatment Plan Agent`
- Generates a treatment plan based on diagnosis
- Operates independently but receives structured input from previous teams

### 4. `med_core_results_team`
- Acts as the **entry point**
- Orchestrates the above teams in sequence:
  - `med_core_symptom_team` → `med_core_diagnosis_team` → `Treatment Plan Agent`
- Asynchronously interacts with the user to refine inputs and ensure accurate treatment planning

---

## 🧱 Project Structure

src/ 
    ├── agents/ # Individual agent definitions
    ├── teams/ # Team orchestration logic 
    ├── prompts/ # System prompts and role definitions 
    ├── utils/ # Model loading and helper utilities requirements.txt  
    # Python dependencies .env # Environment variables (ignored in Git) venv/ # Virtual environment (ignored in Git)

---

## 🚀 Getting Started

### 1. Create a virtual environment
```bash
conda create -p venv python=3.12 -y
```
### 2. Activate virtual environment
```bash
conda activate venv
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the script
```bash
python src/run_med_core_results.py
```

🧭 Architecture Diagram

🧠 Model Client
MedBridge uses OpenAI GPT-4o-mini as its model client, integrated via the ModelLoader utility.

🔒 Human-in-the-Loop
Each team incorporates asynchronous human feedback to ensure:

* Symptom clarity
* Diagnosis accuracy
* Personalized treatment planning

📄 License
This project is for educational and prototyping purposes. Not intended for clinical use.

## 🧭 Mermaid Diagram Code (for PNG generation)

You can use this code in a Mermaid live editor (like [Mermaid Live Editor](https://mermaid.live)) or a tool that supports Mermaid-to-PNG conversion.

```mermaid
graph TD
    A[User Query] --> B[med_core_results_team]
    B --> C[med_core_symptom_team]
    C -->|Asks for symptom clarification| U1[Human Feedback]
    C --> D[med_core_diagnosis_team]
    D -->|Requests history or additional info| U2[Human Feedback]
    D --> E[Treatment Plan Agent]
    E --> F[Final Treatment Plan]
