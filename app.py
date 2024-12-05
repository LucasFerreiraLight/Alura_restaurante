from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lucas', 8)
restaurante_praca.receber_avaliacao('Luana', 7)
restaurante_praca.receber_avaliacao('Joana', 9)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()