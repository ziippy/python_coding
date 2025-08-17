import random
from tqdm import tqdm

def generate_lotto_numbers():
    """
    로또 6/45 번호를 생성하는 함수 (정렬된 리스트 형태)
    """
    numbers = list(range(1, 46))
    lotto_numbers = random.sample(numbers, 6)
    lotto_numbers.sort()
    return lotto_numbers

if __name__ == "__main__":
    target_numbers = [6, 17, 22, 28, 29, 32]
    trials = 0

    print("기존 당첨번호와 동일한 번호가 나올 때까지 시뮬레이션합니다.\n")

    while True:
        trials += 1
        new_lotto = generate_lotto_numbers()

        # 새로 생성된 번호가 이전에 생성된 적이 있는지 확인
        if new_lotto == target_numbers:
            print(f"축하합니다! {trials}번째 시도에서 일치하는 번호가 나왔습니다.")
            print(f"번호: {new_lotto}")
            break

        # 진행 상황을 출력하여 사용자가 멈추지 않았다는 것을 알 수 있게 합니다.
        if trials % 10000 == 0:
            print(f"{trials}번 시도 중... (현재까지 일치 없음)")