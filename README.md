# RainbowHAT Controller Project
This project aims to control a RainbowHAT from a Raspberry Pi, specifically a Pico Pi Rev B1 i.MX7 Dual, and display information like cryptocurrency prices and time.

## Motivation:
While the original goal was to use an abandoned AndroidThings device for this project and aimed to control a RainbowHAT using a Pico Pi Rev B1 i.MX7 Dual running Yocto Linux. However, I encountered limitations due to library incompatibility with the i.MX7 processor. Setting up the necessary libraries for GPIO control on the i.MX7 proved to be overly complex for a hobbyist project. Therefore, I opted for a more feasible approach using a Raspberry Pi.
## Capabilities:
- **Data Display:**
  - Fetches current cryptocurrency prices from an API.
  - Displays date, time, and crypto prices on the RainbowHAT's 4x 14-segment display.
- **Scheduling:**
  - Implements two schedulers:
    - A recurring task scheduler for repetitive actions.
    - A queue-based task scheduler for running tasks in a specific order.
- **Auto-Deployment: (using Fabric library)**
  - Reads SSH credentials and project configuration from a secure YAML file (private.yml).
  - Connects to a remote server.
  - Transfers project files to the server.
  - Prepares and runs the main script on the server.

## Future Enhancements:
- **Hydration Tracker:**
  - Display hydration progress and goal on the 7 RGB LEDs.
- **Remote Control:**
  - Implement TCP communication to allow for remote control of the project during runtime.

## Getting Started:

- Install required libraries [requirements.txt](requirements.txt)
- Configure your API keys and other settings in private.yml (keep this file secure!).
- Run the project using `python3 RPiRainbowHatController.py`.

## Sample output
![GIF](rpi-rainbowhat-sample.gif)