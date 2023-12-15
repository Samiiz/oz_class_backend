# if True and 1:
#     print(True)


# if True and "수강생":
#     print(True)


# if True and None:
#     print(True)


# if True and ["양파", "옥수수", "배추"]:
#     print(True)

# if not ' ':
#     print(True)
# else:
#     print(False)

# x = 5

# if x % 2 ==0:
#     print("짝수")
# else:
#     print("홀수")

#     if 15 >= x and  x >3
# for i in range(5, 16):
#     print(i)

# count = int(input())

# # for i in range(count):
# #     print('i의 값은', end=' ')
# #     print(i)
# for i in reversed("python"):
#     print(i, end='.')

오피스텔 = [[201, 202], [301, 302], [401, 402]]

# for 층 in 오피스텔:
#     for 호수 in 층:
#         print(f"{호수}호")
#     print("----")

ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]

for 주식 in ohlc[1:]:
    if 주식[3] > 150:
        print("종가", 주식[3])

i = 0

i = 0

while i >=0:
    i += 23
    if i > 100:
        print(i)
        break