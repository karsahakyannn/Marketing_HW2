A/B testing

This project involves designing an experiment using Epsilon Greedy and Thompson Sampling algorithms for four different advertisements (bandits).

Result

Average Reward for EpsilonGreedy: 3.9949 Average Regret for EpsilonGreedy: 0.0051 Average Reward for ThompsonSampling: 1.0037 Average Regret for ThompsonSampling: 2.9963

Analysis

Epsilon Greedy seems to perform very well in this scenario. The average reward is close to the highest possible reward of 4, indicating that the algorithm is effectively exploiting the bandits with high rewards. The regret is also extremely low, which means it is making very few suboptimal choices.

Thompson Sampling appears to have a significantly lower average reward compared to Epsilon Greedy. Additionally, the regret is quite high, indicating that it's making more suboptimal choices. This might suggest that the precision chosen for Thompson Sampling may not be well-suited for this particular scenario. However, the values are subject to change, so by adjusting the chosen values we could get better results.
