from cv2 import resize,imread,cvtColor,COLOR_BGR2RGB, imwrite
from numpy import ndarray




def carregar_imagem(caminho_imagem:str)->ndarray:
    image_BGR = imread(caminho_imagem)
    image_RGB = cvtColor(image_BGR,COLOR_BGR2RGB)
    return image_RGB


def redimensionar(imagem:ndarray,nova_largura:float,nova_altura: float)->ndarray:
    return resize(imagem,dsize=(nova_largura, nova_altura))


if __name__ == "__main__":
    from pathlib import Path
    from os.path import join

    root = Path.cwd()
    print(root)
    
    # figma -> 1162x705
    
    LARGURA = 1162
    ALTURA = 705

    images = join(root,"images")
    imagem_desligada = "eyee.jfif"
    imagem_ligada = "eye.jfif"
    
    
    desligada = carregar_imagem(join(images,imagem_desligada))
    nova_desligada = redimensionar(desligada,LARGURA,ALTURA)
    
    ligada = carregar_imagem(join(images,imagem_ligada))
    nova_ligada = redimensionar(ligada,LARGURA,ALTURA)
    
    imwrite(join(images,"ligada.jpg"),nova_ligada)
    imwrite(join(images,"desligada.jpg"),nova_desligada)
    