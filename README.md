# Robotic-Arm
## Overview
This is a side project of mine in an attempt to create a 4 axis robotic arm.

## Design
The project was designed in Fusion 360 and utilizes multiple cycloidal gearboxes of varying sizes
and ratios. The arm also implements several metal bearings and dowel pins for decreased friction
between components, ultimately leading to increased gearbox efficiency.

## Electrical
The arm utilizes four, 200 step Nema 17 motors on an open-loop feedback system. Each motor is
controlled by a TMC 2209 with 8 micro steps enabling for a total of 1600 micro steps per rotation.
These motor controllers are attached to an Arduino UNO with a CNC shield extension to manage axis
X, Y, Z, and A.

## Software
The arm motor code runs on an Arduino UNO using the AccelStepper library. The software uses relative
position based off the counted steps to approximate the current location of the robot without encoder
feedback.

## Current Checklist
### F - Finalized | C - Complete | I - In Progress | X - Not Started
### Section - Status
- Robot Base Model - I
- Robot Lower Limb Model - C
- Robot Upper Limb Model - C
- Robot Wrist Model - X
- Robot Wiring - X
- Motor Code - I
- Camera Vision Code - I

## Notes
- Look into implementing ROS on raspberry pi
- Possibly use logic level converter between PI and UNO
- Larger power supply 10A Power Bench
- Custom PDP and encoders?
