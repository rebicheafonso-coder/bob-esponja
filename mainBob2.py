import pygame

pygame.init()

LARGURA, ALTURA = 720,720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("menu primeiro jogo")

#Variavel com a cor do fundo em RGB
cor_fundo = (30,144,255)

rodando = True
while rodando:
    for evento in pygame.event.get()
        if evento.type == pygame.QUINt:
            rodando = False

    #Pintar o fundo da tela 
    tela.filL(cor_fundo)

    pygame.display.flip()

pygame.quint()