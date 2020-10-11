import os
from PIL import Image


#Confere se o arquivo é uma imagem
def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False


def reduzir_tamanho_img(input_dir, output_dir, ext='.jpg'):
    #Recebe o endereço para o diretório e devolve uma lista com os arquivos que estão dentro desse diretório
    lista_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    #Abre a imagem do diretório
    for nome in lista_arquivos:
        #Redimensiona as imagens
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        redimensionada = imagem.resize((1280, 720))
        nome_sem_extensao = os.path.splitext(nome)[0]
        redimensionada.save(os.path.join(output_dir, nome_sem_extensao + ext))

if __name__ == "__main__":
    diretorio = input(str("Diretório: "))

    reduzir_tamanho_img(diretorio, 'Reduzir_Img\output')