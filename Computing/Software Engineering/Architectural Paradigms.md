# Architectural Paradigms


An **architectural paradigm** or **style** is a description of component types and their topology. It also includes a description of the pattern of data and control interaction among the components and an informal description of the benefits and drawbacks of using that style.

"An architectural style is a coordinated set of architectural constraints that restricts the roles/features of architectural elements and the allowed relationships among those elements within any architecture that conforms to that style."

## Monolithic
In a monolithic architecture, the entire application is developed as a single, unified unit where all components are interconnected and run within a single process. This approach involves a single codebase that contains all the modules and components, which are tightly coupled and share the same resources and memory space. Initially, this can make development simpler due to fewer moving parts and less complexity in communication between components. Deployment is also straightforward as the application is deployed as a single unit.

**Pros:**
- **Simplicity:** Easier to develop and understand due to fewer moving parts and a single codebase.
- **Performance:** Inter-process communication is more efficient because all components run within a single process, reducing overhead.
- **Testing:** Easier to test in isolation since all components are contained within one application, making integration testing more straightforward.
- **Deployment:** Simplified deployment process since the entire application is deployed as a single unit.

**Cons:**
- **Scalability:** Scaling the application means scaling the entire monolith, which can be inefficient and costly, especially for large applications.
- **Flexibility:** Limited flexibility in technology choices and updating individual components, as changes in one part can impact the whole system.
- **Maintenance:** As the application grows, it can become more difficult to maintain due to complex inter-dependencies and longer build times.
- **Deployment Risk:** A failure in any component can potentially cause the entire application to fail, posing higher risk during updates or maintenance.


### **Types of monolithic architectures**

#### Layered architecture
Is a common pattern used in software design, where the application is divided into different layers based on their functionality. Often divided in four layers.

The layers typically are:
- **Presentation**
- **Application**
- **Domain**
- **Infrastructure**

Each layer of the layered architecture pattern has a specific role and responsibility within the application. For example, a presentation layer would be responsible for handling all user interface and browser communication logic, whereas a business layer would be responsible for executing specific business rules associated with the request. Each layer in the architecture forms an abstraction around the work that needs to be done to satisfy a particular business request.
Suitable for medium to large-sized applications with complex business logic. Ideal for systems with changing requirements, as it provides flexibility.


#### Pipeline architecture
The pipeline architecture is one of the most common architecture styles used in designing software systems. Also known as _pipes and filters_, it consists of a series of discrete steps performed in a predictable sequence. This is different from the model-view-controller pattern in a layered architecture.
The most common use case for a pipeline architecture is system integration. Any time you need to move data from one application to another, a pipeline is a very suitable style. Because you define the integration solution as a series of discrete steps, it makes for a very modular design. The filters themselves are highly cohesive and loosely coupled, meaning they do one thing only, and a filter has no dependency on other filters.

Decompose a task that performs complex processing into a series of separate elements that can be reused. Doing so can improve performance, scalability, and reusability of initial steps by allowing task elements that perform the processing to be deployed and scaled independently. Pipes and Filters pattern supports a high level of modularity.

It breaks down the processing required for each stream into a set of separate components (or filters), each performing a single task.

##### Considerations
- **Monolithic nature**. This pattern is usually implemented as a monolithic pipeline, so for any change, the entire filter chain should be tested end to end. Also, fault-tolerance for the whole process needs to be considered; if a filter or pipe fails, the whole pipeline is likely to fail.

- **Complexity**. The increased flexibility that this pattern provides can also introduce complexity, especially if the filters in a pipeline are distributed across different servers.

- **Reliability**. Use an infrastructure that ensures that data flowing between filters in a pipe aren't lost.

- **Idempotency**. If a filter in a pipeline fails after receiving a message and the work is rescheduled to another instance of the filter, part of the work might already be complete. If the work updates some aspect of the global state (like information stored in a database), a single update could be repeated. A similar issue might occur if a filter fails after it posts its results to the next filter, but before it indicates that it completed its work successfully. In these cases, another instance of the filter could repeat this work, causing the same results to be posted twice. This scenario could result in subsequent filters in the pipeline processing the same data twice. Therefore, filters in a pipeline should be designed to be idempotent.

- **Repeated messages**. If a filter in a pipeline fails after it posts a message to the next stage of the pipeline, another instance of the filter might be run, and it would post a copy of the same message to the pipeline. This scenario could cause two instances of the same message to be passed to the next filter. To avoid this problem, the pipeline should detect and eliminate duplicate messages.


