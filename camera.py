import io
import socket
import struct
import cv2
import numpy as np
import pickle

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('192.168.2.151', 1237))
server_socket.listen(0)

# taking the lower half of the frame


def dividingImgHalf(redOnlyImg):
    height, width = redOnlyImg.shape
    # 480px -> y axis, 640px -> x axis
    processedImg = redOnlyImg[240:, :]
    return processedImg

# normalizing the pixels of the image


def normalizationFunc(originalPxs):
    # len(mask) -> 240
    for i in range(len(originalPxs)):
        for j in range(len(originalPxs[i])):
            originalPxs[i][j] = originalPxs[i][j]/255

# storing the pixels as arrays in a file


def storingPxs(normalizedArr, datafile, labelfile, orglabel):
    pickle_out = open(datafile, "wb")
    pickle.dump(normalizedArr, pickle_out)
    pickle_out.close()
    # forward only -> [1,0,0,0] -> [forward, left, right, back]
    pickle_out = open(labelfile, "wb")
    pickle.dump(orglabel, pickle_out)
    pickle_out.close()

# loading the pixels as arrays from a file


def loadingPxs(datafile, labelfile):
    pickle_in = open(datafile, "rb")
    X = pickle.load(pickle_in)
    print(X)

    pickle_in = open(labelfile, "rb")
    y = pickle.load(pickle_in)
    print(y)

# filtering red color for red tape that we are using


def extractingRedFromImg(originalImg):
    hsv = cv2.cvtColor(originalImg, cv2.COLOR_BGR2HSV)

    lowerRed = np.array([150, 50, 0])
    upperRed = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lowerRed, upperRed)
    return mask


# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
i = 0
try:
    img = None
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack(
            '<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, decode the bytes of the frame using opencv
        # and then display the frame
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        mask = dividingImgHalf(extractingRedFromImg(img))
        cv2.imshow("orginal", img)
        cv2.imshow("mask", mask)
        storingPxs(normalizationFunc(mask),
                   "dataFor.pickle", "labelsFor.pickle", [0, 1, 0, 0])
        i += 1
        print(i)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    connection.close()
    server_socket.close()


# canny dosent work
# # Gaussian Blur is an average of a pixel to its surrounding pixels, using
#         # kernel convolution
#         blur = cv2.GaussianBlur(img, (5, 5), 0)
#         # edge detection using canny algo
#         canny = cv2.Canny(blur, 50, 150)
#         # canny displayed
#         cv2.imshow("canny", canny)
#         # gray-scaled image displayed
#         cv2.imshow("gray", img)
