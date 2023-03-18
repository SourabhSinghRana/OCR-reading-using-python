from PIL import Image
from pytesseract import pytesseract
import pandas as pd

fileDF = pd.read_csv(r"input\files_names.csv")
file_names = fileDF['FILE_NAMES'].unique().tolist()

def convert_img_to_txt(fl):
    
    targetFP = open(r"output\{}.txt".format(fl[:-4]),"w+")

    path_to_tesseract = r"D:\Installed Software\tess\tesseract.exe"
    image_path = r"input\images\{}".format(fl)

    img = Image.open(image_path)

    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    #print(text[:-1])

    targetFP.write(text[:-1])
    
    targetFP.close()


# Defining main function
def main():
	
    for fl in file_names:
       convert_img_to_txt(fl)
       print("Completd for: "+fl)
        


# Using the special variable
# __name__
if __name__=="__main__":
	main()
