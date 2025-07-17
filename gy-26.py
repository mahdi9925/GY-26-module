import smbus
import serial
import time


bus = smbus.SMBus(1)


def switch_UART_I2C(UART_addr, baudrat):
    try:
        ser = serial.Serial(UART_addr, baudrate=baudrat, timeout=1)
        time.sleep(2)

        ser.write(b"$WI2C,1*3F\r\n")
        ser.close()

        msg = "I2C mode is successfully switched."
        return msg

    except Exception as err:
        msg = f"Failed to switched: {err}"
        return msg


def read_angle(
    i2c_addr,
    register,
    get_angle,
    high_angle,
    low_angle,
):
    try:
        bus.write_byte_data(i2c_addr, register, get_angle)

        high = bus.read_byte_data(i2c_addr, high_angle)
        low = bus.read_byte_data(i2c_addr, low_angle)
        heading = ((high << 8) + low) / 10

        return heading
    except Exception as err:
        msg = f"Failed to read data: {err}"
        return msg


def start_calibration(i2c_addr, register, start_calib):
    try:
        bus.write_byte_data(i2c_addr, register, start_calib)
        msg = "Calibration started."
        return msg
    except Exception as err:
        msg = f"Failed to started calibration, {err}"
        return msg


def end_calibration(i2c_addr, register, end_calib):
    try:
        bus.write_byte_data(i2c_addr, register, end_calib)
        msg = "Calibration is completed."
        return msg
    except Exception as err:
        msg = f"Failed to end calibration, {err}"
        return msg
