import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Applicare uno sfondo
imgBackground = cv2.imread('risorse/background.png')

folderModePath = "risorse/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
# for path in folderModePath:
print(modePathList)

while True:
    success, img = cap.read()

    # Dimensione del video catturato dalla webcam
    imgBackground[162:162 + 480, 55:55 + 640] = img

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

