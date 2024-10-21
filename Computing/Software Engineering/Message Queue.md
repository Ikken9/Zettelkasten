# Message Queue

A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures. Messages are stored on the queue until they are processed and deleted. Each message is processed only once, by a single consumer. Message queues can be used to decouple heavyweight processing, to buffer or batch work, and to smooth spiky workloads.
Is a component of messaging middleware solutions that enables independent applications and services to exchange information.

Message queues allow different parts of a system to communicate and process operations asynchronously. A message queue provides a lightweight buffer which temporarily stores messages, and endpoints that allow software components to connect to the queue in order to send and receive messages. The messages are usually small, and can be things like requests, replies, error messages, or just plain information. To send a message, a component called a producer adds a message to the queue. The message is stored on the queue until another component called a consumer retrieves the message and does something with it.

## Benefits

#### Reliable message delivery:
Using a message queue can ensure that business-critical messages between applications will not be lost and that they will only be delivered to the recipient once. With this feature in place, additional de-duplication or loss-prevention logic is unnecessary.  

#### Inter-application connectivity:
Some message queue solutions can handle message encryption, transactionality and other communication aspects between applications and services. This simplifies application development and enables disparate architectures to work together.  

#### Versatility:
Message queue solutions can support multiple languages, such as Java, Node.js, COBOL, C/C++, Go, .NET, Python, Ruby, and C#. They can also support numerous application programming interfaces ([[API|APIs]]) and protocols, including MQTT, AMQP, [[REST]] and many others.  

#### Resilience:
Asynchronous messaging ensures application-specific faults won’t impact the system. If one component in the system stalls, all others can continue interacting with the queue and processing messages. This decreases the chance that the entire system’s stability will be impacted by one part’s failure.  

#### Improved security:
A message queue may be able to identify and authenticate all messages. In some message queue solutions, they can be set to encrypt messages at rest, in transit or end-to-end. This can contribute to the overall security of the applications and infrastructure.  

#### Integrated file transfers:
Some message queue solutions include additional features, such as the ability to transfer files. This can be used as an alternative to FTP within enterprises where such solutions are in use.