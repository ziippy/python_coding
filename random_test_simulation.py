import random
from tqdm import tqdm

# WIN_RATE_1ST = 0.01    # -> 시도 횟수 100.xxx
# WIN_RATE_1ST = 0.001   # -> 시도 횟수 1000.xxx
WIN_RATE_1ST =   0.0001  # -> 시도 횟수 10000.xxx
WIN_RATE_2ND = 0.02
WIN_RATE_CONSOLATION = 0.97

def get_lottery_result():
    rand_num = random.random()
    if rand_num < WIN_RATE_1ST:
        return "1등 당첨!"
    elif rand_num < WIN_RATE_1ST + WIN_RATE_2ND:
        return "2등 당첨!"
    else:
        return "꽝!"

if __name__ == "__main__":
    total_trials = 0
    num_simulations = 100_000

    for _ in tqdm(range(num_simulations)):
        trials = 0
        while True:
            trials += 1
            result = get_lottery_result()
            if result == "1등 당첨!":
                total_trials += trials
                break
    
    average_trials = total_trials / num_simulations
    print(f"{num_simulations}번의 시뮬레이션 평균 1등 당첨 시도 횟수: {average_trials:.2f}번")