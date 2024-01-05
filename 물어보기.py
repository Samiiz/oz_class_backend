# 문제 : 정수 배열 arr와 자연수 k가 주어집니다.
#        만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.
#        이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.


def solution(arr, k):
    
    answer = []
    
    if k % 2 == 1:  # k가 홀수인 경우
        # num은 arr리스트 안의 각각의 원소를 뜻한다.
        # for num in arr은 arr의 각각의 요소들을 에 대하여 특정 연산을 반복한다.
        # 그러므로 num * k for num in arr은 arr의 각각의 요소(num)에 대하여 * k 를 반복한다.
        # 그리고 그 리스트를 answer이라는 변수로 선언한다.
        answer = [num * k for num in arr]
    else:  # k가 짝수인 경우
        answer = [num + k for num in arr]
        
    return answer


# 문제 : 정수 리스트 num_list가 주어질 때,
#        마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을  
#        마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여
#        return하도록 solution 함수를 완성해주세요.


def solution(num_list):
    answer = []
    
    last_num = num_list[-1]
    before_last_num = num_list[-2]
    
    if(last_num > before_last_num) :
        answer = num_list + [last_num - before_last_num]
    else :  # elif(last_num < before_last_num) 프로그래머스 기준 정확도 95% 왜??
        answer = num_list + [last_num * 2]
    
    return answer


# 문제 : 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 
#        예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
#        문자열 str1과 str2가 주어질 때,
#        str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.


def solution(str1, str2):
    answer = 0
    for i in range( len(str2) - len(str1) + 1 ) : # 이 부분에 대한 생각을 정리하기
        if str2[i:i+len(str1)] == str1 : # 이 부분도!
            answer = 1
            break
    return answer
## 리스트 컴플리헨션 x for x in range(10) 이걸보니 더 이해가 안간다

# 문제 : 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
#        입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# set()을 사용하면 될줄알았는데 문자열도 중복이 있으면 없애버려서 안됨!!


str1, str2 = input().strip().split(' ')

solved_str = str1 + str2
print(solved_str)

# 타인 정답
# 1 
print(input().strip().replace(' ', ''))
# 2
str1, str2 = input().strip().split(' ')
print(str1, str2, sep='')
# 3
print(''.join(input().strip().split(' ')))