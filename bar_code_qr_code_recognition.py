import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

def process_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    barcodes = pyzbar.decode(image)
    result = []

    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")

        if barcode.type != "QRCODE":
            barcodeType = "BARCODE"
        else:
            barcodeType = barcode.type

        result.append({
            "barcode": barcodeData,
            "type": barcodeType
        })

    return image, len(barcodes),result

