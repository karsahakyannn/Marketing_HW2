from abc import ABC, abstractmethod
from logs import *
import random
import csv

logging.basicConfig()
logger = logging.getLogger("MAB Application")

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

class Bandit(ABC):
    ##==== DO NOT REMOVE ANYTHING FROM THIS CLASS ====##

    @abstractmethod
    def __init__(self, p):
        self.p = p
        self.rewards = []
        self.regrets = []

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def pull(self):
        pass

    @abstractmethod
    def update(self, arm, reward):
        pass

    def experiment(self, trials):
        for _ in range(trials):
            arm = self.pull()
            reward = Bandit_Reward[arm]
            self.rewards.append(reward)  # Recording the reward
            regret = max(Bandit_Reward) - reward  # Calculating regret
            self.regrets.append(regret)  # Recording regret
            self.update(arm, reward)

    def report(self, algorithm):
        # store data in csv
        with open(f'{algorithm}_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Bandit', 'Reward', 'Algorithm'])
            for i, reward in enumerate(self.rewards):
                writer.writerow([i, reward, algorithm])
        # log average reward and regret
        avg_reward = sum(self.rewards) / len(self.rewards)
        avg_regret = sum(self.regrets) / len(self.regrets)
        logger.info(f'Average Reward for {algorithm}: {avg_reward}')
        logger.info(f'Average Regret for {algorithm}: {avg_regret}')

class Visualization():
    @staticmethod
    def plot1(epsilon_greedy_rewards, thompson_rewards):
        # Visualization code goes here
        pass

    @staticmethod
    def plot2(e_greedy_rewards, thompson_rewards):
        # Visualization code goes here
        pass

class EpsilonGreedy(Bandit):
    def __init__(self, p, initial_epsilon):
        super().__init__(p)
        self.epsilon = initial_epsilon
        self.q_values = [0] * len(p)
        self.action_counts = [0] * len(p)

    def __repr__(self):
        return 'EpsilonGreedy'

    def pull(self):
        if random.random() < self.epsilon:
            return random.randint(0, len(self.p) - 1)
        else:
            return self.q_values.index(max(self.q_values))

    def update(self, arm, reward):
        self.action_counts[arm] += 1
        self.q_values[arm] += (reward - self.q_values[arm]) / self.action_counts[arm]
        self.epsilon = 1 / (sum(self.action_counts) + 1)

class ThompsonSampling(Bandit):
    def __init__(self, p, precision):
        super().__init__(p)
        self.precision = precision
        self.alpha = [1.0] * len(p)
        self.beta = [1.0] * len(p)

    def __repr__(self):
        return 'ThompsonSampling'

    def pull(self):
        samples = [random.betavariate(self.alpha[i], self.beta[i]) for i in range(len(self.p))]
        return samples.index(max(samples))

    def update(self, arm, reward):
        self.alpha[arm] += reward
        self.beta[arm] += (1 - reward)
        if self.alpha[arm] <= 0 or self.beta[arm] <= 0:
            self.alpha[arm] = 1.0
            self.beta[arm] = 1.0
        logger.debug(f'ThompsonSampling - Arm {arm} selected, Reward: {reward}')

def comparison():
    # Implementation of comparison logic goes here
    pass

if __name__=='__main__':
    # Your main code here
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
