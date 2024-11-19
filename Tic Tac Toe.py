print("*" * 3, " Игра Крестики-нолики 3x3 ", "*" * 3)

board = list(range(1,10))

def sketch_board(board):
#  Функция для отображения игрового поля 3х3, где указаны числа от 1 до 9 в качестве индикатора клетки
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

def take_input(player_move):
# Функция для принятия хода пользователя с проверкой корректности ввода
# только целые числа от 1 до 9
# 1 клетку можно занять только 1 раз
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_move+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Проверьте, что вы ввели число")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_move
            valid = True
         else:
            print("Эта ячейка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_winner(board):
# функция на проверку победителя или ничью
   win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_comb:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
# функция, которая запускает все остальные функции
    counter = 0
    win = False
    while not win:
        sketch_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           winner = check_winner(board)
           if winner:
              print(winner, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    sketch_board(board)
main(board)

input("Нажмите Enter для выхода!")