import cv2 #opencv
import numpy as np #np dla kernela
import goslate #dla google translate

gs = goslate.Goslate()

###
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract #dla image_to_string

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
###

print '--- Poczatek ---'
print ' '
# odczyt obrazka opencv
obraz = cv2.imread("2a.png")
cv2.imshow('PRZED',obraz)
# Konwersja na szare
obraz = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
# dylatacja i erozja, pozbycie sie szumow
kernel = np.ones((1, 1), np.uint8)
obraz = cv2.dilate(obraz, kernel, iterations=1)
obraz = cv2.erode(obraz, kernel, iterations=1)

while(True):

    # zapis obrazka
    #cv2.imwrite("2_usuniecie_szumow.png", obraz)
    #  Progowanie, by uzsykac obraz czarno bialy
    obraz = cv2.adaptiveThreshold(obraz, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imshow('PO',obraz)
    cv2.imwrite("2_Progowe.png", obraz)
    #czekaj 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()

# Rozpoznwanie dzieki modulowi tesseract i wyswietlenie w konsoli
print(pytesseract.image_to_string(Image.open('2_Progowe.png'),lang="eng"))
text = pytesseract.image_to_string(Image.open('2_Progowe.png'))
print ' '
print '------ Koniec -------'

print ' '

print 'Tlumaczenie'
print ' '
print(gs.translate(text, 'pl'))
print ' '
print 'Koniec Tlumaczenia'
