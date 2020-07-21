# Files: 
# Author：jiang liu
# Date ：2020/3/25 13:57
# Tool ：PyCharm


class Person:

    def work(self):
        print('努力上班！')


def play_game(s):
    print("{0}在玩游戏".format(s))


def work2(s):
    print('升官发财，名利双收')


Person.play = play_game
Person.work = work2

p = Person()
p.work()
p.play()  # Person.play(p)
