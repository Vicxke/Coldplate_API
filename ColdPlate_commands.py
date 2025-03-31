import serial
import serial.tools.list_ports

__all__ = ['ColdPlateCommands']  # Exporteer expliciet de klasse ColdPlateCommands

class ColdPlateCommands:
    def __init__(self):
        self.serial_connection = None

    def list_ports(self):
        """
        List all available USB ports on the system.
        """
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def select_port(self, port_name):
        """
        Select a USB port for communication.
        """
        if self.serial_connection:
            self.serial_connection.close()
        self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1)

    def send_command(self, command):
        """
        Send a command to the connected device.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("No USB port selected or connection is closed.")
        self.serial_connection.write(f"{command}\n".encode())
        return self.serial_connection.readline().decode().strip()

    def close_connection(self):
        """
        Close the USB connection.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None
