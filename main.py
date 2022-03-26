import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = cv2.imread("tata.jpg")
#img=cv2.resize(img,None,fx=0.5,fy=0.5)
def gray_scale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#def threshold(image):
    #return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
    #return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #return cv2.threshold(img,127,255,cv2.THRESH_BINARY)

def noise_removal(image):
    return cv2.medianBlur(img,5)
    #return cv2.GaussianBlur(img, (5, 5), 0)
    #return cv2.bilateralFilter(img,9,75,75)

img=gray_scale(img)
#img=threshold(img)
img=noise_removal(img)

myconfig=" --psm 6 --oem 3"
#text = pytesseract.image_to_string(gray)
text = pytesseract.image_to_string(img,config=myconfig)
print(text)

text_file = open("tata.txt", "w")
text_file.write(text)
text_file.close()

cv2.imshow("img",img)
cv2.waitKey(0)