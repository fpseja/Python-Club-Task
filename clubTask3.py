# 3번 문제입니다.

schoolCount = int(input("학교를 가는 횟수를 입력하세요 : "))
classMe = input("자신의 분반을 입력하세요 : ")
studentName = []
classNumber = []
relationship = []
valueInsert = ["null" , 0 , 0]
bestFriend = []
loopCount = 0
loopCount2 = 0
loopCount3 = 0

print("친구의 '이름 분반 친밀도'를 입력하세요.\n친밀도는 최대가 100 이며, 그만 입력하려면 '입력종료' 만 입력하세요.")
while True:
    loopbreak = input()
    if(loopbreak == "입력종료"):
        break
    else:
        valueInsert[0], valueInsert[1], valueInsert[2] = loopbreak.split()
        studentName.append(valueInsert[0]), classNumber.append(valueInsert[1]) , relationship.append(int(valueInsert[2]))
    loopCount += 1

while (loopCount != loopCount2):
    relationship[loopCount2] = relationship[loopCount2] + schoolCount
    if(classMe == classNumber[loopCount2]):
        relationship[loopCount2] = relationship[loopCount2] + schoolCount
    loopCount2 += 1

while (loopCount != loopCount3):
    if(relationship[loopCount3] >= 50):
        bestFriend.append(studentName[loopCount3])
    loopCount3 += 1

print("친한 친구들의 이름은", bestFriend ,", 그 수는", len(bestFriend), "명 입니다.")