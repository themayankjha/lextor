## Lextor Web
---
#### Overview
This application allows a remote web-based control interface for a Raspberry Pi robot.
The web-based interface has a working backend in PHP while the Raspberry Pi run on Python.
I created this in 2018 have recently found the source code so sharing it here.Some of the things I have done may not be the best from security standpoint but ultimately I achieved the functionality I wanted to achieve.

This is also deployed on [Azure](https://lextor.azurewebsites.net/)

Also I have regenerated the ftp keys so dont go spooing around xD.
---
#### Functionality
- This application uses a web based interface with various control buttons which when clicked activate a script to change contents of text file hosted on the same server.
- The raspberry pi queries the server every second and looks for the contents of the text file to know what command is being run.
- The ultrasonic sensor senses distance updates in a local text file and using FTP uplaods the content to the server.
- I used localtunnel to directly stream the webcam attached to the website.

---
#### Usage
 This acts as a basic wireframe to get started with controling a Raspberry Pi remotely.You can extend this code to allow Database and more secure implementations of various things. 

---


#### Copyright
Copyright (c) 2021 [Mayank Jha](https://github.com/themayankjha)


License - [MIT](License.md)

---