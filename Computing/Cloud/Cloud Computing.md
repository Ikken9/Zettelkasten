# Cloud Computing

Cloud computing is the delivery of computing services over the internet. Computing services include common IT infrastructure such as virtual machines, storage, databases, and networking. Cloud services also expand the traditional IT offerings to include things like Internet of Things (IoT), machine learning (ML), and artificial intelligence (AI).

Because cloud computing uses the internet to deliver these services, it doesn’t have to be constrained by physical infrastructure the same way that a traditional datacenter is. That means if you need to increase your IT infrastructure rapidly, you don’t have to wait to build a new datacenter—you can use the cloud to rapidly expand your IT footprint.


## Shared Responsibility Model
The shared responsibility model in cloud computing defines how responsibilities are divided between the cloud provider and the consumer. In a traditional corporate datacenter, the company handles everything, including physical security and maintaining infrastructure. In the cloud, these responsibilities are split: the cloud provider manages physical aspects like security, power, and connectivity, while the consumer is responsible for data, access security, and specific configurations.

Responsibilities vary based on the cloud service type:
- **IaaS (Infrastructure as a Service):** The consumer has more responsibilities, such as maintaining the operating system and applications.
- **PaaS (Platform as a Service):** Responsibilities are shared more equally between the provider and consumer.
- **SaaS (Software as a Service):** The provider takes on most responsibilities, leaving the consumer mainly in charge of data and access.

When using a cloud provider, you’ll always be responsible for:
- The information and data stored in the cloud
- Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
- The accounts and identities of the people, services, and devices within your organization

The cloud provider is always responsible for:
- The physical datacenter
- The physical network
- The physical hosts

Your service model will determine responsibility for things like:
- Operating systems
- Network controls
- Applications
- Identity and infrastructure

This model helps clarify who is responsible for what, depending on the service type.


## Cloud Models
What are cloud models? The cloud models define the deployment type of cloud resources. The three main cloud models are: private, public, and hybrid.

#### Private cloud
Let’s start with a private cloud. A private cloud is, in some ways, the natural evolution from a corporate datacenter. It’s a cloud (delivering IT services over the internet) that’s used by a single entity. Private cloud provides much greater control for the company and its IT department. However, it also comes with greater cost and fewer of the benefits of a public cloud deployment. Finally, a private cloud may be hosted from your on site datacenter. It may also be hosted in a dedicated datacenter offsite, potentially even by a third party that has dedicated that datacenter to your company.

Nube dedicada para la compania cliente

#### Public cloud
A public cloud is built, controlled, and maintained by a third-party cloud provider. With a public cloud, anyone that wants to purchase cloud services can access and use resources. The general public availability is a key difference between public and private clouds.

No es dedicada para el cliente, publicamente disponible, planes pre-establecidos.

#### Hybrid cloud
A hybrid cloud is a computing environment that uses both public and private clouds in an inter-connected environment. A hybrid cloud environment can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources. Hybrid cloud can be used to provide an extra layer of security. For example, users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure.

Mezcla de las anteriores.

#### Multi-cloud
A fourth, and increasingly likely scenario is a multi-cloud scenario. In a multi-cloud scenario, you use multiple public cloud providers. Maybe you use different features from different cloud providers. Or maybe you started your cloud journey with one provider and are in the process of migrating to a different provider. Regardless, in a multi-cloud environment you deal with two (or more) public cloud providers and manage resources and security in both environments.

El cliente consume los servicios de multiples proveedores.

### Consumption-based model
When comparing IT infrastructure models, there are two types of expenses to consider. Capital expenditure (CapEx) and operational expenditure (OpEx).

CapEx is typically a one-time, up-front expenditure to purchase or secure tangible resources. A new building, repaving the parking lot, building a datacenter, or buying a company vehicle are examples of CapEx.

In contrast, OpEx is spending money on services or products over time. Renting a convention center, leasing a company vehicle, or signing up for cloud services are all examples of OpEx.

Cloud computing falls under OpEx because cloud computing operates on a consumption-based model. With cloud computing, you don’t pay for the physical infrastructure, the electricity, the security, or anything else associated with maintaining a datacenter. Instead, you pay for the IT resources you use. If you don’t use any IT resources this month, you don’t pay for any IT resources.

This consumption-based model has many benefits, including:
- No upfront costs.
- No need to purchase and manage costly infrastructure that users might not use to its fullest potential.
- The ability to pay for more resources when they're needed.
- The ability to stop paying for resources that are no longer needed.

With a traditional datacenter, you try to estimate the future resource needs. If you overestimate, you spend more on your datacenter than you need to and potentially waste money. If you underestimate, your datacenter will quickly reach capacity and your applications and services may suffer from decreased performance. Fixing an under-provisioned datacenter can take a long time. You may need to order, receive, and install more hardware. You'll also need to add power, cooling, and networking for the extra hardware.

In a cloud-based model, you don’t have to worry about getting the resource needs just right. If you find that you need more virtual machines, you add more. If the demand drops and you don’t need as many virtual machines, you remove machines as needed. Either way, you’re only paying for the virtual machines that you use, not the “extra capacity” that the cloud provider has on hand.


## Some concepts

#### Load Balancers
- **Explanation:** Devices or software that distribute network or application traffic across multiple servers.
- **Common Cloud Providers:** AWS Elastic Load Balancing, Azure Load Balancer, Google Cloud Load Balancing.

#### API Gateways
- **Explanation:** Entry points for clients to interact with backend services, managing API traffic, security, and routing.
- **Common Cloud Providers:** AWS API Gateway, Azure API Management, Google Cloud API Gateway.

#### Firewalls
- **Explanation:** Network security devices that monitor and control incoming and outgoing network traffic based on security rules.
- Common Cloud Providers:** AWS Security Groups, Azure Firewall, Google Cloud Firewall.

#### Web Application Firewall (WAF)
A WAF or web application firewall helps protect web applications by filtering and monitoring HTTP traffic between a web application and the Internet. It typically protects web applications from attacks such as cross-site forgery, cross-site-scripting (XSS), file inclusion, and SQL injection, among others.

#### Virtual Private Cloud (VPC)
- Explanation:** Isolated network environments within a cloud provider's infrastructure for hosting resources securely.
- **Common Cloud Providers:** AWS VPC, Azure Virtual Network, Google Cloud VPC.

#### Auto Scaling
- **Explanation:** Automatically adjusts computing resources based on demand to maintain performance and optimize costs.
- *Common Cloud Providers:** AWS Auto Scaling, Azure Virtual Machine Scale Sets, Google Cloud Auto Scaling.

#### Identity and Access Management (IAM)
- Explanation:** Framework for managing and controlling access to cloud resources.
- **Common Cloud Providers:** AWS IAM, Azure Active Directory, Google Cloud IAM.

#### Content Delivery Network (CDN)
- **Explanation:** Distributed network of servers that deliver web content and resources to users based on their geographic location.
- Common Cloud Providers:** AWS CloudFront, Azure CDN, Google Cloud CDN.