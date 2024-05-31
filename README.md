# Project to control RainbowHAT

I just wanted to control RainbowHAT from abandoned AndroidThings with Pico Pi Rev B1 i.MX7 Dual
but i was unable to get it working with Yocto Linux, bcs libraries supports only Raspberry Pi
And there was so much stuff going on to get it working on i.MX7d to control it over GPIO pins as a hobby project.

### Capabilities
- **Main Features** 
  - Fetch current crypto prices from API
  - Can display date, time and current crypto prices
    - data are displayed on the 4x 14segment display
  - Implements 2 schedulers
    - One for scheduling recurring tasks over time
    - One for running tasks in a queue
- **Auto-deloy**
  - Reads private data from YAML file (private.yml)
    - Extracts SSH key password, hostname, username 
  - Connects to the remote server using Fabric library
  - Transfers project files
  - Prepares and runs the main script on the remote server
- Ideas for extensions
  - Hydration tracker
    - Display it with goal on the 7 RGB leds
  - Implement TCP communication
    - Allow remote control in runtime

