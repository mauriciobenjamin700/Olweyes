from pathlib import Path
from os.path import join, exists

local = Path.cwd()
root = local.parents[1]
images = join(root, "images")

print("Diretório de imagens:", images)

imagem = join(images, "eyee.jfif")

print("Caminho da imagem:", imagem)
print("Existe o diretório de imagens:", exists(images))
print("Existe a imagem:", exists(imagem))


#local = Path.cwd()

print("Local: ",local)
#print("Pai: ", local.parents[0])
#print("Avo: ", local.parents[1])