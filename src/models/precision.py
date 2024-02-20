from time import sleep
velocidade = ''

def precisao(botao:str):
    cansado = "cansado"
    normal = "normal"
    rapido = "rapido"
    match botao:
        case "cansado":
            velocidade = cansado
        case "normal":
            velocidade = normal
        case "rapido":
            velocidade = rapido
    print(velocidade)
    sleep(velocidade)


if __name__== "__main__":
    precisao('velocidade')
    
    