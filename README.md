
# Intelligent Traffic Management System

## Project Description
The *Intelligent Traffic Management System* is a machine learning-based solution aimed at improving traffic flow in busy intersections. Unlike the traditional round-robin method (referred to as *Cyclic Fixed-Time Control*) where each lane is given a green light sequentially for a fixed period, this system dynamically allocates green light time based on the real-time traffic volume in each lane. This allows for more efficient management of traffic, reducing congestion and wait times.

## Key Features
- *Vehicle Detection Model*: The system uses a trained machine learning model to count the number of vehicles in each lane.
- *Dynamic Traffic Control*: The lane with the highest traffic volume is prioritized for green light allocation.
- *Cycle Time*: The system runs on a 150-second cycle, dynamically updating green light allocation every 30 seconds.
- *Priority Handling*: If any lane has not received a green light during the cycle, it is automatically prioritized based on lane hierarchy.

## Working Logic
1. *Vehicle Detection*: Cameras are placed in front of each lane (Lane 1, 2, 3, and 4) to detect and count the number of vehicles.
2. *Green Light Allocation*:
   - The system starts by comparing the number of vehicles in all four lanes.
   - The lane with the maximum number of vehicles is given a *green light* for 30 seconds.
   - After the first lane's green light, the system compares the remaining lanes and gives the next green light to the lane with the most vehicles.
   - This process repeats every 30 seconds for a total of 150 seconds.
3. *Handling Unserved Lanes*:
   - If, after the 150-second cycle, one or more lanes have not yet received a green light, those lanes are given priority.
   - If multiple lanes are unserved, the lane priority system is followed (Lane 1 > Lane 2 > Lane 3 > Lane 4) to determine the order of green light allocation.
4. *Priority System*:
   - If, for example, Lane 2 and Lane 4 haven't received a green light, Lane 2 will be opened for 30 seconds, followed by Lane 4.

## Technologies Used
- *Python*: The primary programming language for implementing the logic.
- *OpenCV*: Used for vehicle detection and image processing.
- *Machine Learning*: A vehicle counting model trained using labeled data.
- *NumPy/Pandas*: For data processing and manipulation.
- *Time-Based Simulation*: The system runs on a 150-second loop with 30-second green light intervals.

## Future Enhancements
- *Support for pedestrian crossings* and emergency vehicle detection.
- *Traffic prediction algorithms* based on historical data.
