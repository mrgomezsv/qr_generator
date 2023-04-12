import qrcode
from PIL import Image

def generar_codigo_qr(url: str, nombre_archivo: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

if __name__ == "__main__":
    url = input("Ingresa la URL: ")
    nombre_archivo = input("Ingresa el nombre del archivo (con extensión .png): ")
    generar_codigo_qr(url, nombre_archivo)
    print(f"Código QR generado con éxito y guardado como {nombre_archivo}")
