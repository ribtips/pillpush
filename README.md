# pillpush
Basically a log of when a button is pressed on an Arduino...(I'm using it to track medication ingestion times)

Description: This project senses a button press input from an esp8266 nodemcu and then connects to a python3 server running on a linux box and logs the time that the button was pressed.  When it determines that a button was pressed, it will kick off a script to read the log, generate a json data file with the current week and previous weeks button presses. It then uploads that data file to a remote server where a javascript file will use it as input to create a status of when the button was pressed in prescribed windows.

Files: 
1. server_light_flash_test.ino - this is the arduino IDE sketch that is used to flash a light during a prescribed time period and to monitor when a button is pressed.  The time is then sent to a server when the button is pressed which turns the light off.
2. status.txt - the log of the times that the server writes to.
3. tell_server_v3.py - the python server that listens for when the nodemcu connects to it, logs it into the status file, calls the python code to generate the json, and then sends the updated json file to the webserver.
4. start_of_week2.py - the python script that is called by the tell_server script to generate the json file with statuses of button presses and such.
5. pillpush.html - the javascript page that reads in the data.json file and displays the data on a webpage.
