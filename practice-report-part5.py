#5.5
#def inch2cm(inch):
#    cm=inch*2.54
#    return cm
#for i in range(1, 6):
#    print('{}인치={}센티미터'.format(i, inch2cm(i)))
#5.9
#nums = list(map(int(input('정수를 여러 개 입력하시오').split())))
#def mean_of_n(nums):
#    mean_of_n=sum(nums) / len(nums)
#    return mean_of_n
#def max_of_n(nums):
#    max_of_n = max(nums)
#    return max_of_n
#def min_of_n(nums):
#    min_of_n = min(nums)
#    return min_of_n
#print('평균값은','{:.1f}'.format(mean_of_n(nums)))
#print('최댓값은',max_of_n(nums))
#print('최솟값은'.min_of_n(nums))
#5.13
#def 정육면체(s):
#    정육면체_area=s**3
#    return 정육면체_area
#def 직육면체(w, h, l):
#    직육면체_area=w* h* l
#    return 직육면체_area
#def 원뿔(r, h):
#    원뿔_area=(1/3)*3.14*r**2
#    return 원뿔_area
#def 구(r):
#    구_area=(4/3)*3.14*r**2
#    return 구_area
#def 원기둥(r, h):
#    원기둥_area=3.14*r**2*h
#    return 원기둥_area
#print(정육면체(12))
#print(정육면체(20))
#print(직육면체(3, 5, 6))
#print(원뿔(20, 10))
#print(구(15))
#print(원기둥(20, 10))
#5.17
#def sum_range(n1, n2):
#    numbers=list(range(n1,n2+1))
#    print('{}에서 {:3d}까디의 합: {:4d}'.format(n1,n2,sum(numbers)))
#sum_range(10,20)
#sum_range(40,100)
#5.21
#n=input('주민등록번호 첫 6숫자 형식 입력: ')
#if int(n[0:2])>=50:
#    year='19'+n[0:2]
#else:
#    year='20'+n[0:2]
#print('{}년 {}월 {}일'.format(year,n[2:4],n[4:6]))
#5.25
#s1 = 'Kang Young Min'
#s2 = ' Kang Young-Min'
#s3 = 'Park Dong Min'
#s4 = ' Park Dong-Yun'
#S = [s1, s2, s3, s4]
#for i in range(4):
#    result=S[i].replace(' ','')
#    result=result.replace('-','')
#    result=result.upper()
#    print('{}는 {}로 수정됨'.format(S[i], result))
#for i in S:
#    print('{}:{}개의 N이 나타남'.format(i,i.count('N')))
