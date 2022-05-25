#IMPORTAMOS "opencv".
import cv2

def detectionImage(source_path):
    #INTRODUCIMOS RUTA A LA IMAGEN Y EL ARCHIVO "xml".
    imagePath = source_path
    # imagePath = cv2.resize(image_path, (600,600))
    cascPath = "haarcascade_frontalface_default.xml"

    #CARGAMOS CLASIFICADOR.
    faceCascade = cv2.CascadeClassifier(cascPath)

    #LEEMOS IMAGEN
    image1 = cv2.imread(imagePath)
    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = int(image1.shape[1] * scale_percent / 100)
    height = int(image1.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    image = cv2.resize(image1, dsize)


    #CONVERTIMOS IMAGEN A ESCALA DE GRISES
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #DETECTAMOS ROSTROS EN LA IMAGEN
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30))

    #NÚMERO DE ROSTROS ENCONTRADOS
    print("¡Rostros {0} encontrados!".format(len(faces)))

    #MOSTRAMOS CONTENIDO DE "faces":
    print("Rectángulos:\n",faces)

    #MARCAMOS LOS ROSTROS CON UN RECTANGULO
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #MOSTRAMOS RESULTADO.
    cv2.imwrite("images/output.png", image)
    



