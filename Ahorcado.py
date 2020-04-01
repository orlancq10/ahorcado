import numpy as np


class Ahorcado:

    def revisar_lista(self, new_list):
        lives = len(new_list)
        game_list = [""] * lives
        while lives > 0:
            letra = raw_input("Ingrese una letra: ")
            if new_list.__contains__(letra):
                posicion = new_list.index(letra)
                while posicion < len(new_list) - 1:
                    game_list[posicion] = letra
                    if new_list[posicion + 1: len(game_list)].__contains__(letra):
                        posicion = new_list.index(letra, posicion + 1, len(new_list))
                        if posicion <= len(new_list) - 1:
                            game_list[posicion] = letra
                    else:
                        posicion = posicion + 1
                    print (game_list)
                if not game_list.__contains__(""):
                    print ("Gano")
                    lives = lives = 0
            else:
                lives = lives - 1
                print ("Vidas restantes: " + str(lives))

    def enter_word(self, word):
        new_list = list(word)
        self.revisar_lista(new_list)


def main():
    word = raw_input('Ingrese la palabra para jugar: ')
    ahorcado = Ahorcado()
    ahorcado.enter_word(word)


if __name__ == '__main__':
    main()
