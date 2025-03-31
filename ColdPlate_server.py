from flask import Flask, request, jsonify
from ColdPlate_api import ColdPlateAPI

app = Flask(__name__)
api = ColdPlateAPI()

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
    port_name = data.get('port_name')
    if not port_name:
        return jsonify({"error": "port_name is required"}), 400
    try:
        api.select_port(port_name)
        return jsonify({"message": f"Port {port_name} selected successfully"})
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
        response = api.set_temp_target(target_temp)
        return jsonify({"response": response})
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
