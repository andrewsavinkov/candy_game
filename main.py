# 2) Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
#
# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
#                                         ---1---
# 1) Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота 'интеллектом'
#                                         Решение
from random import randint as RI
import time as TI
#
# def introduce_players():
#     players=[]
#     players_total=int(input('Введите количество игроков:\t'))
#     for i in range(players_total):
#         players.append(input(f'Введите имя игрока {i+1}:\t'))
#     return (players, players_total)
#
# def players_turn():
#     global players_move
#     global now_to_move
#     index_list=[]
#     index=0
#     for i in players_move.keys():
#         index_list.append(i)
#
#     for item in players_move.keys():
#         if players_move[item]==True:
#             index=index_list.index(item)
#             players_move[item] = False
#     if index != len(index_list)-1:
#         index=index+1
#     else:
#         index=0
#     players_move[index_list[index]]=True
#     now_to_move = index_list[index]
#     return index_list[index]
#
# def take_candy(name):
#     global candy_total
#     candies_to_take=int(input(f'{name}, сколько конфет вы забираете? (мин. 1, макс. 28 шт.)\n'))
#     if candies_to_take<=28 and candies_to_take>=1 and candies_to_take<=candy_total:
#         candy_total = candy_total - candies_to_take
#         print(f'Конфет доступно: {candy_total}')
#     else:
#         print('Введите корректное количество конфет!')
#
#
# (my_players, players_count)=introduce_players()
# player_to_be_first=my_players[RI(0, players_count-1)]
# now_to_move=player_to_be_first
# players_move={}
# for i in range(len(my_players)):
#     players_move[my_players[i]]=False
#
#
# print('Начало игры!')
# TI.sleep(1.5)
# candy_total=int(input('Введите количество конфет:\t'))
# prize_candies=candy_total
# TI.sleep(1.5)
# print(f'Первым ходит:\t {player_to_be_first}')
# players_move[player_to_be_first]=True
# TI.sleep(1.5)
#
# while True:
#     take_candy(now_to_move)
#     if candy_total==0:
#         print(f'Поздравляю, {now_to_move}, вы победили и получаете все {prize_candies} конфет!')
#         break
#     else:
#         print(f'Теперь ходит:\t {players_turn()}')
#
# решение а, б)
from random import randint as RI
import time as TI
first_to_move=''
players={}
players['comp']=False
now_to_move=''
def take_candy(name):
     global candy_total
     candies_to_take=int(input(f'{name}, сколько конфет вы забираете? (мин. 1, макс. 28 шт.)\n'))
     if candies_to_take<=28 and candies_to_take>=1 and candies_to_take<=candy_total:
         candy_total = candy_total - candies_to_take
         print(f'Конфет доступно: {candy_total}')
     else:
         print('Введите корректное количество конфет!')

def comp_move():
    global candy_total
    candies_to_take=0
    print('Ходит компьютер!')
    if candy_total%28<2:
        if candy_total==29:
            candies_to_take=1
        else:
            candies_to_take=candy_total-29
    elif candy_total<=28:
        candies_to_take=candy_total
    else:
        candies_to_take=RI(1, 28)
    TI.sleep(1.5)
    print(f'Компьютер берет {candies_to_take} конфет')
    candy_total = candy_total - candies_to_take
    print(f'Конфет доступно: {candy_total}')

def players_turn():
    global players
    global now_to_move
    global first_to_move
    index_list=[]
    index=0
    for i in players.keys():
        index_list.append(i)
    first_to_move=index_list[RI(0,1)]
    for item in players.keys():
        if players[item]==True:
            index=index_list.index(item)
            players[item] = False
    if index != len(index_list)-1:
        index=index+1
    else:
        index=0
    players[index_list[index]]=True
    now_to_move = index_list[index]
    return index_list[index]

player_name=input('Введите имя игрока:\t')
players[player_name]=False

print('Начало игры!')
TI.sleep(1.5)
candy_total=int(input('Введите количество конфет:\t'))
prize_candies=candy_total
TI.sleep(1.5)
print(f'Первым ходит:\t {players_turn()}')

while True:
    if now_to_move==player_name:
        take_candy(now_to_move)
        if candy_total==0:
            print(f'Поздравляю, {now_to_move}, вы победили и получаете все {prize_candies} конфет!')
            break
        else:
            print(f'Теперь ходит:\t {players_turn()}')
    else:
        comp_move()
        if candy_total==0:
            print(f'Поздравляю, {now_to_move}, вы победили и получаете все {prize_candies} конфет!')
            break
        else:
            print(f'Теперь ходит:\t {players_turn()}')