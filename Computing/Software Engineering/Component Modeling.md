# Component Modeling

A **Component Model** is a formal representation of: 
- The internal Structure of the solution (the relationships between the components that make up the solution), i.e. Static View, and solution Behavior, i.e. Dynamic View. 
- A next step from the System Context Diagram that aligns with the Black Box engineering principle to the White Box principle, whereby the architects look at “what’s inside the solution” 
- Provides the necessary input for the operational model to make proper placement decisions about the components various aspects: 
	- *Where should the components run?*
	- *Where should the components data be?* 
	- *Where should the components be installed?
	- *How will the components communicate with each other?*

## Why a model? 
- Today's complex, software-intensive systems cannot be understood without models. 
- Models break down complex systems into smaller parts – components, that have well understood functional responsibilities. It helps us visualize and understand the system.


## Building a component model
### A Component is a primary concept used for describing the functional aspect of the IT architecture
“Component” is a widely used and abused term not only in the world of software engineering. According to the _Merriam-Webster Dictionary,_ a component is “a constituent part,” and in this meaning, the term is used for almost anything that is a part of something bigger.

The **Unified Modeling Language (UML)** provides a more meaningful definition:

*"A component represents a modular part of a system that encapsulates its contents and whose manifestation is replaceable within its environment."

- A component is a modular unit of functionality. 
- A component makes its functionality and state available through one or more interfaces.
- Components serve as the building blocks for the structure of a system

Examples of components are: 
- At the application level of the component model: 
	- Business processing components (such as the Customer Processing component) 
	- Business service components (such as the Account Manager component) 
- At the technical level of the component model: 
	- Technical components (security services or middleware such as messaging or transaction software) 
	- System software components (such as an operating system) 
	- Hardware components (such as an encryption device)


## Components can be classified as...

#### Application vs Technical
- **Application Components** implement a specific business function within the IT system (e.g. Payment Component).
- **Technical Components** are **NOT** associated with a specific business function. They play a technical role that supports realization of other components and supports facilitation of their non-functional requirements (e.g. a Web Server, Hypervisor, DNS Server).

#### Logical vs Physical 
- Logical: focuses on the functional responsibility and purpose of the of the solution components without being concerned of their implementation.
- Physical: Represents actual concrete software or hardware technology, a product/package used for component implementation. These are decision usually made during the Component Implementation stage.


### 1. Identifying components
Component identification is the first step of the component modeling technique and involves the following. Driven by an understanding of the business requirements the Architect will:
- Partition the system into subsystems and components and assign responsibilities based on an analysis of the requirements. 
- Use a reference architecture, architectural patterns, and other reusable assets that can be used as a starting point 
- Ensure the components are well structured, so that they are: 
	- *Highly cohesive?*: Do the responsibilities assigned to a component make sense? 
	- *Loosely coupled?*: Are two or more components too dependent on each other? 
	- *Well isolated?*: Have product or technology dependencies been confined to a few places? 
	- *Of the right granularity?:* Have sufficient responsibilities been allocated to the component? 
	- Layered according to their generality

Isolation is a measure of the degree to which product and technology dependencies are isolated.

Layering involves separating out components according to their generality.


### 2. Specifying Components
Component specification is the second step of the component modeling technique and involves: 
- Defining component interfaces by separating out the responsibilities placed on the components.
- For each interface, specifying the operations and their signatures, that is, parameters passed and return values .
- For each operation, specifying its contract of behavior or preconditions and postconditions.


### 3. Implementing components
Component Implementation is the third step of the component modeling technique and involves:
- For those components that are to be implemented using commercial-off-the-shelf (COTS) products, map the specified-level components to the appropriate products or packages. 
- For those components that are to be built, identify the approach to implementation by defining the physical-level components. Use patterns or other assets to help in this definition. 
- And don’t forget that many components will be realized as standard technologies defined with selection criteria in the EA. 
	- Whether at the *IS* level of IT business functionality
	- Or the *technology* level of IT middleware and so on
- Enterprise Architectures frequently adopt the Reuse before Customize before Buy before Build guideline.


## Component Diagram

![component_diagram](componentDiagramUML2.jpg)


