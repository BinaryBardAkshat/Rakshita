import pytesseract
import cv2
import requests

def recognize_license_plate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh, lang='eng', config='--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return text

def send_data_to_server(original, predicted):
    url = "http://localhost:5050"
    data = {"original": original, "predicted": predicted}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Data sent to server successfully.")
        else:
            print("Failed to send data to server.")
    except Exception as e:
        print("Error sending data to server:", e)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    plate_text = recognize_license_plate(frame)

    cv2.putText(frame, plate_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    send_data_to_server(plate_text, plate_text)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
