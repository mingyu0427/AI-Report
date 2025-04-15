#7.5
#10,(10, 20),(20, 30, 40),(10, 20, 30),(20, 40),(40, 30, 20, 10)
#7.9
#s1 = ([1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 3, 7, 3])
#t1 = tuple(s1)
#u1 = set(s1)
#print("주어진 튜플:{}".format(t1))
#print("중복 제거 튜플:{}".format(u1))
#7.13
#given_list=[5,6,3,9,2,12,3,8,7]
#print('주어진 리스트:',given_list)
#list_length=len(given_list)-1
#for _ in range(list_length):
#    for i in range(list_length):
#        if given_list[i]>given_list[i+1]:
#            given_list[i],given_list[i+1]=given_list[i+1],given_list[i]
#    list_length-+1
#print('정렬된 결과',given_list)
#7.17
#population_A=(100,150,230,120,180,100,140,95,81,21,4)
#population_B=(300,420,530,420,400,300,40,5,1,1,1)
#print('마을A와 B에 보낼 투표용지의 개수는 각각{}장과 {}장입니다.'.format(sum(population_A[2:]), sum(population_B[2:])))
#print('마을A와 B의 고령화 정도는 각각{:0.3f}와 {:0.3f}입니다.'.format(sum(population_A[7:])/sum(population_A),sum(population_B[7:])/sum(population_B)))
#7.21
#str=input('회문인지 확인할 문자를 입력하세요.: ')
#str=str.replace('','')
#str=str.replace('.','')
#str=str.upper()
#if str==str[::-1]:
#    print('회문입니다.')
#else:
#    print('회문이 아닙니다.')
#7.25
