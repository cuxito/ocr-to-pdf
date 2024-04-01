# pip install pdf2image pytesseract pymupdf
# code by: cuxito
# leng: spa

from pdf2image import convert_from_path
import pytesseract
import fitz  # PyMuPDF

# Ruta al archivo PDF de entrada
input_pdf_path = 'ruta/a/tu/pdf_con_imagenes.pdf'
# Ruta al archivo PDF de salida
output_pdf_path = 'ruta/a/tu/pdf_salida.pdf'


def ocr_pdf_and_maintain_format(input_pdf_path, output_pdf_path):
    # Abrir el PDF original
    doc = fitz.open(input_pdf_path)
    
    # Convertir el PDF a una lista de imágenes
    images = convert_from_path(input_pdf_path, dpi=300)
    
    for page_num, image in enumerate(images):
        # Obtener el tamaño de la página original
        page = doc.load_page(page_num)  # Cargar la página actual
        pix = page.get_pixmap()  # Obtener un pixmap para la página
        zoom_x = 595.0 / pix.width  # Calcular el zoom basado en el ancho de la página (A4)
        zoom_y = 842.0 / pix.height  # Calcular el zoom basado en el alto de la página (A4)
        
        # Aplicar OCR a la imagen
        text = pytesseract.image_to_string(image, lang="spa")  # Asumiendo español; cambia "spa" según sea necesario
        
        # Crear un diccionario para el bloque de texto
        text_dict = {"text": text}
        
        # Insertar el texto en la página correspondiente
        page.insert_text((0, 0), text, fontsize=11, rotate=0, overlay=True)
    
    # Guardar el nuevo PDF
    doc.save(output_pdf_path)

ocr_pdf_and_maintain_format(input_pdf_path, output_pdf_path)
