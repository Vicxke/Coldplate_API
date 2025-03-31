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
        self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1)
        print("Connected to ColdPlate.")

    def send_command(self, command):
        """
        Send a command to the connected device.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("No USB port selected or connection is closed.")
        command += '\r'  # Append carriage return as per manual
        self.serial_connection.write(command.encode('ascii'))
        #time.sleep(0.1)  # Wait for response
        response = self.serial_connection.read_until(b'\r\n').decode('ascii').strip()
        return response

    def close_connection(self):
        """
        Close the USB connection.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None
