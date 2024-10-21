# Resilience

In the context of software systems, it refers to the ability of a system to continue functioning properly despite failures, disruptions, or unexpected conditions. A resilient system can handle errors, recover from faults, and maintain an acceptable level of performance and availability even under stress.

Key aspects of resilience include:

- **Fault tolerance**: The system can manage failures in components without crashing.
- **Self-recovery**: The system can recover from errors automatically or through graceful degradation.
- **Redundancy**: Having backup components to ensure system continuity.
- **Scalability**: The system can adjust to varying levels of load or resource availability.

Resilience helps ensure the system is robust, reliable, and capable of sustaining disruptions or failures with minimal impact on users.


## **What a system has to have to be resilient?**
To be resilient, a system needs several key attributes and mechanisms that enable it to withstand, recover from, and adapt to failures, disruptions, or varying conditions. These include:

1. **Fault Tolerance**: The ability to continue operating even when components fail. This can be achieved through:
   - **Redundancy**: Duplicate components or services (e.g., backup servers, databases) that take over in case of a failure.
   - **Failover Mechanisms**: Automatic switching to a standby system or component when a failure occurs.

2. **Error Handling**: The system must gracefully handle errors or unexpected inputs without crashing. This includes:
   - **Exception Handling**: Managing runtime errors without stopping the application.
   - **Graceful Degradation**: Reducing functionality without complete failure if certain parts of the system malfunction.

3. **Recovery Mechanisms**: The system should be able to recover from faults or outages. Key methods include:
   - **Self-Healing**: Automated recovery actions (e.g., restarting failed services).
   - **Checkpoints and Rollbacks**: Ability to return to a stable state after a failure.

4. **Scalability**: Ability to handle varying loads by dynamically adjusting resources, ensuring performance under different conditions.

5. **Monitoring and Alerts**: Continuous observation of system health with alerts for potential issues, enabling proactive detection and mitigation of problems.

6. **Distributed Architecture**: Using microservices, containers, or distributed systems that isolate failures, ensuring one component's failure doesn’t bring down the entire system.

7. **Load Balancing**: Distributing traffic across multiple servers or instances to prevent overload and ensure high availability.

8. **Data Replication**: Keeping data copies across different locations (e.g., databases, file systems) to ensure no data loss in case of a failure.

9. **Security**: Protection against malicious disruptions, such as attacks or unauthorized access, is critical for maintaining resilience.


## **Techniques**

#### **Circuit Breaker Pattern**
This technique helps prevent a failure from cascading through a system. If a service repeatedly fails, the circuit breaker opens, preventing further requests to the failing service. After a cooldown period, it will attempt to close and allow requests again if the service recovers.

#### **Retry Pattern**
Automatically retries a failed operation (e.g., [[API]] call, database query) after a short delay, assuming the failure is transient. This is often combined with **exponential backoff**, where each retry occurs after increasing time intervals.

#### **Load Balancing**
Distributes incoming requests across multiple servers or instances to ensure no single server is overwhelmed. This improves performance and ensures the system remains available even if one server fails.

#### **Data Replication**
Keeps copies of data across multiple nodes, regions, or data centers, ensuring that data is still accessible even if one copy is lost.

#### **Sharding**
Splits data or workloads across different servers (or shards), so each shard handles a portion of the data or traffic. If one shard fails, it doesn’t affect the others.

#### **Graceful Degradation**
When part of the system fails, the system continues to operate with reduced functionality rather than completely crashing.

#### **Self-Healing**
Automation systems detect failure and recover without human intervention. For instance, a failed server or service can automatically be restarted or replaced.
#### **Chaos Engineering**
This technique involves intentionally introducing failures into the system (e.g., shutting down random services) to test how well the system handles unexpected faults and if it can recover smoothly.

#### **Bulkhead Pattern**
Isolates different parts of a system into separate "compartments" or **pools of resources**, so that if one part fails, the failure doesn’t spread to other parts.

#### **Rate Limiting**
Limits the number of requests a service can handle in a given time period, preventing overload by rejecting excessive requests.