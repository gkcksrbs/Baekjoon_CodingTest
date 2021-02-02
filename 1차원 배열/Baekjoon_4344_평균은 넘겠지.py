# # 1. 테스트 케이스의 개수를 입력 받는다. 입력 받은 수가 자연수가 아닌 경우 다시 입력 받도록 한다.
# # 2. 각 테스트 케이스에 대한 학생 수를 입력 받고 각 학생의 점수를 입력 받는다.
# # 3. 학생 수는 자연수가 아니고 점수가 0보다 작거나 100보다 크면 다시 입력 받도록 한다.
# # 4. 학생 수와 점수의 개수가 일치하지 않을 경우에도 다시 입력 받도록 한다.
# # 5. 리스트를 하나 만들고 각 테스트 케이스를 리스트로 만들어 저장한다.
# # 6. 각 테스트 케이스에 대한 평균 값을 새로운 리스트에 저장한다.
# # 7. 각 테스트 케이스에 대해 평균 값보다 높은 학생 수를 새로운 리스트에 저장한다.
# # 8. 각 테스트 케이스에 대한 총 학생수에 대한 평균 보다 높은 학생의 비율을 구하여 새로운 리스트에 저장하고 출력한다.
#
# # 테스트 케이스의 개수 입력
# while(True):
#     num = int(input())
#     if(0 < num):
#         break
#
# #테스트 케이스에 대한 학생 수 및 각 학생의 점수 입력
# test_case_lst = []
#
# for i in range(num):
#     while(True):
#         test_case = list(map(int, input().split()))
#
#         if(test_case[0] > 0): # 학생 수가 자연수인지 확인
#             nonzero_student = True
#         else:
#             nonzero_student = False
#
#         for j in test_case: # 점수에 대해 올바르게 입력했는지 확인
#             if (0 <= j <= 100):
#                 check_score = True
#             else:
#                 check_score = False
#
#         if(test_case[0] == len(test_case) - 1): # 학생 수와 점수의 개수가 일치하는지 확인
#             check_student = True
#         else:
#             check_student = False
#
#         if(nonzero_student and check_score and check_student): #위의 세 가지 모두 만족하였을 경우 while문 탈출
#             test_case.pop(0)
#             test_case_lst.append(test_case)
#             break
#
# # 각 평균값 구하여 평균값 리스트에 저장
# mean_lst = [0 for i in range(num)]
#
# for i in range(num):
#     mean_lst[i] = sum(test_case_lst[i], 0.0) / len(test_case_lst[i])
#
# # 평균보다 높은 학생수를 구하여 리스트에 저장
# over_avg_student_lst = [0 for i in range(num)]
#
# for i in range(num):
#     avg = mean_lst[i]
#     for j in range(len(test_case_lst[i])):
#         if (test_case_lst[i][j] > avg):
#             over_avg_student_lst[i] += 1.0
#
# # 평균보다 높은 학생의 비율을 구하여 리스트에 저장
# percent_over_avg_lst = []
#
# for i in range(num):
#     percent_over_avg = over_avg_student_lst[i] / len(test_case_lst[i]) * 100
#     percent_over_avg_lst.append(percent_over_avg)
#
# # 평균보다 높은 학생의 비율 출력
# for i in percent_over_avg_lst:
#     print(round(i,3),"%")

c = int(input())
lst = []
for _ in range(c):
    count = 0
    tmp = list(map(int, input().split()))
    num = tmp.pop(0)
    avg = sum(tmp) / num
    for i in range(len(tmp)):
        if tmp[i] > avg:
            count += 1
    lst.append(count/num*100)

for i in range(len(lst)):
    print(str('%0.3f' % lst[i])+"%")

