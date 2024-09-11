import numpy as np
import cv2 as cv

def rotacao_matriz(theta):
    roda = np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])
    return roda

def cisalhamento_matriz(shx, shy):
    cisalha = np.array([[1, shx, 0],
                        [shy, 1, 0],
                        [0, 0, 1]])
    return cisalha

def aplicar_rotacao(image, angulo):
    altura, largura = image.shape[:2]

    cx, cy = largura // 2, altura // 2

    rotacao = rotacao_matriz(np.radians(angulo))

    imagem_rotacionada = np.zeros_like(image)

    for y in range(altura):
        for x in range(largura):
            x_rel = x - cx
            y_rel = y - cy

            x_rot = rotacao[0, 0] * x_rel + rotacao[0, 1] * y_rel
            y_rot = rotacao[1, 0] * x_rel + rotacao[1, 1] * y_rel

            # Transladar de volta ao sistema original
            x_rot = int(x_rot + cx)
            y_rot = int(y_rot + cy)

            if 0 <= x_rot < largura and 0 <= y_rot < altura:
                imagem_rotacionada[y, x] = image[y_rot, x_rot]

    return imagem_rotacionada

def aplicar_cisalhamento(image, shx, shy):
    altura, largura = image.shape[:2]

    cx, cy = largura // 2, altura // 2

    cisalhamento = cisalhamento_matriz(shx, shy)

    imagem_cisalhada = np.zeros_like(image)

    for y in range(altura):
        for x in range(largura):
            x_rel = x - cx
            y_rel = y - cy

            x_cisalhado = cisalhamento[0, 0] * x_rel + cisalhamento[0, 1] * y_rel
            y_cisalhado = cisalhamento[1, 0] * x_rel + cisalhamento[1, 1] * y_rel

            # Transladar de volta ao sistema original
            x_cisalhado = int(x_cisalhado + cx)
            y_cisalhado = int(y_cisalhado + cy)

            if 0 <= x_cisalhado < largura and 0 <= y_cisalhado < altura:
                imagem_cisalhada[y, x] = image[y_cisalhado, x_cisalhado]

    return imagem_cisalhada

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    angulo = 0
    cx, cy = 0.5, 0.5
    rodar = False
    cisalhamento = False
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # Aplica a rotação ou cisalhamento ao frame
        if rodar:
            image = aplicar_rotacao(frame, angulo)
            # Incrementa o ângulo de rotação
            angulo += 1
            if angulo >= 360:
                angulo = 0

        elif cisalhamento:
            image = aplicar_cisalhamento(frame, cx, cy)
        else:
            # A variável image é um np.array com shape=(width, height, colors)
            image = np.array(frame).astype(float)/255

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

        if cv.waitKey(1) == ord('c'):
            cisalhamento = not cisalhamento
        
        if cv.waitKey(1) == ord('r'):
            rodar = not rodar

        if cv.waitKey(1) == 27:
            rodar = False
            cisalhamento = False

    cap.release()
    cv.destroyAllWindows()

run()
