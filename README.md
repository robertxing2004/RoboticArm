# StrongArm - A Robotic Arm Project
A Software Engineering Design Project for ICS4UI.
Project By Sean W, Daniel E, Robert X and Steven M

### What is it? 

StrongArm is an ambitious project that combines hardware and software. The inspiration for this project came when we saw how inefficient modern-day ship yards are. In order to load a ship, multiple workers have to manually operate very complex machines, which are expensive, hard to maintain and dangerous. Not to mention, the amount of human errors that can occur is mind-boggling. You often see containers delivered to wrong locations due to human errors.  Because of this, companies have to spend more money getting everything fixed while the customer is getting angry because their shipment is delayed once again. What if there’s a better way to do this through the use of technology? That’s where we came up with the idea for StrongArm.

The StrongArm platform is built to be a simulation for the actual shipyard. Essentially, we have a camera that checks where a container is. Then, the user is able to move the container wherever they want using our simple and super intuitive UI. This command then gets sent to our hardware component, which physically moves the boxes without any workers. This process can be repeated to sort all the boxes. This process can also be automated, but we do not plan to implement that feature at the current stage of development. 


### How To Use

![alt text](opencv_frame.png)

Sample computer vision frame

To use this product, please refer to our user manual:
https://docs.google.com/document/d/1IBoCJequiSFqITuXN23gAgejYG0clhTA1TldQzqMFVI/edit?usp=sharing


### What was used? (Tech Stack)

Processing (Frontend)
- G4P UI Design Tool
- Serial 

Python (Backend)
- Socket
- PySerial
- OpenCV
- CMake
- GCC

Arduino:
- Servo 
- Stepper
- Software Serial