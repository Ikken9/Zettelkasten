# Architectural Patterns


## Three-Tier Architecture
Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: the presentation tier, or user interface; the application tier, where data is processed; and the data tier, where application data is stored and managed.

#### Presentation tier
The presentation tier is the user interface and communication layer of the application, where the end user interacts with the application. Its main purpose is to display information to and collect information from the user. This top-level tier can run on a web browser, as desktop application, or a graphical user interface (GUI), for example. Web presentation tiers are developed by using HTML, CSS, and JavaScript. Desktop applications can be written in various languages depending on the platform.

#### Application tier
The application tier, also known as the logic tier or middle tier, is the heart of the application. In this tier, information that is collected in the presentation tier is processed - sometimes against other information in the data tier - using business logic, a specific set of business rules. The application tier can also add, delete, or modify data in the data tier using [[API|API]] calls. 

#### Data tier
The data tier, sometimes called database tier, data access tier or back-end, is where the information that is processed by the application is stored and managed.


## Model View Controller Pattern (MVC)
MVC is an architectural pattern used to decouple user-interface (view), data (model), and application logic (controller). This pattern helps to achieve separation of concerns.

Using the MVC pattern for websites, requests are routed to a Controller that is responsible for working with the Model to perform actions and/or retrieve data. The Controller chooses the View to display and provides it with the Model. The View renders the final page, based on the data in the Model.


## Saga Architecture Pattern
The Saga architecture pattern **provides transaction management using a sequence of local transactions.**

##### Context
A _transaction_ is a single unit of logic or work, sometimes made up of multiple operations. Within a transaction, an _event_ is a state change that occurs to an entity, and a _command_ encapsulates all information needed to perform an action or trigger a later event.

Transactions must be _atomic, consistent, isolated, and durable (ACID)_. Transactions within a single service are **ACID**, but cross-service data consistency requires a cross-service transaction management strategy

A local transaction is the unit of work performed by a Saga participant. Every operation that is part of the Saga can be rolled back by a compensating transaction. Further, the Saga pattern guarantees that either all operations complete successfully or the corresponding compensation transactions are run to undo the work previously completed.

In the Saga pattern, **a compensating transaction must be _idempotent_ and _retryable_.** These two principles ensure that we can manage transactions without any manual intervention.


## Broker Architecture Pattern

A broker pattern is used for structuring distributed systems with decoupled components. By invoking remote services, components can interact with others in broker architecture patterns. Also, the broker is responsible for all the coordination and communication among the components. 

Clients, servers, and brokers are three major components of the broker pattern. Generally, a broker will have access to all the services and characteristics related to a particular server. When clients request a service from the broker, the broker redirects them to a suitable service category for further process. 

One of the key benefits of this architecture pattern is how it manages operations, such as change, addition, deletion, or relocation, related to objects in a dynamic manner. Lastly, this architecture pattern separates all communication-related code into layers from the application, allowing applications to run on distributed or single computers. Because of such advantages, broker architecture has been prevalent.



## Backends For Frontends
Create separate backend services to be consumed by specific frontend applications or interfaces. This pattern is useful when you want to avoid customizing a single backend for multiple interfaces. This pattern was first described by Sam Newman.
#### Context
An application may initially be targeted at a desktop web UI. Typically, a backend service is developed in parallel that provides the features needed for that UI. As the application's user base grows, a mobile application is developed that must interact with the same backend. The backend service becomes a general-purpose backend, serving the requirements of both the desktop and mobile interfaces.

But the capabilities of a mobile device differ significantly from a desktop browser, in terms of screen size, performance, and display limitations. As a result, the requirements for a mobile application backend differ from the desktop web UI.

These differences result in competing requirements for the backend.

#### Solution
Create one backend per user interface. Fine-tune the behavior and performance of each backend to best match the needs of the frontend environment, without worrying about affecting other frontend experiences.



## BFF vs API Gateway
BFF Layer is basically an orchestrator layer which is also called as **Backend for frontend**. When an orchestrator layer includes aggregation, computation, composition of some data then it’s more than a simple [[API Gateway|API gateway]].

BFF is mostly used to support its client request with one-size-fit all API

While an [[API Gateway]] is a single point of entry into the system for all clients, a **BFF is only responsible for a single type of client**. Let’s assume your system has two (typical) clients: A Single Page Application (SPA) and a mobile client (Android, iOS). In this case, each client would get its own API Gateway, which would therefore be a _BFF_. In other words, an **API gateway is a single point of entry for all clients fetching data from the system, while a** **backend-for-frontend (BFF) is tailored to a specific frontend** — typically with multiple BFFs corresponding to multiple frontends.



## What is the difference between tiers and layers?
#### Layer
**The term layer refers to a logical separation of code.** In other words, it’s a coherent set of related functionality.
Structuring applications in layers is a way to organize our codebase better. For this reason, portability and maintainability are drivers that push us to use this kind of structure.
Indeed, we find an application of this concept in various types of architecture, such as _Layered Architecture_ and _Hexagonal Architecture_.

#### Tier
**On the other hand, the term tier refers to the physical structure**. Tiers define where to deploy the layers, without necessarily a one-to-one mapping. So when we talk of an application’s tiers, we mean its topology.
**Tiers are defined with an eye toward the computing environment on which the software will run.** By dividing an application into tiers, it’s possible to achieve a higher degree of scalability.

