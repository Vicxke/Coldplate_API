import serial
import serial.tools.list_ports
import threading

__all__ = ['ColdPlateCommands']  # Exporteer expliciet de klasse ColdPlateCommands

class ColdPlateCommands:
    def __init__(self):
        self.serial_connection = None
        self.lock = threading.Lock()  # Add a threading lock

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
        with self.lock:  # Ensure thread-safe access
            if self.serial_connection:
                self.serial_connection.close()
            self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1)
            print("Connected to ColdPlate.")
        
    def send_command(self, command):
        with self.lock:  # Ensure thread-safe access
            if not self.serial_connection or not self.serial_connection.is_open:
                raise ConnectionError("No USB port selected or connection is closed.")

            # Ensure the command ends with a carriage return
            command += '\r'
            
            # Send the command
            self.serial_connection.write(command.encode('ascii'))

            # Read the version number (first response line)
            response = self.serial_connection.read_until(b'\r\n').decode('ascii').strip()
            print(f"DEBUG: Received version response: {response}")

            # Check if the response indicates an error ('e')
            #error_response = self.serial_connection.read_until(b'\r\n').decode('ascii').strip()
            #print(f"DEBUG: Received error response: {error_response}")

            if response == 'e':
                raise Exception(f"Error from device: {response}")

            return response  # Return the version number

    def close_connection(self):
        """
        Close the USB connection.
        """
        with self.lock:  # Ensure thread-safe access
            if self.serial_connection:
                self.serial_connection.close()
                self.serial_connection = None
