from game_env import gameEnv
from PIL import Image
import numpy as np
import os
import tensorflow as tf
from dqn import Qnetwork, processState

def main():
    h_size = 512  # The size of the final convolutional layer before splitting it into Advantage and Value streams.
    path = './dqn'
    tf.reset_default_graph()
    mainQN = Qnetwork(h_size)
    targetQN = Qnetwork(h_size)
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()
    env = gameEnv(84, 3)
    env.canvas.show()
    with tf.Session() as sess:

        print('Loading Model...')
        ckpt = tf.train.get_checkpoint_state(path)
<<<<<<< Updated upstream
        saver.restore(sess, "./dqn\\model-49999.ckpt")
=======
        saver.restore(sess, "./dqndir\\model-47000.ckpt")
>>>>>>> Stashed changes
        s = env.reset()
        s = processState(s)
        while not env.game_over:
            # The Q-Network
            a = sess.run(mainQN.predict, feed_dict={mainQN.scalarInput: [s]})[0]
            s, r, d = env.step(a)
            s = processState(s)
            env.canvas.show()
        '''for i in range(30):
            env.reset()
            print(env.actions)
            while env.game_over != True:
                s1, r, d = env.step()
                env.canvas.show()
                print(r)
                print(d)
'''





if __name__ == "__main__":
    main()