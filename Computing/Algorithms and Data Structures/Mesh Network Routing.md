# Mesh Network Routing

We want an algorithm that can efficiently route between two nodes separated by a distance of $n$-hops. It's necessary to determine the bests paths from the starting node to the target node, as they can be many, we want to balance the load to send the packets via different paths to avoid bottlenecks and node overloading. 

For example, the number of best suited paths between two nodes at a distance of $n$-hops can be 10, but instead of dividing the traffic between the 10 paths, we only send the packets through the best 5 paths in terms of cost.

## **Algorithm**
todo!
https://github.com/Ikken9/heroin
https://stackoverflow.com/questions/69665188/min-max-of-vecf64-trait-ord-is-not-implemented-for-xy





### **Key Factors for Edge Cost Calculation**
The edge cost calculation can vary depending on the parameters that we take into account.

#### **Latency-Bandwidth Ratio**
A simple approach that balances latency and bandwidth is using their ratio. This method assumes that lower latency and higher bandwidth are both desirable.

$$
\text{cost} = \frac{\text{latency}}{\text{bandwidth}}
$$
- **Pros**: Easy to implement and provides a simple balance.
- **Cons**: Bandwidth might dominate the formula if latency is low.


#### **Weighted Sum**
https://en.wikipedia.org/wiki/Weighted_sum_model
In many cases, it's desirable to give more importance to one factor over another, like minimizing latency for real-time applications or maximizing bandwidth for high-throughput applications. The WSM method can be used to prioritize certain factors:

$$
\text{cost} = w_{\text{latency}} \times \text{latency} + w_{\text{bandwidth}} \times \frac{1}{\text{bandwidth}}
$$

where:
- $w_{\text{latency}}$ is the weight for latency (a larger value will prioritize low-latency paths).
- $w_{\text{bandwidth}}$ is the weight for bandwidth (a larger value will prioritize high-bandwidth paths).

- **Pros**: Flexibility to adjust based on the specific requirements of the network.
- **Cons**: It's necessary to experimentally determine the correct weights for the use case.


### **Logarithmic Cost**
For networks where the range of bandwidth and latency values can vary significantly (e.g., from very high bandwidths to very low ones), a logarithmic function can be used to smooth out extreme values:

$$
\text{cost} = \log(1 + \text{latency}) - \log(1 + \text{bandwidth})
$$

- **Pros**: Handles extreme values more gracefully, preventing very large or very small values from dominating the cost function.
- **Cons**: More complex and may not always give the most intuitive results.
