import cv2

# reading the image  
qr_img = cv2.imread("MyQRCode1.png")
# using the QRCodeDetector() function  
qr_det = cv2.QRCodeDetector()  
# using the detectAndDecode() function  
val, pts, st_code = qr_det.detectAndDecode(qr_img)  
# printing the value  
print("Information:", val)  


