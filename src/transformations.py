import cv2
import numpy as np

def load_image(image_path: str) -> np.ndarray:
    """
    Carga la imagen en formato BGR (estándar de OpenCV)
    y la devuelve como un arreglo NumPy.
    """
    image = cv2.imread(image_path)  # Lee la imagen en formato BGR
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en {image_path}")
    return image

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path: str) -> np.ndarray:
    """
    Carga la imagen en formato BGR (estándar OpenCV).
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en {image_path}")
    return image

def show_image_cv2(image_bgr: np.ndarray, title: str = "Imagen"):
    """
    Muestra la imagen usando Matplotlib, convirtiéndola de BGR a RGB.
    """
    # Convertir de BGR a RGB
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    
    # Mostrar con Matplotlib
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')  # Omitir ejes para una vista más limpia
    plt.show()

#Rotación cv2.getRotationMatrix2D

import cv2
import numpy as np

def rotate_image(image_bgr: np.ndarray, angle: float) -> np.ndarray:
    """
    Rota la imagen (BGR) un número de grados especificado alrededor de su centro.
    Utiliza cv2.getRotationMatrix2D + cv2.warpAffine.
    """
    # Dimensiones de la imagen
    (height, width) = image_bgr.shape[:2]
    
    # Calcula el centro
    center = (width // 2, height // 2)
    
    # Obtiene la matriz de rotación (2x3)
    # scale=1.0 → no hay escalado
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Aplica la transformación
    rotated = cv2.warpAffine(
        image_bgr,              # imagen de entrada
        rotation_matrix,        # matriz de transformación
        (width, height)         # tamaño de la imagen de salida (ancho, alto)
    )
    return rotated

#Escalado cv2.resize

def scale_image(image_bgr: np.ndarray, fx: float, fy: float) -> np.ndarray:
    """
    Escala la imagen multiplicando el ancho por fx y el alto por fy.
    """
    # cv2.resize usa (ancho, alto) y fx/fy (factor en x e y)
    scaled = cv2.resize(image_bgr, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled


#Reflexión (Espejo) cv2.flip

def reflect_image(image_bgr: np.ndarray, flip_code: int) -> np.ndarray:
    """
    flip_code = 0 -> flip vertical
    flip_code = 1 -> flip horizontal
    flip_code = -1 -> flip en ambos ejes
    """
    flipped = cv2.flip(image_bgr, flip_code)
    return flipped


#Traslación (Mover la imagen en x, y) warpAffine

def translate_image(image_bgr: np.ndarray, shift_x: float, shift_y: float) -> np.ndarray:
    """
    Desplaza la imagen shift_x píxeles horizontalmente y shift_y píxeles verticalmente.
    shift_x > 0 -> mueve a la derecha
    shift_y > 0 -> mueve hacia abajo
    """
    (height, width) = image_bgr.shape[:2]
    
    # Construir la matriz de traslación
    T = np.float32([
        [1, 0, shift_x],
        [0, 1, shift_y]
    ])
    
    # warpAffine necesita (width, height) como tamaño de la salida
    translated = cv2.warpAffine(image_bgr, T, (width, height))
    
    return translated

