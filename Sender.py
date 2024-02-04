import obd
import requests
import pytesseract
import cv2
import base64

# Initialize connection to the car's OBD-II system
connection = obd.OBD()

# Function to fetch information from the car's ECU
def fetch_ecu_info():
    ecu_info = {}

    # Fetch RPM
    rpm_response = connection.query(obd.commands.RPM)
    ecu_info["RPM"] = rpm_response.value.magnitude

    # Fetch vehicle speed
    speed_response = connection.query(obd.commands.SPEED)
    ecu_info["Vehicle Speed (mph)"] = speed_response.value.to("mph").magnitude

    # Fetch coolant temperature
    coolant_response = connection.query(obd.commands.COOLANT_TEMP)
    ecu_info["Coolant Temperature (Celsius)"] = coolant_response.value.magnitude

    # Fetch throttle position
    throttle_response = connection.query(obd.commands.THROTTLE_POS)
    ecu_info["Throttle Position (%)"] = throttle_response.value.magnitude

    # Fetch engine load
    load_response = connection.query(obd.commands.ENGINE_LOAD)
    ecu_info["Engine Load (%)"] = load_response.value.magnitude

    return ecu_info


def recognize_license_plate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh, lang='eng', config='--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return text

def measure_distance():
    
    return 10 

# Function to send all data to web server
def send_all_data_to_server(ecu_info, license_plate, distance):
    server_url = "http://localhost:5050"
    data = {"ECU_Info": ecu_info, "License_Plate": license_plate, "Distance": distance}
    try:
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the server.")
        else:
            print("Failed to send data to the server. Status code:", response.status_code)
    except Exception as e:
        print("Error occurred while sending data to the server:", e)

# Main function
def main():
    try:
        # Fetch ECU information
        ecu_info = fetch_ecu_info()
        print("ECU Information:", ecu_info)

        # Dummy image capture (replace with actual camera capture logic)
        frame = cv2.imread("license_plate_image.jpg")

        # Perform license plate recognition
        license_plate = recognize_license_plate(frame)
        print("License Plate:", license_plate)

        # Measure distance (replace with actual distance measurement logic)
        distance = measure_distance()
        print("Distance Measurement:", distance)

        # Send all data to the server
        send_all_data_to_server(ecu_info, license_plate, distance)
    except Exception as e:
        print("Error occurred:", e)
    finally:
        # Close connection to the car's OBD-II system
        connection.close()

if __name__ == "__main__":
    main()
