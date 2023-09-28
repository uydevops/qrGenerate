import qrcode

# QR kodu oluşturulacak URL
url = "https://jacksonmersin.com/"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,  # QR kod sürümü (1 ila 40 arasında bir değer olabilir)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
    box_size=10,  # Kutu boyutu
    border=4,     # Kenar genişliği
)
qr.add_data(url)
qr.make(fit=True)

# QR kodu görüntüleme
qr_img = qr.make_image(fill_color="black", back_color="white")

# QR kodunu dosyaya kaydetme
output_path = "jacksonmersin_qr.png"
qr_img.save(output_path)

print("QR kodu oluşturuldu ve", output_path, "adlı dosyaya kaydedildi.")