#### Microkernel architecture
El estilo arquitectónico de Microkernel o también conocido como arquitectura de *Plug-in*, permite crear aplicaciones extensibles, mediante la cual es posible agregar nueva funcionalidad mediante la adición de pequeños plugins que extienden la funcionalidad inicial del sistema.
En una arquitectura de Microkernel las aplicaciones se dividen en dos tipos de componentes, en sistema Core (o sistema central) y los plugins (o módulos), el sistema Core contiene los elementos mínimos para hacer que la aplicación funcione y cumpla el propósito para el cual fue diseñada, por otra parte, los módulos o plugins con componentes periféricos que se añaden o instalan al componente Core para extender su funcionalidad. En este sentido, solo puede haber un componente Core y muchos Plugins.



## Distributed
Distributed systems architecture involves constructing an application from multiple independent components or services that communicate over a network. Each service operates as a separate process and may be hosted on different machines. This approach emphasizes decentralization, with loosely coupled components that can be developed, deployed, and scaled independently. Communication between these services is managed through network protocols such as HTTP, RPC, or messaging queues. This architecture allows for flexibility in technology choices and enables each component to be updated or scaled without affecting the entire system.

**Pros:**
- **Scalability:** More scalable because individual components can be scaled independently based on demand, improving resource efficiency.
- **Flexibility:** Allows for the use of different technologies and languages for different components, and enables independent updates or replacements.
- **Resilience:** Greater fault tolerance, as the failure of one component does not necessarily affect the entire system, improving overall reliability.
- **Maintainability:** Easier to maintain and upgrade individual services without impacting the whole system, facilitating modular development.

**Cons:**
- **Complexity:** Increased complexity due to managing multiple services, network communication, and potential issues with synchronization and data consistency.
- **Deployment:** More complex deployment processes, requiring infrastructure for service orchestration, discovery, and [[Monitoring|monitoring]].
- **Testing:** More challenging to test due to the need for integration testing across different services and handling network latency or failures.
- **Performance Overhead:** Potential performance overhead from inter-service communication over a network, which can introduce latency and additional complexity.

### **Types of distributed architectures**

#### Service-Oriented Architecture (SOA)
SOA is an architectural pattern where the application is composed of services that communicate over a network using standard protocols. Unlike microservices, SOA often involves more extensive use of enterprise service buses (ESBs) and has a focus on reusability and integration.

**Characteristics:**
- **Service Composition:** Services are designed to be reusable and can be composed into larger business processes.
- **Interoperability:** Services communicate through standardized protocols like SOAP and WSDL.
- **Enterprise Integration:** Often used for integrating diverse systems within an enterprise.

#### Event-Driven Architecture (EDA)
Is a design pattern that has gained popularity in recent years due to its ability to enable scalable and resilient software systems. EDA is a messaging-based architecture that allows for the decoupling of components in a software system, allowing them to communicate through events. These events can be thought of as notifications that are sent when something happens within the system, such as a user performing an action, a database update, or a sensor reading in an [[Internet of Things (IoT)]] device.
https://bitloops.com/docs/bitloops-language/learning/software-architecture/event-driven-architecture

#### Space-Based Architecture (SBA)
Space-based architecture is a software architecture pattern designed for highly-scalable, distributed systems that can handle large workloads and accommodate varying demand. It relies on the principles of partitioning and replication of data and processing components, allowing for parallelism, fault tolerance, and load balancing across the system.

The space-based architecture style is specifically designed to address problems involving high scalability, elasticity, performance, and high concurrency issues. It is often the architecture of choice for financial applications, gaming platforms, and large-scale simulations.
https://umairsaeed.com/space-based-architecture/

#### Microservices architecture
Microservices are a software development approach that has gained significant popularity in recent years. It is a modern architectural style where software applications are built as a collection of small, independent services that communicate with each other through [[API|APIs]].

Unlike traditional monolithic applications, where everything is tightly integrated, microservices are loosely coupled and can be deployed, managed, and scaled independently. This approach has several benefits, including better agility, scalability, and maintainability.

In modern software development, businesses need to deliver applications quickly and efficiently to meet ever-changing customer demands. Traditional monolithic applications have several drawbacks that make them ill-suited to meeting these needs.

As the application grows in complexity, it becomes increasingly difficult to maintain and scale. In contrast, microservices offer a way to build applications that can scale and evolve independently, enabling organizations to be more agile and responsive to changing market conditions.
https://bitloops.com/docs/bitloops-language/learning/software-architecture/microservices-architecture


#### SOA vs Microservices
A diferencia de los microservicios, SOA trata de que haya una mayor interoperabilidad entre los componentes y reusabilidad.