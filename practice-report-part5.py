#6.1
    #40
    #60
    #30
    #60
    #70
    #90
    #20
    #7

#6.3
#list1 = [3, 5, 7]
#list2 = [2, 3, 4, 5, 6]
#for i in list1:
 #   print('')
  #  for j in list2:
   #     print(i, '*',j, '=', i*j)

#6.5
#list1 = ['I like', 'I love']
#list2 = ['pancakes.', 'kiwi juice.', 'espresso.']
#print(list1[0],list2[0])
#print(list1[0],list2[1])
#print(list1[0],list2[2])
#print(list1[1],list2[0])
#print(list1[1],list2[1])
#print(list1[1],list2[2])

#.6.7
#n_list = [10, 20, 30, 50, 60]
#print("리스트 원소들:",n_list)
#print("리스트 원소들의 합:",n_list[0]+n_list[1]+n_list[2]+n_list[3]+n_list[4])

#.6.9
#n_list = [10, 20, 30, 50, 60]
#print("리스트 원소들:",n_list)
#print("리스트 원소들 중 최대값:",n_list[4])

#.6.11
#n_list = [45, 67, 20, 34, 2]
#print("합:",sum(n_list))
#print("평균:",sum(n_list)/len(n_list))
#print("최댓값:",max(n_list))
#print("최솟값:",min(n_list))

##6.13
#nums = list(map(int, input('10개의 수를 입력하세요: ').split()))
#print('합 :', sum(nums))
#nums_average = sum(nums) / len(nums)
#print('평균 :', nums_average)
#nums_sigma = 0
#for i in nums:
#    nums_sigma += (i - nums_average) ** 2
#print('표준편차 : {:.2f}'.format((nums_sigma / len(nums)) ** 0.5))

#.6.15
#greet = 'Have a beautiful day.'
#print(greet[0:4])
#print(greet[7:16])
#print(greet[17:21])

#.6.17
#a ="animals = ['dog', 'cat', 'tiger', 'lion']"
#print(a)
#animals.append(animals.pop(0))
#print('animals=',animals)
#for i in animals:
#    print('I lovw {}.'.format(i))

##6.19
#s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
#new_s_list = list(set(s_list))
#for i in s_list:
#    if not i in new_s_list:
#        new_s_list.append(i)

##6.21
#src = input("문자를 입력하세요 : ")
#print(f"src = {src}")
#output = src[0]
#cnt = 0
#for char in src:
#    if output[-1] == char:
#        cnt += 1
#    else:
#        output += str(cnt) + char
#        cnt = 1
#output += str(cnt)
#print(f"output = {output}")

##6.23
#person1 =['온달', 20, 1, 180.0, 100.0]
#person2 = ['이사부', 25, 1, 170.0, 70.0]
#person3 = ['평강', 22, 0, 169.0, 60.0]
#person4 = ['혁거세', 40, 1, 150.0, 50.0]
#def persons(person_list):
#    result = {}
#    divide_list = []
#    for i in range(int(len(person_list) / 5)):
#        divide_list.append(person_list[i * 5:i * 5 + 5])
#    result['n_persons'] = len(divide_list)
#    result['average_age'] = 0
#    result['n_male'] = 0
#    result['f_male'] = 0
#    result['person_list'] = divide_list
#    for i in divide_list:
#        result['average_age'] += i[1]
#        if i[2] ==1:
#            result['n_male'] += 1
#        else:
#            result['f_male'] += 1
#    result['average_age'] /= result['n.persons']
#    return result
#person_list = person1 + person2 + person3 + person4
#print(persons(person_list))
            
       



