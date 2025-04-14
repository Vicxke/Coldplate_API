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