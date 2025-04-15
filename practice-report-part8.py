#8.5
#import math as m
#for i in range(0, 181, 10):
#    print('sin({}) = {:.3f}, cos({}) = {:.3f}, tan({}) = {:.3f}'.format(i,m.sin(m.radians(i)), i, m.cos(m.radians(i)), i, m.tan(m.radians(i))))
#8.9
#import random as rd
#def game():
#    ai = rd.randrange(1,21)
#    a = 0
#    print(ai)
#    while True:
#        us = int(input('1~20 숫자 입력: '))
#        a += 1
#        if ai != us :
#            if us < ai :
#                print(f'{us}보다 큽니다.')
#                continue
#            else:
#                print(f'{us}보다 작습니다.')
#                continue
#        else:
#            print('정답입니다.')
#            if a<= 3:
#                print(f'{a}번만에 맞츰 천재')
#            elif a>3 and a<=6:
#                print(f'{a}번만에 맞춤 일반')
#            else:
#                print(f'{a}번만에 맞춤 바보')
#            break
#game()
            
        
