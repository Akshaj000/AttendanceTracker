
# Attendance Tracker
Attendance Tracker is a web-based application designed to track attendance in a classroom setting. It consists of three apps: tracker, logger, and client. This project leverages the Django framework and provides REST endpoints for seamless communication between the different components.
  
### Apps
#### 1) Tracker
The tracker app is responsible for managing the core functionality of the attendance tracking system. It provides the following models:
  
- User: Represents a user of the system, typically staff or students.
- Log: Stores the log information of devices connected to the classroom Wi-Fi network. Logs are created through an API by the logger app.
- Sessions: Defines a range of time from start time to end time during which attendance records can be created.
- Records: Stores attendance records for students. A record is only created if the log of the student exists within the session timestamps.
  
Additionally, the tracker app exposes REST endpoints to interact with the system, allowing users to register, login, create sessions, and manage attendance records.
  
#### 2) Logger
The logger app serves as an interface between the attendance tracker system and the Wi-Fi network. It scans the Wi-Fi network for MAC addresses and calls the tracker API to create logs based on the discovered devices. The logger app helps automate the attendance tracking process by integrating with the classroom's Wi-Fi infrastructure.
  
#### 3) Client
The client app is a web application that provides an interface for staff and students to interact with the attendance tracker system. Users can log in using their credentials and perform the following actions:
  
- Staff:
  Create sessions for recording attendance.
  Manage attendance records.
- Students:
  Record attendance by marking their presence for specific sessions.
    
The client app utilizes the REST endpoints provided by the tracker app to communicate with the backend and perform the required actions.
