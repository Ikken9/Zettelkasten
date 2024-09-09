# gRPC

**gRPC** is a modern open source high performance **Remote Procedure Call** **(RPC)** framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

In gRPC, a client application can directly call a method on a server application on a different machine as if it were a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just a client in some languages) that provides the same methods as the server.


### What is RPC?
In RPC, client-server communications operate as if the client API requests were a local operation, or the request was internal server code.

In RPC, a client sends a request to a process on the server that is always listening for remote calls. In the request, it contains the server function to call, along with any parameters to pass. An RPC API uses a protocol like HTTP, TCP, or UDP as its underlying data exchange mechanism.

### Working with Protocol Buffers
By default, gRPC uses Protocol Buffers, Google’s mature open source mechanism for serializing structured data (although it can be used with other data formats such as JSON). Here’s a quick intro to how it works. If you’re already familiar with protocol buffers, feel free to skip ahead to the next section.

The first step when working with protocol buffers is to define the structure for the data you want to serialize in a _proto file_: this is an ordinary text file with a `.proto` extension. Protocol buffer data is structured as _messages_, where each message is a small logical record of information containing a series of name-value pairs called _fields_.


## When to use gRPC vs. REST
[[REST]] is currently the most popular API architecture for web services and microservice architectures. REST’s popularity is due to its simple implementation and data structure mapping, readability, and flexibility. It’s easy for new programmers to start developing RESTful APIs for their applications, whether for web services development or internal microservices.

Here are use cases for a REST API:

- Web-based architectures
- Public-facing APIs for ease of understanding by external users
- Simple data communications

gRPC, unlike REST, was designed specifically to allow developers to create high-performance APIs for microservice architectures across distributed data centers. It’s better suited for internal systems that require real-time streaming and large data loads. gRPC is also a good fit for microservice architectures comprising several programming languages when the API is unlikely to change over time.

A gRPC API is better for these use cases:

- High-performance systems
- High data loads
- Real-time or streaming applications