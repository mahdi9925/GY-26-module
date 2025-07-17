# GY-26 Compass Module Python Library

This is a simple Python library to interface with the **GY-26 digital compass module** using both **UART** and **I2C** protocols on a Raspberry Pi.

It allows you to:

- Switch the module from UART to I2C
- Read heading angle (in degrees)
- Perform calibration
- Apply magnetic declination correction

---

## 📦 Requirements

- Raspberry Pi (any model with I2C and UART)
- GY-26 Compass Module
- Python 3.7+
- Installed Python packages:
  
  sudo apt install python3-smbus i2c-tools
  pip3 install serial
