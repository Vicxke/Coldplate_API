from ColdPlate_commands import ColdPlateCommands  # Gebruik expliciete import

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
        return self.commands.send_command("getVersion")

    def get_description(self):
        """
        Get the model information of the device.
        """
        return self.commands.send_command("getDescription")

    def get_version_and_description(self):
        """
        Get the model information and version number.
        """
        return self.commands.send_command("version")

    def get_info(self):
        """
        Get the boot screen text.
        """
        return self.commands.send_command("info")

    def reset_device(self):
        """
        Restart the controller.
        """
        return self.commands.send_command("resetDevice")

    def get_error_list(self):
        """
        Get a list of errors and warnings.
        """
        return self.commands.send_command("getErrorList")

    def enable_cled(self):
        """
        Enable the LED indication lights.
        """
        return self.commands.send_command("enableCLED")

    def disable_cled(self):
        """
        Disable the LED indication lights.
        """
        return self.commands.send_command("disableCLED")

    def get_cled_status(self):
        """
        Get the status of the LED indication lights.
        """
        return self.commands.send_command("getCLED")

    def flash_led(self):
        """
        Flash the device LED five times.
        """
        return self.commands.send_command("flashLed")

    def set_buzzer(self, duration):
        """
        Set the buzzer to beep for a given duration in milliseconds.
        """
        if not (50 <= duration <= 999):
            raise ValueError("Duration must be between 50 and 999 milliseconds.")
        return self.commands.send_command(f"setBuzzer{duration}")

    def enable_boot_screen(self):
        """
        Enable the boot screen startup text.
        """
        return self.commands.send_command("enableBootScreen")

    def disable_boot_screen(self):
        """
        Disable the boot screen startup text.
        """
        return self.commands.send_command("disableBootScreen")

    def get_boot_screen_state(self):
        """
        Get the state of the boot screen.
        """
        return self.commands.send_command("getBootScreenState")

    def set_led_brightness(self, brightness):
        """
        Set the LED brightness (0-127).
        """
        if not (0 <= brightness <= 127):
            raise ValueError("Brightness must be between 0 and 127.")
        return self.commands.send_command(f"setLedBrightness{brightness}")

    def enable_led_pulse_mode(self):
        """
        Enable the LED pulse mode.
        """
        return self.commands.send_command("setLedPulseModeEnable")

    def disable_led_pulse_mode(self):
        """
        Disable the LED pulse mode.
        """
        return self.commands.send_command("setLedPulseModeDisable")

    def temp_on(self):
        """
        Turn on the temperature control.
        """
        return self.commands.send_command("tempOn")

    def temp_off(self):
        """
        Turn off the temperature control.
        """
        return self.commands.send_command("tempOff")

    def get_temp_state(self):
        """
        Get the state of the temperature control.
        """
        return self.commands.send_command("getTempState")

    def get_temp_state_as_string(self):
        """
        Get the state of the temperature control as a string.
        """
        return self.commands.send_command("getTempStateAsString")

    def get_temp_target(self):
        """
        Get the target temperature.
        """
        return self.commands.send_command("getTempTarget")

    def set_temp_target(self, target_temp):
        """
        Set the target temperature in 1/10 °C (-10 to 99.9°C).
        """
        if not (-100 <= target_temp <= 999):
            raise ValueError("Target temperature must be between -10.0 and 99.9°C.")
        return self.commands.send_command(f"setTempTarget{target_temp}")

    def get_temp_actual(self):
        """
        Get the current temperature.
        """
        return self.commands.send_command("getTempActual")

    def get_temp_min(self):
        """
        Get the minimum possible temperature set point.
        """
        return self.commands.send_command("getTempMin")

    def get_temp_max(self):
        """
        Get the maximum possible temperature set point.
        """
        return self.commands.send_command("getTempMax")

    def get_temp_limiter_min(self):
        """
        Get the minimum temperature limiter.
        """
        return self.commands.send_command("getTempLimiterMin")

    def set_temp_limiter_min(self, min_temp):
        """
        Set the minimum temperature limiter.
        """
        return self.commands.send_command(f"setTempLimiterMin{min_temp}")

    def get_temp_limiter_max(self):
        """
        Get the maximum temperature limiter.
        """
        return self.commands.send_command("getTempLimiterMax")

    def set_temp_limiter_max(self, max_temp):
        """
        Set the maximum temperature limiter.
        """
        return self.commands.send_command(f"setTempLimiterMax{max_temp}")

    def enable_temp_logging(self):
        """
        Enable automatic temperature logging.
        """
        return self.commands.send_command("setTempLoggingOn")

    def disable_temp_logging(self):
        """
        Disable automatic temperature logging.
        """
        return self.commands.send_command("setTempLoggingOff")

    def close_connection(self):
        """
        Close the USB connection.
        """
        self.commands.close_connection()
