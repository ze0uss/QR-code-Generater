import qrcode
import tkinter as tk
from PIL import Image, ImageTk

#function to generate the a QR:
def generate_qr_code():
    text = entry.get() # Get text fom the inputfiled
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=7)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color ="Black",back_color ="white")
    img.save("generated_qr.png") #save the QR code as input
    # display the QR codeimage above the input field
    qr_image = Image.open("generated_qr.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image


# creat the main window
window = tk.Tk()
window.title("QR code Generator - saurabhk.in")

# create an input field for the user to enter text
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

#creat a button
generate_button = tk.Button(window, text="Generate QR code", command=generate_qr_code)
generate_button.pack()

# create a label to display the QR code image
qr_label = tk.Label(window)
qr_label.pack()

#start the main loop
window.mainloop()
