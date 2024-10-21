# HTTP



## **Methods**
1. **GET**: Retrieve data from the server (e.g., fetching a resource).
2. **POST**: Submit data to the server, often used to create a new resource.
3. **PUT**: Update or replace an existing resource on the server.
4. **PATCH**: Apply partial updates to an existing resource.
5. **DELETE**: Remove a resource from the server.
6. **HEAD**: Similar to GET, but retrieves only the headers, not the body of the response.
7. **OPTIONS**: Retrieve the supported methods for a resource, often used for CORS (Cross-Origin Resource Sharing) checks.
8. **TRACE**: Echoes back the received request, useful for testing/debugging.


**PATCH** and **POST** are **not idempotent**:
- **PATCH** might modify different parts of a resource if called multiple times.
- **POST** typically creates a new resource, and calling it repeatedly creates additional resources.