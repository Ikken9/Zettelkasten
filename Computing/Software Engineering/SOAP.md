# SOAP

**SOAP** (formerly known as **Simple Object Access Protocol**) is a lightweight protocol for the exchange of information in a decentralized, distributed environment. A SOAP message is a transmission of information from a sender to a receiver. SOAP messages can be combined to perform request/response patterns.

SOAP is transport independent but is most commonly carried over HTTP in order to run with the existing Internet infrastructure.  SOAP enables the binding and usage of discovered Web services by defining a message path for routing messages. SOAP is used to query UDDI for Web services.

SOAP is an XML-based protocol that defines three parts to every message:

##### Envelope:  
- The envelope defines a framework for describing what is in a message and how to process it.  A SOAP message is an envelope containing zero or more headers and exactly one body.  The envelope is the top element of the XML document, providing a container for control information, the address of a message, and the message itself.  Headers transport any control information such as quality-of-service attributes.  The body contains the message identification and its parameters.  Both the headers and the body are child elements of the envelope.
##### Encoding rules:  
- The set of encoding rules expresses instances of application-defined data types. Encoding rules define a serialization mechanism that can be used to exchange instances of application-defined data types. SOAP defines a programming language-independent data type scheme based on XSD plus encoding rules for all data types defined according to this model. SOAP encoding is not WS-I compliant and thus the Literal use (which is no encoding) is suggested for interoperable Web services and required for WS-I compliance.
##### Communication styles:
- Communications can follow a remote procedure call (RPC) or message-oriented (Document) format.