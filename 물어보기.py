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