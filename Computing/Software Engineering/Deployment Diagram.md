  
# Deployment Diagram

Hardware devices, processors and software execution environments (system Artifacts) are reflected as Nodes, and the internal construction can be depicted by embedding or nesting Nodes. Deployment relationships indicate the deployment of Artifacts, and Manifest relationships reveal the physical implementation of Components. As Artifacts are allocated to Nodes to model the system's deployment, the allocation is guided by the use of Deployment Specifications. A Deployment diagram can also indicate that a Node has a State, or show an instance of a Node with an actual run-time value for the state, representing a specific condition or scenario.

![deployment_diagram](deploymentdiagram1.png)

Deployment diagrams are ideal for applying alternative images to depict the objects that the elements represent. Such images can be substituted for the elements in the diagram, as shown here:

![deployment_diagram2](deploymentdiagram2.png)


- [Nodes in UML models](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cnode.html)  
    In UML models, nodes are model elements that represent the computational resources of a system, such as personal computers, sensors, printing devices, or servers. Nodes can be connected by communication paths to describe network structures.
- [Node instances](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cnodeinst.html)  
    In UML modeling, a node instance is a model element that represents an instantiation, or actual occurrence, of a node. Node instances are based on existing nodes.
- [Execution environments](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cexecenviro.html)  
    In UML modeling, an execution environment is a type of node that represents a particular execution platform, such as an operating system or a database management system. You can use execution environments to describe the context in which the execution of a model takes place.
- [Artifacts](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cartifact.html)  
    In UML models, artifacts are model elements that represent the physical entities in a software system. Artifacts represent physical implementation units, such as executable files, libraries, software components, documents, and databases.
- [Artifact instances](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cartinst.html)  
    In UML modeling, an artifact instance is a model element that represents an instantiation, or actual occurrence, of an artifact. Artifact instances are based on existing artifacts.
- [Devices](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cdevice.html)  
    In deployment diagrams, a device is a type of node that represents a physical computational resource in a system, such as an application server.
- [Deployment specifications](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/cdeployspec.html)  
    A deployment specification is essentially a configuration file, such as an XML document or a text file, that defines how an artifact is deployed on a node.
- [Relationships in deployment diagrams](https://www.ibm.com/docs/en/SS8PJ7_9.7.0/com.ibm.xtools.modeler.doc/topics/crelsme_depd.html)  
    In UML, a relationship is a connection between model elements. A UML relationship is a type of model element that adds semantics to a model by defining the structure and behavior between model elements.


### Nodes
A **node** is a physical or logical resource that has the capacity to process, store, or transport data. In a deployment diagram, nodes represent the hardware elements or execution environments where the system's components are deployed.

**Types of Nodes:**
- **Physical Nodes:** Represent physical devices such as servers, workstations, routers, mobile devices, etc.
- **Logical Nodes:** Represent virtual environments or software that provides specific services, such as virtual machines, Docker containers, application servers, etc.

**Node Components:**
- A node can have internal components like processors, storage units, memory, and other hardware resources, but in UML modeling, the focus is on the node as a unit that executes software components.

**Example:**
- A server in a data center that runs multiple applications.

### Components
A **component** in a deployment diagram represents a modular unit of software or part of the system that can be deployed and executed within a node. Components are pieces of code that offer a set of functionalities and can be implementations of classes, modules, libraries, web services, etc.
 
**Relationship with Nodes:**  
- Components are "hosted" or deployed on nodes. This means that a component depends on a node for its execution, and the node provides the necessary hardware or software environment for the component to function.

**Types of Components:**
- **Software Components:** Modules, microservices, applications, etc., that perform specific tasks.
- **Artifacts:** A special type of component that includes executables, configuration files, scripts, databases, etc.

**Example:**
- A web application deployed on a server.