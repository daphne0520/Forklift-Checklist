```mermaid
flowchart TD
    A([Start]) --> B[Preparation]
    B --> C[Complete 17-Item Checklist]
    C --> D{All Items Pass?}

    D -->|Yes| G[Operating]
    D -->|No| E[Awaiting Review]

    E --> F[AI Defect Analysis]
    F --> H[AI Suggested Action]
    H --> I[PIC Review]
    I --> J{Decision}

    J -->|Release| G
    J -->|Maintenance Required| K[Maintenance]
    K --> L[Repair / Corrective Action]
    L --> M[Maintenance Release]
    M --> G

    G --> N[Shut Down]
    N --> O([Closed])
