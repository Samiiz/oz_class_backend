# import random

# 로또번호_1 = random.randint(1, 45)
# 로또번호_2 = random.randint(1, 45)
# 로또번호_3 = random.randint(1, 45)
# 로또번호_4 = random.randint(1, 45)
# 로또번호_5 = random.randint(1, 45)
# 로또번호_6 = random.randint(1, 45)
# 로또번호_Bonus = random.randint(1, 45)
# 당첨번호 = [로또번호_1, 로또번호_2, 로또번호_3, 로또번호_4, 로또번호_5, 로또번호_6, 로또번호_Bonus]
# print(f'금주의 로또번호는{당첨번호} 입니다! 축하드립니다!')

# 번호가 중복이 안되게 하려면...? if문?





num = int(input('임의의 수를 입력하세요'))
숫자1만들기 = list()


# 우엑 똥코드...
while num != 1:
    if num % 2 == 0:
        숫자1만들기.append(num / 2)
        continue
    elif num % 2 != 0:
        숫자1만들기.append(num * 2 + 1)
    else :
        break
else :
    print(f'당신이 선택한 숫자가 {숫자1만들기} 의 과정을 통해 "1"이 되었습니다.')
    # dkdkdkdkdk