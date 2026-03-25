---
description: Business Analysis Workflow 2.2 - Multi-LLM Orchestrated
---

# BA Workflow Protocol 2.2

This workflow automates the creation of BA documentation with a focus on Data-Driven decisions and AI-assisted analysis.

// turbo-all

## Steps

1. **Project Classification & Metric Identification**
   - Check if project is `Product` or `Outsource`.
   - **New 2.2:** Ask user for the "North Star Metric" or "Business Goal".

2. **Initialize Workspace 2.2**
   - Create directory `d:\Project\BA studies\{topic}`.
   - Initialize a `00-Internal-Brainstorming.md` file for AI-driven notes.

3. **Template Selection & Data Planning**
   - Refer to `../BA-document-rule/overlays/{type}/overlay-config.md`.
   - **New 2.2:** Identify data events that need to be tracked for the success metrics.

4. **Document Generation (via @ba-specialist 2.2)**
   - For each mandatory file:
     - Copy template from `../BA-document-rule/templates/`.
     - **AI Insight:** Call `@ba-specialist` to generate the document PLUS an "Edge Cases & Risks" section.
     - **Visual First:** Generate at least one Mermaid diagram per document.
     - Add a "Success Metrics" table to the BRD.

5. **AI-Driven Quality Gate**
   - Run `../BA-document-rule/core/quality-checklist.md`.
   - **New 2.2:** Self-ask "Does this feature have a way to measure its success?"

6. **Final 2.2 Report**
   - List created files.
   - Summarize the **Data Plan** and **Key Risks**.

---

## Command Usage
`/ba-workflow [topic] [yêu cầu]`
