from ColdPlate_commands import ColdPlateCommands

class ColdPlateAPI:
    def __init__(self):
        self.commands = ColdPlateCommands()

    def list_ports(self):
        """
        List all available USB ports on the system.
        """
        return self.commands.list_ports()

    def select_port(self, port_name):
        """
        Select a USB port for communication.
        """
        self.commands.select_port(port_name)

    def get_version(self):
        """
        Get the version of the connected device.
        """
        return self.commands.send_command("GetVersion")

    def temp_on(self):
        """
        Turn on the temperature control.
        """
        return self.commands.send_command("tempOn")

    def set_temp_target(self, target_temp):
        """
        Set the target temperature.
        """
        return self.commands.send_command(f"setTempTarg {target_temp}")

    def close_connection(self):
        """
        Close the USB connection.
        """
        self.commands.close_connection()

# Example usage:
# api = ColdPlateAPI()
# print(api.list_ports())
# api.select_port("COM3")
# print(api.get_version())
# api.temp_on()
# api.set_temp_target(25)
# api.close_connection()
