import random

def generate_lotto_numbers():
    """
    로또 6/45 번호를 생성하는 함수
    """
    # 1부터 45까지의 숫자 리스트를 생성합니다.
    numbers = list(range(1, 46))
    
    # numbers 리스트에서 무작위로 6개의 숫자를 선택합니다.
    # 중복을 허용하지 않는 random.sample() 함수를 사용합니다.
    lotto_numbers = random.sample(numbers, 6)
    
    # 생성된 번호를 오름차순으로 정렬합니다.
    lotto_numbers.sort()
    
    return lotto_numbers

# 함수를 호출하여 로또 번호를 생성하고 출력합니다.
if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("생성된 로또 번호:", lotto_numbers)