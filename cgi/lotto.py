#!/Users/heejin/PycharmProjects/server_basic/venv/bin/python

# 로또 예상 번호 5게임 출력하기

import random

# 로또는 1게임당 1~45 사이의 정수 중 6개를 중복 없이 뽑아야 한다.

# 1. 랜덤하게 숫자 뽑아서 채우기
numbers = []

while len(numbers)<6:
    number = random.randint(1, 45)
    if number not in numbers:
        numbers.append(number)

# 1-1. 리스트 대신 set
numbers = set()
while len(numbers) < 6:
    number = random.randint(1, 45)
    numbers.add(number)

# 2. 원본을 만들어두고 랜덤하게 몇 개 뽑는 방법
original_numbers = [x for x in range(1,46)]

# 1)
random.sample(original_numbers,6)

# 2)
random.shuffle(original_numbers)
numbers = original_numbers[:6]
numbers = original_numbers[-6:]

print('Context-type: text/html\n')
print('<html><head><title>lotto numbers</title></head><body>'+str(numbers)+'</body></html>')

# 랜덤 숫자 뽑는거 -> 랜덤 문자열 -> UUID