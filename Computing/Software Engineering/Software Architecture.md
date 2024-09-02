# Software Architecture

Software architecture are a set of artifacts (that is: principles, guidelines, policies, models, standards, and processes) and the relationships between these artifacts, that guide the selection, creation, and implementation of solutions aligned with business goals.

A software architecture is a description of the **subsystems** and **components** of a software system and the relationships between them:
- **Subsystems** and **components** are typically specified in different views to show the relevant functional and non-functional properties of a software system.
- The software system is an artifact. It is the result of the software design activity.

The _architecture_ of a software system is a metaphor, analogous to the architecture of a building. It functions as the blueprints for the system and the development project, which project management can later use to extrapolate the tasks necessary to be executed by the teams and people involved.


## Software Architecture Process

The Software Architecture Process refers to the series of steps and methodologies used to design, develop, and implement the architecture of a software system. This process ensures that the software system meets both functional and non-functional requirements, such as scalability, performance, and maintainability.

These are the key phases in the Software Architecture Process:

### 1. **Requirement Gathering and Analysis**
- Understand the system's [[Functional Requirements (FRs)]] and [[Non-Functional Requirements (NFRs)]]
- Work closely with stakeholders, gather detailed requirements, and analyze them to understand the system's needs. This step is crucial for setting the foundation of the software architecture.
- What freedom do we have?
- What is to be solved?
- Determine the use cases
- Determine the constraints

### 2. **Architectural Design**
- Develop a high-level design that outlines the structure of the system, use an [[Architecture Overview Diagram (AOD)]].
- Identify the main components or modules, their relationships, and interactions.
- Choose appropriate technologies, frameworks, and platforms.
- Apply relevant design patterns to ensure a scalable and maintainable architecture.

### 3. **Architectural Documentation**
- Create diagrams (e.g., flowcharts, class diagrams, sequence diagrams), define component interactions, interfaces, and describe the deployment view. Tools like UML (Unified Modeling Language) are often used.
- Document the architecture for communication and future reference.
- Use [[Architecture Decision Record (ADR)]]

### 4. **Architectural Evaluation**
- Assess the architecture to ensure it meets the required quality attributes.

### 5. **Prototyping**
- Before doing an implementation, validate the architecture by creating a working model or proof of concept.
- Implement a small part of the system, focusing on critical components to test assumptions, assess feasibility, and identify potential issues early.

### 6. **Implementation and Integration**
- Build the system based on the architectural design.
- Develop software components, integrate them, and ensure that the implementation follows the architectural guidelines.

### 7. **Maintenance and Evolution**
- Adapt the architecture to changes in requirements or technology over time.
- Refactor and evolve the architecture to address new requirements, performance improvements, or technology upgrades while maintaining system integrity.


## Architecture Decisions
Often, there is more than one possible solution to an architectural problem. This involves components and their relationships, technology choices, assigning functionalities to different components, and making decisions about the placement of components across different nodes. Each alternative has different costs, meets a set of requirements or constraints, and offers different ways to balance competing interests. They allow for:

- Documenting the critical choices made in creating the solution. 
- Understanding and agreeing on why the solution is what it is -> ***Why is more important than how.*** 
- Making explicit the reason and justification for the decision that was made. 
- Helping ensure that the solution meets functional and non-functional requirements, and if it does not, making it explicit to stakeholders. 
- Preventing rework during the project's life cycle.

Architectural decisions should be properly documented, preferably using a standard template/solution like an [[Architecture Decision Record (ADR)]].


*See also [[Component Modeling]], [[The Operational Aspect of Software Architecture]]*


## Viability

*"The common causes for troubled projects are known, and almost all are avoidable."*

A software-oriented **viability assessment** focuses on determining whether a proposed software project or solution is feasible, sustainable, and likely to succeed. The process considers various aspects specific to software development, including technical feasibility, resource requirements, market demand, risks, and alignment with business goals.

Even most well thought through solution are imperfect
- **Cost**: Budgets are limited. Even if a project starts off well-funded, new cost constraints may cause solution architectures to change radically from initial design.
- **Information**: *"As you know more, you know more"*. New information: requirements, legislation, competition causes change to the business. The architecture must change to accommodate new information constantly.
- **Skilled resources**: Throughout a long-lived project, staff comes and goes.
- **Time**: Architects never have sufficient time, particularly at the beginning of the project when they have the most influence.


## Risk Assessment and RAID

#### Step 1. Identify project risks
Start by brainstorming and analyzing potential risks and opportunities related to your project scope. Leave no risk behind. Depending on your organization and project, your list of risks might include several types of risks, such as cost, environmental, and legal risks.

### Step 2: Determine the risk likelihood
In this step, you need to identify the likelihood of a given risk happening. ​​On a 5×5 matrix, you express the **likelihood scale** on 5 levels:

- **1** – (Very unlikely): A very slim chance for this risk to occur.
- **2** –  (Not likely): Low chances for this risk to occur.
- **3** – (Possible): Fifty-fifty chances for this risk to occur.
- **4** – (Probable): Good chances for this risk to occur.
- **5** – (Very likely): You can bet this risk will occur at some point.

### Step 3. Define the impact scale

Next, you rank your risks based on the impact they would cause on your project if they occur. The **impact scale** also has 5 levels:

- **1** – (Negligible): This risk will hardly impact your project.
- **2** –  (Low): You can easily handle the consequences of this risk.
- **3** – (Moderate): It will take some time and effort to mitigate the consequences of this risk.
- **4** – (Significant): This risk could cause long-term consequences that will be hard to recover from.
- **5** – (Catastrophic): The impact of this risk might wreck your project.

#### RAID
In project management, **RAID** is a technique that evaluates the effectiveness of a work assignment. A project manager often creates and adds updated information to a RAID log, which includes an agenda for completing tasks and satisfying the needs of stakeholders. The term RAID is an acronym that represents the following terms that apply to project management:

- Risks: Risks represent potential challenges that can interfere with the success of the assignment. The RAID log explains the risks and their causes, discusses the effects they can have on the project's goals and develops strategies for avoiding and overcoming them.
- Actions: Actions are the tasks team members plan to work on to deliver a quality final product. In this section, project managers identify the employees responsible for the tasks and the timeline for finishing them.
- Issues: Issues are hardships project management teams have encountered in the past. The log explains how the issue transpired, who contributed to its occurrence and what team members did to resolve it.
- Decisions: Decisions are choices the group made throughout the course of the project, which allow employees to track changes to their objectives. In the log, project managers may write what they decided on, who made the decision and when they agreed on the choice.


## Verification and Validation

Is the process of checking that a software engineer system meets specifications and requirements so that it fulfills its intended purpose. It may also be referred to as software quality control. It is normally the responsibility of software testers as part of the software development lifecycle.

Verification and validation are not the same thing, although they are often confused. Barry Boehm succinctly expressed the difference as:

- **Verification**: *Are we building the product right?*
- **Validation**: *Are we building the right product?*

