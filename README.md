# Forklift Daily Pre-Start Checklist App
A ticket-driven forklift pre-start inspection system built on the **V-ONE low-code platform**. It carries a forklift through its full daily lifecycle: inspection, PIC review, maintenance, operation and shutdown on a single traceable ticket, with an LLM step that drafts a suggested action for the reviewer whenever a defect is flagged.

# Problem Statement
Forklifts are high-risk equipment; most sites require a standardized pre-start checklist before every shift, with any defect gated behind a supervisor (PIC) sign-off before the unit can be used. Paper checklists make that gate easy to skip and impossible to audit later. This app puts the whole lifecycle: checklist → review → maintenance/release → operation → shutdown, on one status-driven ticket, and adds an AI-drafted action summary to reduce the PIC's triage time.

# Objective
1. Standardize 5S inspections
Provide a consistent checklist and scoring method for all audit areas.

2. Improve audit efficiency
Reduce manual paperwork and simplify the process of recording audit results.

3. Enable better tracking and accountability
Record findings, photo evidence, and improvement actions for easier follow-up.

4. Support continuous improvement
Provide clear audit results and trends to help identify recurring issues and improve workplace standards.

# Methodology
1. Workflow Automation
Designed and implemented a digital 5S audit workflow using the V-ONE low-code development platform. The workflow automates audit submission, scoring, evidence collection, review, and status tracking to standardize the inspection process.

2. Checklist & Scoring System
Developed a structured 5S checklist with predefined inspection criteria and scoring rules. The system records audit results for each area and calculates overall scores to provide a consistent evaluation of workplace conditions.

3. Digital Evidence & Action Tracking
Implemented photo evidence and remarks to document audit findings and support issue identification. Audit results and improvement actions are recorded for follow-up and traceability.

4. Business Analytics & Dashboard
Developed an interactive dashboard to monitor 5S audit scores, area performance, audit trends, and recurring issues, providing management with visibility into workplace conditions and supporting continuous improvement.

# Pre-Implementation Findings
1. Lack of a Structured Inspection Process

  Forklift pre-start inspections involve multiple safety and operational checkpoints.

  Inspection information may be difficult to standardise and track when recorded through manual or fragmented processes.

  A centralised digital checklist can provide a more consistent inspection process.


2. Need for Clear Defect Escalation

  Defects identified during pre-start inspections require further evaluation before the forklift can resume operation.

  A clear workflow is needed to differentiate between normal operation, PIC review, and maintenance.

  The app provides a structured escalation flow from inspection → PIC review → operation/maintenance.


3. Critical Safety Defects Require Immediate Action
   
  Certain defects, such as brake issues, LPG leakage, mast problems, and hydraulic-related issues, may pose significant safety risks.

  The inspection process should not only record defects but also support appropriate actions such as stop-work, quarantine, or     maintenance.


4. Need for End-to-End Traceability
   
  Forklift status needs to be traceable throughout different stages of its operational lifecycle.

  Inspection results, defect remarks, PIC decisions, maintenance information, and operating status should be linked to the same record.

  A ticket-based workflow can improve visibility and traceability.


5. Limited Availability of Production Data
    
  The application has not yet been deployed for actual production use.

  Therefore, current data cannot be used to establish actual defect trends, inspection compliance, review turnaround time, or maintenance performance.

  Production-level performance should be evaluated after sufficient real operational data has been collected.

# Future Data Analysis After Implementation

-Identify the most frequently reported defect categories.

-Monitor defect frequency by forklift unit.

-Identify recurring defects and potential maintenance issues.

-Analyse PIC review turnaround time.

-Monitor the proportion of forklifts cleared for operation vs. sent for maintenance.

-Evaluate inspection compliance and completion trends.

-Compare operational performance before and after app implementation.
