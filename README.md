# Network-Message-Broadcast-Simulation

# Optimizing Distribution In Networks With Multiple Starting Nodes Combinations 


# Introduction

In this project, we aim to optimize the data broadcasting protocol in networks, especially decentralized networks, within a specifically selective dead node environment scenario. The goal is to ensure that all active nodes in the network receive the data while maintaining the untraceability of the data origin. We will analyze the best starting nodes for achieving optimal efficiency. To simulate and analyze the system, we will implement a 2D Cellular Automata simulation using Python.
This experiment encompasses and can be used for all environments that have a broadcast-to-immediate-neighbors nature of distribution, such as: spread of a viral disease like Covid-19, spreading any information or rumor in a human population density, spreading of a spray like a disinfectant or air freshener inside a building for fastest full coverage speed, etc.

# Problem Statement

In decentralized networks, it is crucial to efficiently broadcast data to all active nodes while considering challenges such as selective dead nodes and full mesh scenarios. Additionally, preserving the untraceability of the data origin is essential for maintaining privacy and security. The problem can be summarized as follows:
Design an optimized data broadcasting protocol that ensures all active nodes receive the data.
Address the challenges posed by selective dead node environments and full mesh scenarios.
Develop a shortest path selection method for efficient data propagation.
Maintain the untraceability of the data origin by limiting data transmission to adjacent nodes.

# System Design and Modeling

In our project, we aim to optimize the data broadcasting protocol in decentralized networks within selective dead node and full mesh scenarios. Our goal is to ensure that all active nodes in the blockchain network receive the data while maintaining the untraceability of the data origin. To achieve this, we have developed a detailed system design and modeling approach that incorporates stochastic processes and control strategies to optimize efficiency in the data broadcasting process.

The system architecture consists of a 2-dimensional grid, where each block represents a node in the decentralized network. Nodes communicate with their adjacent nodes by transferring data, creating a peer-to-peer network structure.

We have designed an optimized data broadcasting protocol that guarantees all active nodes receive the data. Our protocol utilizes a shortest path selection method to determine the most efficient path for data propagation. To ensure the untraceability of the data origin, we limit data transmission only to adjacent nodes.

We have also considered the presence of unresponsive nodes in the network. These nodes cannot receive or transmit data, and we have implemented mechanisms to handle their presence during the data broadcasting process.

# Simulation and Analysis

To simulate real-world uncertainties, we have introduced stochastic processes in our modeling approach. These processes capture the responsiveness of nodes and network conditions. By introducing randomness, we account for variations in the behavior of nodes and network connectivity.

Our modeling approach includes a 2D Cellular Automata simulation implemented using Python. The simulation accurately models the decentralized network, defining the rules and behaviors of nodes, data transmission, node responsiveness, and interaction with adjacent nodes. The developed data broadcasting protocol and control strategies are integrated into the simulation for comprehensive analysis.

We are continuously optimizing our protocol by analyzing the simulation results. We fine-tune the selection of starting nodes to achieve optimal efficiency, considering the number of steps required to propagate data to all responsive nodes.

To manage the scope of the system the number of nodes have been selected in the range 1 to 4 while their positions are initially random but are changed according to circumstances.

The Simulation environment is shown below where the initial node is [32:23]. Gray blocks represent data transferred nodes and black blocks represents unresponsive nodes :



# Experimental Validation

As part of our evaluation, we define a metric to assess the efficiency of the data broadcasting protocol. Our primary focus for efficiency is the number of steps taken until all responsive nodes receive the data.

The following pattern of unresponsive blocks is used for all evaluations of this system as it covers all variations of possible situations:


By employing our detailed system design and modeling approach, we can optimize the efficiency of the data broadcasting protocol in decentralized networks. The 2D Cellular Automata simulation serves as a powerful tool for testing and analyzing the system, enabling us to evaluate different starting nodes and scenarios and apply various optimization techniques.

To find the optimum position in a multi initial point system we are using the Reinforced learning algorithm. Although it is not 100% accurate, the inaccuracy is not substantial enough to discard the results.

# Results

The results of the experiments are shown below, the coordinates are in the format Y, X:  

Initial starting points: 			1
Number of minimum steps: 		81
Coordinates of the minimum steps:
43 , 9




Initial starting points: 			2
Number of minimum steps: 		45
Coordinates of the minimum steps:
45, 39    12, 16
45, 39    14, 18
45, 39    14, 19
45, 40    13, 17
45, 40    14, 18
45, 40    15, 19
46, 40    13, 18
46, 40    15, 19
46, 41    12, 16
46, 41    13, 17
47, 41    12, 16
47, 41    12, 17
47, 41    13, 17
47, 41    13, 18
47, 41    14, 18
47, 41    14, 19
47, 41    15, 19
47, 42    13, 17
47, 42    14, 18




Initial starting points: 			3
Number of minimum steps: 		38
Coordinates of the minimum steps:
41, 46    27, 16    9, 21
41, 47    27, 16    9, 21
42, 45    27, 17    9, 20
41, 44    27, 17    9, 20
39, 44    27, 17    9, 20
41, 44    27, 18    9, 20
42, 45    27, 18    9, 20
43, 46    29, 18    9, 21
43, 46    28, 18    9, 20
41, 46    28, 18    9, 20
41, 46    29, 18    9, 21
42, 47    29, 18    9, 21
42, 45    29, 18    9, 21
42, 45    27, 17    9, 21



Initial starting points: 			4
Number of minimum steps: 		32
Coordinates of the minimum steps:
39, 44    30, 9    11, 21    23, 43
39, 44    30, 9    11, 21    25, 41
39, 44    30, 9    11, 21    23, 41
39, 44    30, 9    11, 23    23, 41
39, 44    30, 8    11, 21    25, 43
39, 44    30, 9    11, 21    25, 43
41, 42    30, 8    11, 21    23, 40
41, 42    31, 8    11, 22    23, 40


Note: The coordinate combination lists are not exhaustive but are only a few examples of the possible combinations and a simulation example of only one combination is added for better visualization. 

# Analysis

From these results it can be concluded that the number of steps required to reach all nodes Decrease as the number of Initial points Increase however adding additional initial points reduce the percentage of improvement as each initial point is added.




