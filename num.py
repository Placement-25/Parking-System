import cv2
import pytesseract

# Initialize the video capture from your camera (0 for default camera)
cap = cv2.VideoCapture(0)

# Load Tesseract and set the path to the Tesseract executable (update with your Tesseract path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize a variable to store the license plate number
license_plate_number = ""

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    if not ret:
        break

    # Perform preprocessing as needed (grayscale, thresholding, etc.)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Display the processed frame with the detected license plate text
    cv2.putText(frame, "Number Plate: " + license_plate_number, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Number Plate Detection", frame)

    # Check for key press events
    key = cv2.waitKey(1)
    
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord(' '):  # Spacebar key press
        # Capture an image from the current frame
        captured_image = frame

        # Extract the license plate number from the captured image
        captured_gray = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)
        _, captured_thresh = cv2.threshold(captured_gray, 128, 255, cv2.THRESH_BINARY)
        captured_license_plate_text = pytesseract.image_to_string(captured_thresh, config='--psm 7')
        
        license_plate_number = captured_license_plate_text
        print("Captured Plate Number:", license_plate_number)

# Release the VideoCapture and close any open windows
cap.release()
cv2.destroyAllWindows()
