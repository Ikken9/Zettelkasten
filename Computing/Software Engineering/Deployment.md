# Deployment


## **CI/CD**
Stands for continuous integration and continuous delivery/deployment, aims to streamline and accelerate the software development lifecycle.

[Continuous integration](https://www.redhat.com/en/topics/integration?cicd=32h281b "Red Hat | Understanding enterprise integration") (CI) refers to the practice of [automatically](https://www.redhat.com/en/topics/automation?cicd=32h281b "Understanding automation") and frequently integrating code changes into a shared source code repository. [Continuous delivery](https://www.redhat.com/en/topics/devops/what-is-continuous-delivery?cicd=32h281b "What is continuous delivery?") and/or deployment (CD) is a 2 part process that refers to the integration, testing, and delivery of code changes. Continuous delivery stops short of automatic production deployment, while continuous deployment automatically releases the updates into the production environment.

Helps organizations avoid bugs and code failures while maintaining a continuous cycle of software development and updates.   
  
As apps grow larger, features of CI/CD can help decrease complexity, increase efficiency, and streamline workflows.

Because CI/CD automates the manual human intervention traditionally needed to get new code from a commit into production, downtime is minimized and code releases happen faster. And with the ability to more quickly integrate updates and changes to code, user feedback can be incorporated more frequently and effectively, meaning positive outcomes for end users and more satisfied customers overall.


## Deployment Patterns

#### **Canary releases**
A canary release is a method of spotting possible issues before they affect all consumers. Before making a new feature available to everyone, the plan is only to show it to a select group of users. We monitor what transpires after the feature is available in a canary release. If there are issues with the release, we fix them. We transfer the canary release to the actual production environment once its stability has been established.

#### **Blue/green deployments**
Here we have run two similar environments simultaneously, lowering risk and downtime. These surroundings are referred to be blue and green. Only one of the environments is active at any given moment. A router or load balancer that aids in traffic control is used in a blue-green implementation. The blue/green deployment also provides a quick means of performing a rollback. We switch the router back to the blue environment if anything goes wrong in the green environment.

#### **Feature toggles**
Here we can turn a switch on/off with feature toggles at runtime. We may roll out new software without exposing our users to any other brand-new or modified functionality. When we build new functionality, we can use feature toggles to enable continuous deployments by splitting releases from deployments.

#### **Rolling**
A rolling deployment is a deployment strategy that slowly replaces previous versions of an application with new versions of an application by completely replacing the infrastructure on which the application is running.

#### **A/B testing**
Two versions of an app are compared using A/B testing to see which one performs better. An experiment is like A/B testing. In A/B testing, we randomly present users with two or more page versions. Then, we use statistical analysis to determine which variant is more effective in achieving our objectives.

#### **Dark launches**
In a "dark launch," we introduce a new feature to a select group of users rather than the general public. These users must be aware that they are helping us test the functionality. We need to point out the new functionality to them. It is nicknamed a "dark launch" for this reason. Users are introduced to the program to get feedback and test its effectiveness.

### **Physical computers, Virtual Machines (VMs), and Containers**:

#### Physical Computers** (Bare Metal)
   - **Definition**: These are traditional physical machines where the hardware resources (CPU, memory, storage) are directly available to the operating system (OS).
   - **Resources**: Directly connected to the hardware components (e.g., processor, memory).
   - **Isolation**: None; the OS and applications run directly on the hardware. If the OS fails, all applications go down.
   - **Performance**: High, as there is no additional abstraction layer.
   - **Use Case**: Dedicated servers for workloads that require full access to the hardware, such as high-performance computing (HPC).

#### **Virtual Machines (VMs)**
   - **Definition**: VMs are software emulations of physical computers. They run on top of a **hypervisor**, which allows multiple VMs to share the physical hardware resources of a host system.
   - **Resources**: VMs are allocated virtualized hardware resources (CPU, memory, storage) that are managed by the hypervisor.
   - **Isolation**: Strong; each VM runs its own OS and is isolated from other VMs. If one VM fails, others are unaffected.
   - **Performance**: VMs generally have slightly lower performance than physical machines due to the overhead of virtualization.
   - **Use Case**: Running multiple different OS environments on a single physical server, isolating applications in separate environments for security or testing.

#### **Containers**
   - **Definition**: Containers are lightweight, virtualized environments that run on a shared host OS but are isolated from one another. They package applications with their dependencies, making them highly portable.
   - **Resources**: Containers share the host OS's kernel and resources, such as CPU and memory, but run in isolated user spaces.
   - **Isolation**: Moderate; containers are isolated using OS-level techniques (namespaces, cgroups) but share the same kernel. If the host OS crashes, all containers fail.
   - **Performance**: Higher than VMs since containers do not require a separate OS for each instance, leading to less overhead.
   - **Use Case**: Microservices architectures, lightweight application deployment, and scalable environments, such as Kubernetes.

### Key Differences:
| Feature               | Physical Computers          | Virtual Machines (VMs)          | Containers                     |
|-----------------------|-----------------------------|---------------------------------|--------------------------------|
| **OS Level**          | Single OS on hardware       | Each VM has its own OS          | Shared OS kernel across containers |
| **Resource Allocation**| Direct access to hardware   | Virtualized hardware per VM     | Shared resources, isolated environments |
| **Isolation**         | No isolation between apps   | Strong isolation between VMs    | Moderate isolation, shared kernel |
| **Performance**       | Maximum performance         | Slightly lower due to virtualization | Higher than VMs, close to native |
| **Overhead**          | No overhead                 | Hypervisor overhead             | Minimal overhead                |
| **Use Case**          | High-performance tasks      | Running multiple OS environments | Lightweight, portable apps, microservices |

In summary:
- **Physical computers** provide direct access to hardware with maximum performance but no flexibility or isolation between different applications.
- **Virtual machines** offer strong isolation with the ability to run multiple OS environments on the same hardware but with some performance overhead.
- **Containers** are lightweight, provide efficient resource usage, and are faster to start, but they share the host OS kernel, leading to slightly less isolation than VMs.