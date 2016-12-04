import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy
import random 

numRuns = 1
n = numTiles * numTilings * 3
numTilings = 4

def learn(alpha=.1/numTilings, epsilon=0, numEpisodes=1000):
    theta1 = -0.001*rand(n)
    theta2 = -0.001*rand(n)
    returnSum = 0.0

    for episodeNum in range(numEpisodes):
        G = 0
        #...
        #your code goes here (20-30 lines, depending on modularity)
        # ...
        s = mountaincar.init()
        p = s[0]
        v = s[1]
        step = 0
        state = tilecode(p,v)
        terminal = False

        while(not terminal) :

            step += 1

            # this represents the random greedy probability
            i = random.uniform(0,1) 
            # use random policy
            if i < epsilon :
                a = random.randint(0,2)

            else :
                # Greedy policy
                thetaTotal = theta1 + theta2
                a = argmax([qHat(state, 0, thetaTotal), qHat(state, 1, thetaTotal), qHat(state, 2, thetaTotal)])


            # Next state and reward from current state and action   
            R,s = mountaincar.sample(s,a)
            G += R 

            if s:
                nextState = tilecode(s[0], s[1])
            # terminal state
            else :
                nextState = None
            
            #probability of 0.5 for update
            l = random.randint(0,1)
            
            #Double Q learning stuff
            newStateValue = 0

            # update q1
            if l == 0 :
                if nextState:
                    bestActionTheta1 = argmax([qHat(state, 0, theta1), qHat(state, 1, theta1), qHat(state, 2, theta1)])
                    newStateValue = qHat(nextState, bestActionTheta1, theta2) 
                    update = alpha*(R + newStateValue - qHat(state, a, theta1))

                for i in state:
                    theta1[i+a*(9*9*4)] += update 
            # update q2
            elif l == 1 :
                if nextState:
                    bestActionTheta2 = argmax([qHat(state, 0, theta2), qHat(state, 1, theta2), qHat(state, 2, theta2)])
                    newStateValue = qHat(nextState, bestActionTheta2, theta1) 
                    update = alpha*(R + newStateValue - qHat(state, a, theta2))

                for i in state:
                    theta2[i+a*(9*9*4)] += update 

            if not s:
                terminal = True
            else: 
                state = nextState

        print("Episode: ", episodeNum, "Steps:", step, "Return: ", -1*G)
        returnSum = returnSum + G
    print("Average return:", returnSum / numEpisodes)
    return returnSum, theta1, theta2



def qHat(state, action, theta):
    actionValue = 0
    for i in state:
        actionValue += theta[i+action*(9*9*4)]
    return actionValue

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF(theta1, theta2):
    fout = open('value', 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            F = tilecode(-1.2 + i * 1.7 / steps, -0.07 + j * 0.14 / steps)
            height = -max(Qs(F, theta1, theta2))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


if __name__ == '__main__':
    runSum = 0.0
    for run in range(numRuns):
        returnSum, theta1, theta2 = learn()
        runSum += returnSum
    print("Overall performance: Average sum of return per run:", runSum/numRuns)
