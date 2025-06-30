import cv2 
import pytesseract 
import pdfplumber 
import tempfile 
from pathlib import Path 

def pdf_to_images(pdf_path: str):    
 images = []    
 with pdfplumber.open(pdf_path) as pdf:        
   for page in pdf.pages:            
       images.append(page.to_image(resolution=300).original)    
 return images 


def image_to_text(img):    
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
  return pytesseract.image_to_string(gray) 

def extract_text(path: str):    
   path = Path(path)    
   if path.suffix.lower() == ".pdf":        
      imgs = pdf_to_images(str(path))    
   else:        
      import cv2        
      imgs = [cv2.imread(str(path))]    
   full_text = "\n".join(image_to_text(im) for im in imgs)    
   return full_text