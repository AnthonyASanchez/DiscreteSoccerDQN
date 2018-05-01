from game_env import gameEnv
from PIL import Image


def main():
    env = gameEnv(200,3)
    env.drawGridState()
    env.canvas.show()
    while env.game_over != True:
        env.playerTurn()
        env.enemyTurn()
        reward = env.getReward()
        env.drawGridState()
        env.canvas.show()
        print(reward)






if __name__ == "__main__":
    main()