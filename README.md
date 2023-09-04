# **Mars Tank Prototype Rover Project**

This is a personal project with the goal of creating a fully autonomous Mars Tank Prototype Rover. Various different sensors and techniques will be utilized to achieve autonomous travel.

## Objectives and Motivation

During my grade 11 year, I developed an interest in electrical and computer engineering, as well as programming, through my previous experiences with Arduino and Python programming. To further explore these interests, I decided to embark on a project involving a Raspberry Pi and Python programming. I undertook the challenge of constructing my own rover to practice Python programming, embedded systems design, PCB design, and other technical skills I aimed to learn and improve.

# Table of Contents

- [Parts List](#parts-list)
- [Current Build](#current-build)
     * [PCB Addition](#pcb-addition)
- [Mobilizing the Rover](#mobilizing-the-rover)
     * [Remote Control via PS4 Controller](#remote-control-rover-via-PS4-controller)
     * [Remote Control via Webservers](#remote-control-via-webservers)
       + [HTML Based Server](#html-based-server)
       + [Node-RED Server](#node-red-server)
 - [Autonomous Rover Programs](#autonomous-rover)
   * [Obstacle Avoidance Rover](#obstacle-avoidance-rover)
- [Future Plans](#future-plans)

## Parts List

The following is the up-to-date parts list for the project:

1. Bogie Runt Rover Kit from ServoCity (Includes 6 140RPM Motors) 
2. 2 Lithium Polymer batteries rated at 3.7V 2000 mAh 
3. 2x7A Roboclaw Motor Controller
4. Raspberry Pi 4 (8GB RAM)
5. Half-Size Breadboard
6. 3 HD-SR04 Ultra Sonic Range Sensors
7. Anker 20100 mAh Battery Pack
8. PS4 Controller
9. Jumper Wires

# Current Build

The images below show version 2.0 of the current rover design. From version 1, there were a lot of design changes made to make the rover more streamlined. Removed sensors that may not serve a function for autonomous travel as well as a new battery supply for the Pi, rearranging the components to help with the center of mass, and adding 2 more ultrasonic sensors on the left and right sides.

## PCB Addition

To save space on the rover, I converted the breadboard circuit that connects the Ultrasonic sensors and the motors to a PCB design that I developed in Autodesk Eagle. Updated images are found below. I learned how to build the board through a free Udemy Course that covers the basics, and I was able to print, solder, and implement the board within 2 weeks. This will allow me to use the breadboard to prototype other circuits for different sensors.

<div align="center">Updated Design with PCB Board</div>

![Caption](https://user-images.githubusercontent.com/55263663/113646131-0b331280-963d-11eb-8094-8f6ab8cfa5e2.jpg)
![IMG_0808](https://user-images.githubusercontent.com/55263663/109580868-2fd12300-7ab0-11eb-835c-0d006bbe778e.jpg)

# Mobilizing the Rover

At the current build, there are 3 ways to mobilize the rover. One of them uses a PS4 controller, the bluetooth functionality of the Raspberry Pi, pyPS4 library, and the libraries that control the Roboclaw Motor Controller. The second method uses the Ultrasonic sensors to help the rover avoid obstructions in its path without physical human interaction. The third method uses an HTML-based webserver based on Python libraries to control the rover's movements.

## Remote Control Rover via PS4 Controller

This method requires specific libraries with Python to work properly. One of them is the Roboclaw libraries that will be used for the remainder of the project, as this motor controller will be used to control all six motors. The full library with sample code is provided by Basic Micro here: https://www.basicmicro.com/downloads. 

This link will aid in setting up the controller with the Raspberry Pi --> https://resources.basicmicro.com/packet-serial-with-the-raspberry-pi-3/

**Note:** The sample code imports "roboclaw" at the top. This will only work for Python 2. The file marked as "roboclaw_3" must be imported instead for Python 3.

The other library to be used is from this Github page --> https://github.com/ArturSpirin/pyPS4Controller

Using a combination of the sample code from Basic Micro and the pyPS4 functions, I was able to control the movement of the rover with a PS4 controller. Basic movements include Forward, Backward, Left Rotate, and Right Rotate.

The code for this part of the project is listed as "test.py" --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/test.py

## Remote Control via Webservers

### HTML Based Server

This server is constructed with Python's built-in https server library and allows users to create an HTML-based server with Python. I found a website that had used the library to control the GPIO pins of a Raspberry Pi and be able to turn off an on an LED through a local webserver. Using the template, I programmed additional HTML code to add features to the server that would allow me to control the rover's movements by clicking hyperlinks. The webserver also keeps track of the CPU temperature of the Pi and can also initiate the obstacle avoidance program with a click of a button.

![HTML-Based Server Screenshot](https://user-images.githubusercontent.com/55263663/112916259-0efeec00-90b5-11eb-9e63-109e29d04f2a.png)

The built-in library is a great way to get started with creating webservers. I had only used HTML to customize the server design, but we could also use CSS and Javascript to further improve the web server's UI.

Here is the source code I used to build this webserver: --> https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/

### Node-RED Server

Node-RED is a flow-based programming tool that allows users to control hardware devices such as Raspberry Pi and Arduino within their local network. It also allows the user to create their own UI to set up their network and monitor it from their laptop or mobile web browser.

#### Set-Up

I used the following link to set up Node-RED on my Raspberry Pi using Terminal commands. I highly recommend using the autostart feature so that the program starts on its own when the Pi is booted.

Node-RED Raspberry Pi Link --> https://nodered.org/docs/getting-started/raspberrypi

If you have Raspian installed with recommended software, Node-RED should already be preinstalled on your device. The only thing to do is enable the autostart. The link below is the Raspian OS with Recommended Software image.

Raspian OS --> https://www.raspberrypi.org/software/operating-systems/

#### My Node-RED User Interface

I used Node-RED to control the Raspberry Pi on the UI Rover. I have set up different webpages on the server to monitor and control different aspects of the prototype rover.

On the homepage, I am able to shut down or reboot the Pi when I need to, as well as update the Pi and execute the HTML server program to start the web server remotely.

![Node-RED Homepage](https://user-images.githubusercontent.com/55263663/114245029-74b86700-9944-11eb-9a33-cc7af4412ed1.png)

Another page is designated to monitoring the Pi's CPU temperature and the available memory. If my Pi suddenly slows down, I can check if the Pi is overheating or if the RAM is full.

![CPU Temperature and Memory Monitoring](https://user-images.githubusercontent.com/55263663/114245043-7d10a200-9944-11eb-8ca0-698f7407b925.png)

The rover itself can be controlled by setting up switches that direct the rover forward, backward, left, right, and stop. The last page I had set up is able to start the Obstacle Avoidance program remotely by clicking a switch. Both of these pages allow me to test the rover without needing to connect a monitor or use VNC server. I have the Raspberry Pi set up to autostart Node-RED on boot so it is ready to use right away.

![Rover Control](https://user-images.githubusercontent.com/55263663/114245054-826dec80-9944-11eb-9798-3d0d927b39ec.png)

![Obstacle Avoidance Start](https://user-images.githubusercontent.com/55263663/114245057-869a0a00-9944-11eb-8112-adffffc06441.png)

In future iterations, I will continue to add to the webserver with more functions and statistics that will be useful when the rover is fully autonomous.

# Autonomous Rover 

The following section discusses the programs and techniques that I have used to get the rover to move autonomously without human interaction. The main program so far is based on using sensors to help the rover avoid obstructions in its path. 

## Obstacle Avoidance Rover 

The next step for this project was to get some autonomous travel going. For the current build, I have three Ultrasonic Range sensors on the front of the rover to aid in detecting obstructions in the rover's path. 

### How the Sensors work (HD-SC04)

In the most basic terms, the sensor has 2 "eyes". One of the eyes sends a sonic pulse towards an object. The pulse will bounce back into the other eye of the sensor. The time it takes for that pulse to be transmitted and received is calculated into a distance based on the speed of sound in air, which is collected by the Raspberry Pi.

### How the Code works

The code I have written is listed as "Obstacle_Avoidance.py" in the Github --> https://github.com/karmsingh691/Ultra-Instinct-Rover-Project/blob/main/Obstacle_Avoidance.py

The algorithm works as follows: 

The front sensors' responsibility is to detect objects that may be less than 30 cm from the rover. If there is an object, the left and right sensors will also report back if they see objects less than 15 cm from the rover. If one side has a clearance of more than 15cm, the rover is instructed to rotate in the direction of the least amount of obstructions. This is looped forever so that the rover can continue avoiding obstacles that it can detect.

## Future Plans

I am currently working on using OpenCV functions for lane tracking algorithms and incorporating different components in different versions of this rover. I will update this rover with a revamp in summer 2024. See you then!

**Disclaimer:** This project was completed over two months during the summer of 2023.

