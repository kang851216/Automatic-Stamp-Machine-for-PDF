from tkinter import *
from tkinter.filedialog import *
import os
import fitz  # Changed from 'from fitz import fitz, Rect'

pdfpath = ""
imgpath = ""
pdfdir = ""

def openpdfFile():
    global pdfpath, pdfdir
    pdffile = askopenfilename(title="Open File", filetypes=(("Pdf File", "*.pdf"), ("모든 파일", "*.*")))
    if pdffile:
        pdfpath = pdffile
        # Saves the result in the same folder as the source PDF
        pdfdir = os.path.join(os.path.dirname(pdffile), "result.pdf")
        lb1["text"] = pdfpath

def openimgFile():
    global imgpath
    imgfile = askopenfilename(title="Open File", filetypes=(("png File", "*.png"), ("모든 파일", "*.*")))
    if imgfile:
        imgpath = imgfile
        lb2["text"] = imgpath
    
def click_exe():
    global pdfpath, imgpath, pdfdir
    try:
        pdf = fitz.open(pdfpath)
        # Read the image bytes
        with open(imgpath, "rb") as f:
            img_bytes = f.read()

        for page in pdf:
            # MediaBox provides the width and height
            w = page.rect.width
            h = page.rect.height
            
            # Define the stamping area (Bottom of the page)
            # fitz.Rect(x0, y0, x1, y1)
            rect = fitz.Rect(0, 0.95 * h, w, h) 
            
            page.insert_image(rect, stream=img_bytes)
            
        pdf.save(pdfdir)
        pdf.close()
        lb3["text"] = "Succeed and Saved!"
        lb4["text"] = f"Saved at: {os.path.basename(pdfdir)}"
    except Exception as e:
        lb3["text"] = "Error occurred"
        print(f"Error: {e}")

# --- GUI Setup remains the same ---
top = Tk()
top.title("Automatic Stamp Machine")
top.geometry("600x170")

btn1 = Button(text="1.Select PDF File", command=openpdfFile)
btn2 = Button(text="2.Select IMG File", command=openimgFile)
btn3 = Button(text="3.Merge", command=click_exe)

lb1 = Label(top, text="empty", font=("System", 9))
lb2 = Label(top, text="empty", font=("System", 9))
lb3 = Label(top, text="", font=("System", 9))
lb4 = Label(top, text="", font=("System", 9))

lb5 = Label(top, text="1. Select pdf file", font=("System", 9))
lb6 = Label(top, text="2. Select stamp img file(png file)", font=("System", 9))
lb7 = Label(top, text="3. Click 'Merge' button", font=("System", 9))
lb8 = Label(top, text="4. Check 'result.pdf' in same directory", font=("System", 9))

# Layout
btn1.place(x=250, y=20); lb1.place(x=350, y=20)
btn2.place(x=250, y=70); lb2.place(x=350, y=70)
btn3.place(x=250, y=120); lb3.place(x=350, y=120); lb4.place(x=350, y=140)

lb5.place(x=5, y=20)
lb6.place(x=5, y=40)
lb7.place(x=5, y=60)
lb8.place(x=5, y=80)

top.mainloop()