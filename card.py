import random, copy
import numpy as np
import itertools

class Card:

    def constructor_card(self):
        numbers = range(1, 90)
        self.gen_numb = [sorted(random.sample(numbers, 5)) for i in range(3)]

        self.game_card = ' '.join(['{:>3}' for i in range(9)])
        for line in self.gen_numb:
            for cell in '_' * 4:
                line.insert(random.randint(0, len(line) - 1), cell)
        return'\n'.join([self.game_card.format(*line) for line in self.gen_numb])


    def constructor_barrel(self):
        self.barrel_list = [i for i in range(1, 91)]
        self.shuffle_brl = random.sample(self.barrel_list, 90)
        return self.shuffle_brl

class Game:

    def play_game(self):
        self.user_card = Card()
        self.AI_card = Card()
        self.user_card1 = copy.deepcopy(self.user_card.constructor_card())
        self.AI_card1 = copy.deepcopy(self.AI_card.constructor_card())
        self.keg = copy.deepcopy(self.user_card.constructor_barrel())

        user_score = 0
        AI_score = 0
        i = 0
        print(f'Правила игры в лото. Игра ведется с помощью спе циальных карточек, на которых \n '
              f'отмечены числа,и фишек (бочонков) с цифрами. Количество бочонков — 90 штук \n'
              f'(с цифрами от 1 до 90). Каждый ход выбирается один случайный бочонок и выводится на экран. \n'
              f'Также выводятся карточка игрока и карточка компьютера. \n'
              f'Пользователю предлагается зачеркнуть цифру на карточке или продолжить. \n'
              f'Если игрок выбрал "зачеркнуть": \n'
              f'Если цифра есть на карточке - она зачеркивается и игра продолжается.\n'
              f'Если цифры на карточке нет - игрок проигрывает и игра завершается. \n'
              f'Если игрок выбрал "продолжить": \n'
              f'Если цифра есть на карточке - игрок проигрывает и игра завершается. \n'
              f'Если цифры на карточке нет - игра продолжается. \n'
              f'Побеждает тот, кто первый закроет все числа на своей карточке.')

        print(f'\n ----------карточка Компьютера------\n {self.AI_card1}')

        while i <= len(self.keg):
            try:
              print(f'\n ----------карточка игрока----------\n {self.user_card1}')
              print('бочонок ', self.keg[i])

              user_answer = input('Зачеркнуть номер бочонка есть в карточке: у / n ')
              if 'n' != user_answer != 'y':
                   print("необходимо ввести y или n, попробуйте еще раз")
                   continue

              if str(self.keg[i]) in self.user_card1 and user_answer == 'y':
                  user_score += 1
              elif str(self.keg[i]) in self.user_card1 and user_answer == 'n':
                   return 'Вы ответили невeрно! Игра окончена'
              elif str(self.keg[i]) not in self.user_card1 and user_answer == 'n':
                   pass
              elif str(self.keg[i]) not in self.user_card1 and user_answer == 'y':
                   return 'Вы ответили невeрно! Игра окончена'

              if str(self.keg[i]) in self.AI_card1:
                  AI_score += 1

              i += 1

              if user_score == 15:
                  return 'Вы победили!'
              elif AI_score == 15:
                  return 'Вы проиграли, мистер Андерсон.'

            except IndexError:
                if user_score > AI_score:
                   return 'Вы победили!'
                else:
                   return 'Вы проиграли, мистер Андерсон.'


            print('очки пользователя: ', user_score)
            print('очки компьютера: ', AI_score)


a = Game()
print(a.play_game())
