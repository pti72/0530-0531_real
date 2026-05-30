# 리스트 메소드

li1 = [1, 3, 5, 7, 9]
print(li1, type(li1))

# .append(값)
li1.append(10)
print(li1) # li1의 맨끝에 10 추가

# .insert(idx, 값)
li1.insert(1, 2) # 1번 인덱스 자리에 2번 추가
print(li1)

# .extend()
li2 = [50, 60, 70]
li1.extend(li2) # li1에 li2의 요소들 추가
print(li1)

# remove(값)
li1.remove(50) # li1에 있는 50을 삭제
print(li1)

# pop(idx)
li1.pop(0) # li1의 0번 위치의 값 삭제
print(li1)

li1.pop() # li1의 맨끝의 요소 삭제
print(li1)




