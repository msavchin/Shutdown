# Shutdown App

This script uses the tkinter library to create a simple graphical user interface (GUI) for a "Shutdown App" that allows the user to schedule a system shutdown at a specified time. 

## Requirements
- Python 3
- Tkinter library

## How to use
- Run the script on your computer
- A window will appear with two options: submit and cancel
- In the text field, enter the time in minutes until you want the system to shut down
- Press submit to schedule the shutdown
- Press cancel to cancel the scheduled shutdown

## Functionality
- The script uses the os library to execute command line commands to initiate and cancel the shutdown
- The platform library is used to determine the type of operating system the script is running on (Windows, Linux, or macOS)
- The script checks the type of operating system and uses the appropriate command to initiate or cancel the shutdown
- The script also uses tkinter's messagebox library to display error messages if the user enters an invalid time or if an unsupported platform is detected.

## Note 
- This script will only work on Windows, Linux and Mac OS.
- The user should have administrative rights to run the script.
- The user can cancel the shutdown by clicking the "Cancel" button on the GUI or by manually canceling the scheduled shutdown via their operating system's settings.
