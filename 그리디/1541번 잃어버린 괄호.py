# 이것이 합 또는 차 기혼가
def is_pm(char):
    return char in ['+', '-']

sentence=input()
# 형식 맞추기 위한 +
sentence += "+"

# + 끼리 다 더해버리고 마지막에 - 붙는 게 최소
# -가 하나 나오면, 그 이후는 다 음수로 바꿀 수 있음
is_m_presented = False
numeric_combo = ""
least_sum = 0
for char in sentence:
    # 부호 처리
    if is_pm(char):
        # 숫자 파싱
        number = int(numeric_combo)

        # -가 나온 이후
        if is_m_presented:
            number = -number
        
        if char == '-':
            is_m_presented = True

        least_sum += number

        # 숫자 콤보 초기화
        numeric_combo = ""
        continue

    # 숫자 콤보 추가
    numeric_combo += char
print(least_sum)

        
        

    
