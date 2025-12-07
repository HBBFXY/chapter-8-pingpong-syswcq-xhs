from random import random

def get_probability():
    """获取两位选手的发球回合获胜概率"""
    probA = float(input("请输入选手A的发球得分概率(0-1)："))
    probB = float(input("请输入选手B的发球得分概率(0-1)："))
    return probA, probB

def sim_one_game(probA, probB):
    """模拟一局比赛（11分制，10平后赢2分，最高12:10）"""
    scoreA, scoreB = 0, 0
    serve_count = 0  # 发球次数（每2次换发球）
    serving = 'A'    # 初始发球方

    while True:
        serve_count += 1
        # 每2次发球换发球
        if serve_count % 2 == 0:
            serving = 'B' if serving == 'A' else 'A'
        
        # 判定得分
        if serving == 'A':
            scoreA += 1 if random() < probA else 0
        else:
            scoreB += 1 if random() < probB else 0
        
        # 判断比赛结束（11分制+12:10上限）
        max_sc = max(scoreA, scoreB)
        min_sc = min(scoreA, scoreB)
        if (max_sc == 11 and max_sc - min_sc >= 2) or (max_sc == 12 and min_sc == 10):
            break
    return scoreA, scoreB

def sim_multiple_games(probA, probB, game_num):
    """模拟多局比赛，统计胜负规律"""
    A_win = 0
    for _ in range(game_num):
        scA, scB = sim_one_game(probA, probB)
        A_win += 1 if scA > scB else 0
    B_win = game_num - A_win
    print(f"\n共模拟{game_num}局比赛：")
    print(f"选手A获胜{ A_win }局，胜率{ A_win/game_num*100:.2f}%")
    print(f"选手B获胜{ B_win }局，胜率{ B_win/game_num*100:.2f}%")

if __name__ == "__main__":
    probA, probB = get_probability()
    game_count = int(input("请输入模拟比赛的局数："))
    sim_multiple_games(probA, probB, game_count)
