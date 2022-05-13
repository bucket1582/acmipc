BEGINNING_DIALOG = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
QUESTION = '"재귀함수가 뭔가요?"'
FIRST_LINE = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
SECOND_LINE = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
THIRD_LINE = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
TAB_PREFIX = "____"
ANSWER_LINE = '"재귀함수는 자기 자신을 호출하는 함수라네"'
ANSWER_PACKAGE = "라고 답변하였지."


def recursive_ars(prefix, n):
    if n == 0:
        print(prefix + QUESTION)
        print(prefix + ANSWER_LINE)
        print(prefix + ANSWER_PACKAGE)
        return
    print(prefix + QUESTION)
    print(prefix + FIRST_LINE)
    print(prefix + SECOND_LINE)
    print(prefix + THIRD_LINE)
    recursive_ars(prefix + TAB_PREFIX, n - 1)
    print(prefix + ANSWER_PACKAGE)

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())
print(BEGINNING_DIALOG)
recursive_ars("", n)
