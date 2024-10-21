# Architecture Decision Record (ADR)

An **Architecture Decision Record (ADR)** is a *point-in-time* document that records architectural decisions and the reasoning behind them.

Think of it as a snapshot that says, “On this date, given the context, drivers, and information we had, we made a decision to go with Option Z. We considered Options X, Y, and Z.”

- **The Decision:** Written as a statement, for example: *"The system will use the messaging integration pattern to communicate with the XYZ application."*
- **Identifier:** A unique code that identifies the decision, for example: *"AD-065."*
- **Problem/Context:** A description of the situation in which a decision needs to be made, for example, *"How should the system integrate with the XYZ application?"*
- **Assumptions:** What we understand to be true about the problem context, solution constraints, etc., for example: *"The XYZ application supports a messaging interface."*
- **Alternatives:** If there are no alternatives, there cannot be an architectural decision. This is a list of alternatives and explanations. Example: *1-File transfer 2-Messaging 3-REST [[API|API]].*
- **Decision:** The decision made, for example: *"Alternative 2 is chosen."*
- **Justification:** Why the decision was made, for example: *"Messaging provides reliable, asynchronous program-to-program communication."*
- **Implications:** The consequences and impacts of the decision on other aspects of the solution. For example: *1. An integration node is required 2. A new layer will exist that must be considered for performance modeling and availability.*
