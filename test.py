import qrcode
from PIL import Image

# Payment information
iban = "YOUR_IBAN"
amount = "100.00"  # Amount in EUR
recipient_name = "Recipient Name"
reference = "Payment Reference"

# Format the payment data in the SEPA format
sepa_data = f"SPD\n\n\n\n\n\n\n\n{iban}\nEUR{amount}\n\n\n\n{recipient_name}\n\n\n\n\n\n\n\n\n\n\n\n\n{reference}\n\n\n\n\n\n\n\n\n\n\n\n"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(sepa_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
qr_img.save("payment_qr_code.png")

# Display the QR code image (optional)
qr_img.show()