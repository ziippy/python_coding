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
    generated_numbers_history = []
    duplicated_list = []
    trials = 0

    print("기존에 생성된 번호와 중복되는 번호가 나올 때까지 시뮬레이션합니다.\n")

    while True:
        trials += 1
        new_lotto = generate_lotto_numbers()

        # 새로 생성된 번호가 이전에 생성된 적이 있는지 확인
        if new_lotto in generated_numbers_history:
            print(f"축하합니다! {trials}번째 시도에서 이전에 생성했던 번호와 일치하는 번호가 나왔습니다.")
            print(f"중복된 번호: {new_lotto}")
            print(f"총 시도 횟수: {trials}회")

            duplicated_list.append(new_lotto)
            if len(duplicated_list) >= 5:
                print("중복된 번호가 5개 이상 생성되었습니다. 프로그램을 종료합니다.")
                print("중복된 번호 목록:", duplicated_list)
                break
        else:
            # 중복되지 않으면 리스트에 추가
            generated_numbers_history.append(new_lotto)

        # 진행 상황을 출력하여 사용자가 멈추지 않았다는 것을 알 수 있게 합니다.
        if trials % 10000 == 0:
            print(f"{trials}번 시도 중... (현재까지 중복 없음)")