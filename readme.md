The ColdPlate API was developed using the `pyserial` library to facilitate communication with the device over USB and the `Flask` framework to create a lightweight and efficient web API. The combination of these technologies ensures reliable data exchange between the API and the hardware while providing an easy-to-use interface for developers.

# API Endpoints for ColdPlate API

## Connection Management
- **GET /list_ports**: Lists all available USB ports.
- **POST /select_port**: Selects a USB port for communication.
- **POST /close_connection**: Closes the USB connection.
- **GET /is_connected**: see if there is a connection.

## Device Information
- **GET /get_version**: Retrieves the device version.
- **GET /get_description**: Retrieves the device description.
- **GET /get_version_and_description**: Retrieves both version and description.
- **GET /get_info**: Retrieves boot screen information.
- **GET /get_error_list**: Retrieves a list of errors and warnings.

## Temperature Control
- **POST /temp_on**: Turns on the temperature control.
- **POST /temp_off**: Turns off the temperature control.
- **POST /set_temp_target**: Sets the target temperature.
- **GET /get_temp_state**: Retrieves the state of the temperature control.
- **GET /get_temp_state_as_string**: Retrieves the state of the temperature control as text.
- **GET /get_temp_target**: Retrieves the target temperature.
- **GET /get_temp_actual**: Retrieves the current temperature.
- **GET /get_temp_min**: Retrieves the minimum temperature setting.
- **GET /get_temp_max**: Retrieves the maximum temperature setting.
- **GET /get_temp_limiter_min**: Retrieves the minimum temperature limiter.
- **POST /set_temp_limiter_min**: Sets the minimum temperature limiter.
- **GET /get_temp_limiter_max**: Retrieves the maximum temperature limiter.
- **POST /set_temp_limiter_max**: Sets the maximum temperature limiter.
- **POST /enable_temp_logging**: Enables automatic temperature logging.
- **POST /disable_temp_logging**: Disables automatic temperature logging.

## LED & Indicator Control
- **POST /enable_cled**: Enables the LED indicator lights.
- **POST /disable_cled**: Disables the LED indicator lights.
- **GET /get_cled_status**: Retrieves the current status of the LED indicators.
- **POST /flash_led**: Flashes the LED.
- **POST /set_led_brightness**: Sets the LED brightness.
- **POST /enable_led_pulse_mode**: Enables the LED pulse mode.
- **POST /disable_led_pulse_mode**: Disables the LED pulse mode.

## Boot Screen & Device Reset
- **POST /reset_device**: Resets the device.
- **POST /enable_boot_screen**: Enables the boot screen display.
- **POST /disable_boot_screen**: Disables the boot screen display.
- **GET /get_boot_screen_state**: Retrieves the boot screen state.

## Buzzer Control
- **POST /set_buzzer**: Activates the buzzer for a specific duration.
