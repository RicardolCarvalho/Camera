# Camera

Este é um programa que utiliza a biblioteca OpenCV para capturar imagens e como foi desenvolvido em uma materia de Algebra Linear, ele tambem consegue fazer operações com as imagens capturadas.

Para instalar, você pode usar uma de duas maneiras.

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/RicardolCarvalho/camera.git
    cd camera
    pip install .

A segunda maneira é instalar direto do repositório:

    pip install git+https://github.com/RicardolCarvalho/camera.git

Após instalar, o programa `camera` deve estar instalado. Então, executando o comando:

    camera

O programa deve abrir uma janela com a imagem da câmera. 

Pressionando a tecla `r` você faz a imagem começar a girar 360 graus.

Pressionando a tecla `d` você faz a imagem começar a girar mais rápido.

Pressionando a tecla `a` você faz a imagem começar a girar mais devagar.

Pressionando a tecla `c` você transforma a imagem em um cisalhamento.

Pressionando a tecla `esc` você faz a imagem parar de girar ou remover o cisalhamento.

Pressionando a tecla `q` você fecha a janela e o programa.