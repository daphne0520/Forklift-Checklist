# Forklift Daily Pre-Start Checklist App
A ticket-driven forklift pre-start inspection system built on the **V-ONE low-code platform**. It carries a forklift through its full daily lifecycle: inspection, PIC review, maintenance, operation and shutdown on a single traceable ticket, with an LLM step that drafts a suggested action for the reviewer whenever a defect is flagged.

# Problem Statement
Forklifts are high-risk equipment; most sites require a standardized pre-start checklist before every shift, with any defect gated behind a supervisor (PIC) sign-off before the unit can be used. Paper checklists make that gate easy to skip and impossible to audit later. This app puts the whole lifecycle: checklist → review → maintenance/release → operation → shutdown, on one status-driven ticket, and adds an AI-drafted action summary to reduce the PIC's triage time.

# Objective
1. Standardize pre-start inspections Provide a consistent 17-item checklist covering all critical safety and operational checkpoints for every forklift, every shift.

2. Enforce a clear defect escalation gate Ensure any failed checklist item routes the ticket to PIC review before the forklift can return to operation, closing the gap that paper checklists leave open.

3. Reduce PIC triage time with AI-assisted analysis Automatically draft a defect summary and suggested action (e.g. stop-work, quarantine, route to maintenance) whenever a defect is flagged, so the PIC reviews AI-drafted guidance rather than starting from a blank remark.

4. Enable better tracking and accountability Carry inspection results, defect remarks, PIC decisions, and maintenance outcomes on a single traceable ticket from checklist to shutdown.

5. Support fleet-wide visibility Provide a dashboard showing each forklift's current status, ticket history, and fleet-level distribution across preparation, review, operation, maintenance, and shutdown.


# Methodology
1. Workflow Automation Designed and implemented a digital forklift lifecycle workflow using the V-ONE low-code development platform. A single ticket moves through checklist submission, PIC review, maintenance/release, operation, and shutdown, with status-driven routing at each stage.

2. Checklist Design Developed a standardized 17-item pre-start checklist covering forks and load handling, mast/chains/hydraulics, tires, brakes, LPG/fuel systems, safety interlocks, and other critical checkpoints, with pass/fail marking and remarks per item.

3. AI Defect Analysis Integration Implemented an LLM-based workflow that triggers when a ticket enters "Awaiting Review": a prompt builder assembles the flagged defect details, the model returns a defect analysis and suggested action, and the ticket is updated with this AI-drafted guidance before it reaches the PIC Inspector Portal.

4. Digital Evidence & Action Tracking Recorded defect remarks, AI-suggested actions, PIC decisions, and maintenance outcomes on the same ticket to support issue identification and follow-up.

5. Business Analytics & Dashboard Developed an interactive dashboard to monitor fleet status (operating, maintenance, pending PIC, shut down), per-unit ticket history, and fleet-wide status distribution, providing management with visibility into fleet safety and availability.

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
