import serial
import time
import threading

__all__ = ['SyringeCommands']  # Exporteer expliciet de klasse ColdPlateCommands

class SyringeCommands:
    def __init__(self, baudrate=115200, timeout=1):
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        self.port = None  # Poort wordt later ingesteld
        self.lock = threading.Lock()  # Zorgt ervoor dat commando’s niet tegelijk verstuurd worden

    def connect(self, port=None):
        try:
            self.port = port 
            self.connection = serial.Serial(port, baudrate=self.baudrate, timeout=self.timeout)
            # Verify the connection
            if not self.verify_connection():
                self.disconnect()
                raise ConnectionError("Verbinding mislukt: apparaat niet herkend.")
            print(f"✅ Verbonden met {port}")
        except Exception as e:
            raise ConnectionError(f"Fout bij verbinden met de poort {port}: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print(f"Verbinding met de poort verbroken.")
        else:
            raise ConnectionError("Geen actieve verbinding om te verbreken.")

    def send_command(self, cmd):
        with self.lock:
            if self.connection and self.connection.is_open:
                try:
                    self.connection.write((cmd + '\r').encode())
                    time.sleep(0.2)
                    response = self.connection.read_all().decode('utf-8', errors='ignore')
                    if not response:
                        raise IOError(f"Fout bij het versturen naar de usb poort {self.port}.")
                    return response
                except Exception as e:
                    raise IOError(f"Fout bij versturen van commando: {e}")
            else:
                raise ConnectionError("Geen actieve verbinding om commando te versturen.")

    def verify_connection(self):
        """
        Verify the connection by sending the ECHO command.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("Geen actieve verbinding om te verifiëren.")
        
        try:
            response = self.send_command("echo on")  # Send the ECHO command
            print(f"DEBUG: ECHO response: {response}")  # Debug print to check the response
            # Check if the response contains the expected confirmation
            if "echo on" in response or "echo is ON" in response:
                return True
            else:
                return False
        except Exception as e:
            raise IOError(f"Fout bij het verifiëren van de verbinding: {e}")