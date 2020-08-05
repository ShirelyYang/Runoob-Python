def get_reward(i):
    i /= 10000
    rewards = 0
    obj = {100: 0.01, 60: 0.015, 40: 0.03, 20: 0.05, 10: 0.075, 0: 0.1}
    keys = list(obj.keys())
    keys.sort()
    keys.reverse()
    for key in keys:
        if i > key:
            rewards += (i - key) * obj.get(key)
            i = key
    return int(rewards * 10000)
if __name__ == "__main__":
    i = int(input("请输入净利润："))
    print("发放的奖金为：", get_reward(i), "元")