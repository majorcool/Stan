def input_score():
    Score=float(input())
    str_score=str(Score)
    if len(str_score[str_score.find('.')::])-1>2 or Score>100 or Score<0:
        er=Exception("ScoreError")
        raise er
try:
    for i in range(30):
        input_score()
except ValueError:
    print("输入的不是数字类型")
