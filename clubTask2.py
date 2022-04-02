# 2번 문제입니다.

str = input()

strCount = len(str) - 1
strCountHalf = int(len(str)/2)
loopCount = 0
trueFalse = 1

while(strCountHalf > 0):
    if(str[loopCount] != str[strCount]):
        trueFalse = 0
        break
    loopCount += 1
    strCount -= 1
    strCountHalf -= 1

print(trueFalse)