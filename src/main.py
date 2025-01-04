from transformations import load_image, show_image_cv2

def main():
    # Ruta relativa hacia la imagen
    img = load_image("../img/prueba1.jpg")
    print("Dimensiones de la imagen:", img.shape)
    
    # Visualizar
    show_image_cv2(img, "Visualización con Matplotlib")

if __name__ == "__main__":
    main()


#PROBAR FUNCIONES

# src/main.py
from transformations import (
    load_image, show_image_cv2,
    rotate_image, scale_image, reflect_image, translate_image
)

def main():
    # 1. Carga la imagen
    img = load_image("../img/prueba1.jpg")
    
    # 2. Rotar la imagen 45 grados
    rotated_img = rotate_image(img, 45)
    show_image_cv2(rotated_img, "Imagen Rotada 45°")
    
    # 3. Escalar la imagen a la mitad
    scaled_img = scale_image(img, fx=0.5, fy=0.5)
    show_image_cv2(scaled_img, "Imagen Escalada a la Mitad")
    
    # 4. Reflejar la imagen horizontalmente
    flipped_h_img = reflect_image(img, 1)  # flip_code=1: flip horizontal
    show_image_cv2(flipped_h_img, "Imagen Reflejada Horizontalmente")
    
    # 5. Trasladar la imagen 100 px a la derecha y 50 px hacia abajo
    translated_img = translate_image(img, 100, 50)
    show_image_cv2(translated_img, "Imagen Trasladada")

if __name__ == "__main__":
    main()

#BRAIN

# src/main.py
from transformations import (
    load_image,
    show_image_cv2,
    rotate_image,
    scale_image,
    reflect_image,
    translate_image
)

def main():
    # 1. Cargar imagen (ajusta la ruta si tu imagen se llama distinto o está en otra carpeta)
    img = load_image("../img/brain.jpg")
    print("Dimensiones originales:", img.shape)

    # 2. Rotar la imagen 45 grados
    rotated_img = rotate_image(img, 45)
    show_image_cv2(rotated_img, "Imagen Rotada 45°")

    # 3. Escalar la imagen a 0.2 (20% de su tamaño original)
    scaled_img = scale_image(img, fx=0.2, fy=0.2)
    show_image_cv2(scaled_img, "Imagen Escalada 0.2x")

    # 4. Reflejar la imagen (flip horizontal)
    flipped_img = reflect_image(img, 1)  # 1 = flip horizontal
    show_image_cv2(flipped_img, "Imagen Reflejada Horizontalmente")

    # 5. Trasladar la imagen (100 px a la derecha, 50 px abajo)
    translated_img = translate_image(img, 100, 50)
    show_image_cv2(translated_img, "Imagen Trasladada")

if __name__ == "__main__":
    main()

