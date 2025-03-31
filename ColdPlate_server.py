from flask import Flask, request, jsonify
from ColdPlate_api import ColdPlateAPI  # Gebruik expliciete import

app = Flask(__name__)
api = ColdPlateAPI()

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST"
    return response

@app.route('/list_ports', methods=['GET'])
def list_ports():
    """
    Endpoint to list all available USB ports.
    """
    ports = api.list_ports()
    return jsonify(ports)

@app.route('/select_port', methods=['POST'])
def select_port():
    """
    Endpoint to select a USB port.
    """
    data = request.json
    port = data.get('port')
    if not port:
        return jsonify({"error": "port_name is required"}), 400
    try:
        api.select_port(port)
        return jsonify({"message": f"Port {port} selected successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_version', methods=['GET'])
def get_version():
    """
    Endpoint to get the version of the connected device.
    """
    try:
        version = api.get_version()
        return jsonify({"version": version})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/temp_on', methods=['POST'])
def temp_on():
    """
    Endpoint to turn on the temperature control.
    """
    try:
        response = api.temp_on()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_temp_target', methods=['POST'])
def set_temp_target():
    """
    Endpoint to set the target temperature.
    """
    data = request.json
    target_temp = data.get('target_temp')
    if target_temp is None:
        return jsonify({"error": "target_temp is required"}), 400
    try:
        target_temp = int(target_temp*10)  # Converteer naar integer
        response = api.set_temp_target(target_temp)
        return jsonify({"response": response})
    except ValueError:
        return jsonify({"error": "target_temp must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/close_connection', methods=['POST'])
def close_connection():
    """
    Endpoint to close the USB connection.
    """
    try:
        api.close_connection()
        return jsonify({"message": "Connection closed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_description', methods=['GET'])
def get_description():
    try:
        description = api.get_description()
        return jsonify({"description": description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_version_and_description', methods=['GET'])
def get_version_and_description():
    try:
        info = api.get_version_and_description()
        return jsonify({"info": info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_info', methods=['GET'])
def get_info():
    try:
        info = api.get_info()
        return jsonify({"info": info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reset_device', methods=['POST'])
def reset_device():
    try:
        response = api.reset_device()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_error_list', methods=['GET'])
def get_error_list():
    try:
        errors = api.get_error_list()
        return jsonify({"errors": errors})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enable_cled', methods=['POST'])
def enable_cled():
    try:
        response = api.enable_cled()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disable_cled', methods=['POST'])
def disable_cled():
    try:
        response = api.disable_cled()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_cled_status', methods=['GET'])
def get_cled_status():
    try:
        status = api.get_cled_status()
        return jsonify({"status": status})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flash_led', methods=['POST'])
def flash_led():
    try:
        response = api.flash_led()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_buzzer', methods=['POST'])
def set_buzzer():
    """
    Endpoint to set the buzzer duration.
    """
    data = request.json
    duration = data.get('duration')
    if duration is None:
        return jsonify({"error": "duration is required"}), 400
    try:
        duration = int(duration)  # Converteer naar integer
        response = api.set_buzzer(duration)
        return jsonify({"response": response})
    except ValueError:
        return jsonify({"error": "duration must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enable_boot_screen', methods=['POST'])
def enable_boot_screen():
    try:
        response = api.enable_boot_screen()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disable_boot_screen', methods=['POST'])
def disable_boot_screen():
    try:
        response = api.disable_boot_screen()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_boot_screen_state', methods=['GET'])
def get_boot_screen_state():
    try:
        state = api.get_boot_screen_state()
        return jsonify({"state": state})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_led_brightness', methods=['POST'])
def set_led_brightness():
    """
    Endpoint to set the LED brightness.
    """
    data = request.json
    brightness = data.get('brightness')
    if brightness is None:
        return jsonify({"error": "brightness is required"}), 400
    try:
        brightness = int(brightness)  # Converteer naar integer
        response = api.set_led_brightness(brightness)
        return jsonify({"response": response})
    except ValueError:
        return jsonify({"error": "brightness must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enable_led_pulse_mode', methods=['POST'])
def enable_led_pulse_mode():
    try:
        response = api.enable_led_pulse_mode()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disable_led_pulse_mode', methods=['POST'])
def disable_led_pulse_mode():
    try:
        response = api.disable_led_pulse_mode()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/temp_off', methods=['POST'])
def temp_off():
    try:
        response = api.temp_off()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_state', methods=['GET'])
def get_temp_state():
    try:
        state = api.get_temp_state()
        return jsonify({"state": state})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_state_as_string', methods=['GET'])
def get_temp_state_as_string():
    try:
        state = api.get_temp_state_as_string()
        return jsonify({"state": state})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_target', methods=['GET'])
def get_temp_target():
    try:
        target = api.get_temp_target()
        return jsonify({"target": target})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_actual', methods=['GET'])
def get_temp_actual():
    try:
        actual = api.get_temp_actual()
        return jsonify({"actual": actual})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_min', methods=['GET'])
def get_temp_min():
    try:
        temp_min = api.get_temp_min()
        return jsonify({"temp_min": temp_min})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_max', methods=['GET'])
def get_temp_max():
    try:
        temp_max = api.get_temp_max()
        return jsonify({"temp_max": temp_max})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_limiter_min', methods=['GET'])
def get_temp_limiter_min():
    try:
        limiter_min = api.get_temp_limiter_min()
        return jsonify({"limiter_min": limiter_min})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_temp_limiter_min', methods=['POST'])
def set_temp_limiter_min():
    """
    Endpoint to set the minimum temperature limiter.
    """
    data = request.json
    min_temp = data.get('min_temp')
    if min_temp is None:
        return jsonify({"error": "min_temp is required"}), 400
    try:
        min_temp = int(min_temp)  # Converteer naar integer
        response = api.set_temp_limiter_min(min_temp)
        return jsonify({"response": response})
    except ValueError:
        return jsonify({"error": "min_temp must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_temp_limiter_max', methods=['GET'])
def get_temp_limiter_max():
    try:
        limiter_max = api.get_temp_limiter_max()
        return jsonify({"limiter_max": limiter_max})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_temp_limiter_max', methods=['POST'])
def set_temp_limiter_max():
    """
    Endpoint to set the maximum temperature limiter.
    """
    data = request.json
    max_temp = data.get('max_temp')
    if max_temp is None:
        return jsonify({"error": "max_temp is required"}), 400
    try:
        max_temp = int(max_temp)  # Converteer naar integer
        response = api.set_temp_limiter_max(max_temp)
        return jsonify({"response": response})
    except ValueError:
        return jsonify({"error": "max_temp must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enable_temp_logging', methods=['POST'])
def enable_temp_logging():
    try:
        response = api.enable_temp_logging()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disable_temp_logging', methods=['POST'])
def disable_temp_logging():
    try:
        response = api.disable_temp_logging()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
