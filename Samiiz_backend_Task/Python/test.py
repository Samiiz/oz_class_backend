def translate(user_input) :
    replace_input = user_input.replace( " ", "" )
    return replace_input

user_input = input()
user_input = translate(user_input)
middle = len(user_input) // 2

if len(user_input)% 2 == 0 :
    print(f'당신의 입력한 내용의 길이는 {len(user_input)}글자 입니다')
    print(f'가운데 글자는 "{user_input[middle-1:middle+1]}"')
else :
    print(f'당신의 입력한 내용의 길이는 {len(user_input)}글자 입니다')
    print(f'가운데 글자는 "{user_input[middle]}"')