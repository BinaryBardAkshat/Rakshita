import obd

connection = obd.OBD()

def fetch_ecu_info():
    # Fetch and print RPM
    rpm_response = connection.query(obd.commands.RPM)
    print("Engine RPM:", rpm_response.value)

    # Fetch and print vehicle speed
    speed_response = connection.query(obd.commands.SPEED)
    print("Vehicle Speed:", speed_response.value.to("mph"))

    # Fetch and print coolant temperature
    coolant_response = connection.query(obd.commands.COOLANT_TEMP)
    print("Coolant Temperature:", coolant_response.value.to("celsius"))

    # Fetch and print throttle position
    throttle_response = connection.query(obd.commands.THROTTLE_POS)
    print("Throttle Position:", throttle_response.value)

    # Fetch and print engine load
    load_response = connection.query(obd.commands.ENGINE_LOAD)
    print("Engine Load:", load_response.value)

# Main function
def main():
    try:
        fetch_ecu_info()
    except Exception as e:
        print("Error occurred:", e)
    finally:
        # Close connection to the car's OBD-II system
        connection.close()

if __name__ == "__main__":
    main()
