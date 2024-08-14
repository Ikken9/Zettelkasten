### RAM Banks

RAM banks refer to groups of memory chips on a memory module (such as a DIMM or SO-DIMM) that can be accessed independently or in parallel by the memory controller. Here's a more detailed breakdown:

1. **Bank Groups**: A memory module can be divided into multiple bank groups, with each bank group containing multiple banks. Each bank is a distinct storage area within the memory module.
    
2. **Interleaving**: Bank interleaving allows the memory controller to access different banks simultaneously or in quick succession, improving overall memory throughput and reducing latency.
    
3. **Addressing**: Each bank within a memory module has its own set of address registers, allowing the memory controller to specify which bank to access during a read or write operation.

### Single Rank Memory Array Architecture

The term "rank" in memory architecture refers to a set of memory chips that are accessed simultaneously. A "rank" is essentially a set of memory chips on a module that are activated together to form a 64-bit (or 72-bit with ECC) data bus.

