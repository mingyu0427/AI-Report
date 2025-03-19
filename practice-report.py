# 2.1
print( 200,'+',300 + 400,'=', 200 + 300 + 400)

# 2.2
weight = 30
height = 60
print(weight)
print(height)

# 2.3
width = 30
height = 60
print(width * height)

# 2.4
width = 40
height = 20
print(width * height * 1/2)

# 2.5
width = int(input('정사각형의 밑변을 입력하시오:'))
area = int(input('정사각형의 면적:'))

# 2.6
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

# 2.7
print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)

# 2.8
for a in range(2, 7):
    print(a)
    for n in range(2, 3):
        print(n)
        print('a = {}, n = {}, a ** n = {}'.format(a, n, a ** n))
# 2.9
print('섭씨 화씨')
print('0 32.0')
print('10 50.0')
print('20 68.0')
print('30 86.0')
print('40 104.0')
print('50 122.0')

# 2.10
c = int(input('섭씨 온도를 입력하세요:'))
f = (9/5) * c + 32
print('섭씨',c,'화씨',f,'도 입니다')

# 2.11
f = int(input('화씨 온도를 입력하세요:'))
c = f * (5/9) - (160/9)
print('화씨',f,'도는 섭씨',c,'도 입니다')

# 2.12
radius = 11
pi =3.141592
print('원의 반지름:',radius)
print('원의 둘래:',radius * 2 * pi)
print('원의 넓이:',radius **2 * pi)

# 2.13
radius = int(input('원의 반지름을 입력하세요:'))
pi = 3.141592
print('원의 둘래:',radius * 2 * pi)
print('원의 넓이:',radius ** 2 * pi)

# 2.14
for x in range(2, 11):print(x,'의 제곱근',x**(1/2))

# 2.15
a = int(input('밑변을 입력하세요:',))
b = int(input('높이를 입력하세요:',))
c = (a**2 + b**2)**(1/2)
print('빗변:',c)

# 2.16
b = 1 + 2j
c = b*((3**0.5/2)+0.5j)
print('회전하기 전:',b)
print('30도 회전한 후 :',c)

# 2.17
for b in range(0,10):print(2 << b)

# 2.18
a = int(input('정수를 입력하세요:',))
b = 0
c = a % 2
print('이 수가 짝수인가요?',b == c)

# 2.19
a = int(input('정수를 입력하세요 :'))
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',a % 2 == 0 and 0 <= a <= 100)

# 2.20
print(bin(5&6))
print(bin(5|6))
print(bin(5^6))

# 2.21
a = int(input('정수를 입력하시오:'))
print(a,'의 2진수 값:', bin(a))
print(a,'의 2진수 값에 대한 비트단위 부정값:',bin(~a))      

# 2.22
a = int(input('정수 a를 입력하시오:'))
b = int(input('정수 b를 입력하시오:'))
print('a/b의 몫: ',a//b)
print('a/b의 나머지:',a%b)

# 2.23
a = int(input('세 자리 정수를 입력하세요:'))
print('백의 자리:',a//100)
print('십의 자리:',(a//10)%10)
print('일의 자리:',a%10)

# 2.24
a = int(input('세 자리 정수를 입력하세요 :'))
print(a%10)
print(a//10)%10)
print(a//100)


    
        
    
