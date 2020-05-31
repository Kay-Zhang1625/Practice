"""
craps賭博遊戲
"""
class Game(object):
    def __int__(self, name, money):
        self.name = name
        self.money = money
        self.debt = debt

    def Debt(self, debt):
        self.debt = debt


    def WinNumber(self, win=0):
        self.win = win


from random import randint

gameNumber = 0
while playerA.money > 0 and playerB.money > 0 and gameNumber < 5:
    needs_go_on = False
    while True:
        while gameNumber > 0:
            print('%s 目前的資產: ' % (playerA.money))
            print('%s 目前的資產: ' % (playerB.money))
            print('已玩 %d 局, %s 贏 %d 局, %s 贏 %d 局' %
                  (gameNumber, playerA.name, winA, playerB.name, winB))
            break
    first = randint(1, 6) + randint(1, 6)
    print('Python搖出: %d 點' % first)
    if first == 7 or first == 11:
        print('這一局 %s 贏了!' % playerA.name)
        playerA.money += playerB.debt
        playerB.money -= playerB.debt
        playerA.win += 1
        gameNumber += 1
    elif first == 2 or first == 3 or first == 12:
        print('這一局 %s 贏了!' % playerB.name)
        playerA.money -= playerA.debt
        playerB.money += playerA.debt
        playerB.win += 1
        gameNumber += 1
    else:
        needs_go_on = True

    while needs_go_on == True:
        current = randint(1, 6) + randint(1, 6)
        print('Python搖出: %d 點' % current)
        if current == first:
            print('這一局 %s 贏了!' % playerA.name)
            playerA.money += playerB.debt
            playerB.money -= playerB.debt
            playerA.win += 1
            gameNumber += 1
            needs_go_on = False
        elif current == 7:
            print('這一局 %s 贏了!' % playerB.name)
            playerA.money -= playerA.debt
            playerB.money += playerA.debt
            playerB.win += 1
            gameNumber += 1
            needs_go_on = False
        else:
            needs_go_on = True

print('遊戲結束!\n總結: %s 贏 %d 局, %s 贏 %d 局'
      % (playerA.name, playerA.win, playerB.name, playerB.win))
if playerA.win > playerB.win:
    print('%s 贏了' % playerA.name)
else:
    print('%s 贏了' % playerB.name)


def main():
    playerA = Game('Kay', 1000, 200)
    playerB = Game('Elain', 1000, 300)


if __name__ == '__main__':
    main()








