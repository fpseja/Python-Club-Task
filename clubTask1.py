# 좋아하시는 프링글스 스윗 마요 프로그램입니다.

hour , minu , seco = input().split()
hour = int(hour)
minu = int(minu)
seco = int(seco)
while True:
    bakeTime = int(input())
    if(0 <= bakeTime <= 500000):
        break
    else:
        print("값이 너무 큽니다, 500000 이하로 입력해주세요.")

allTime = hour*3600 + minu*60 + seco + bakeTime
allTime = allTime % 86400
hour, allTime = int(allTime/3600), int(allTime%3600)
minu, allTime = int(allTime/60), int(allTime%60)
seco = int(allTime)

print(hour, minu, seco)