# Include your imports here, if any are used.

student_name = "Sandeep Alankar"


# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.game = game
        self.discount = discount
        self.values = {}
        self.values = {state: 0 for state in game.states}

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        return self.values.get(state, 0)

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        q_value = 0
        transitions = self.game.get_transitions(state, action)
        for new_state in transitions:
            reward = self.game.get_reward(state, action, new_state)
            if new_state in self.game.states:
                q_value += transitions[new_state] * (reward + self.discount *
                                                     self.get_value(new_state))
            else:
                q_value += transitions[new_state] * (reward)
        return q_value

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        best_policy = None
        best_q = float('-inf')

        for action in self.game.get_actions(state):
            q = self.get_q_value(state, action)
            if q > best_q:
                best_policy = action
                best_q = q
        return best_policy

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        for state in self.values:
            best_policy = self.get_best_policy(state)
            q = self.get_q_value(state, best_policy)
            self.values[state] = q


# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function
    or override ValueIterationAgent's methods, you can add them as well.
    """

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until |V_{k+1}(s) -
        V_k(s)| < ε
        """
        epsilon = 1e-6
        policy = {}
        policy = {state: self.get_best_policy(state) for state in self.values}
        next_policy = {}

        while True:
            for state in self.values:
                q = self.get_q_value(state, policy[state])
                if abs(q - self.get_value(state)) > epsilon:
                    self.values[state] = q

            for state in self.values:
                next_policy[state] = self.get_best_policy(state)

            if policy == next_policy:
                break
            else:
                policy = next_policy


# 3. Bridge Crossing Analysis
def question_3():
    discount = 0.9
    noise = 0.01
    return discount, noise


# 4. Policies
def question_4a():
    discount = 0.3
    noise = 0.0
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = 0.5
    noise = 0.4
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = 0.9
    noise = 0.0
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = 0.9
    noise = 0.1
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = 0.9
    noise = 0.2
    living_reward = 20
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


# 5. Feedback
# Just an approximation is fine.
feedback_question_1 = 5

feedback_question_2 = """
I found this assignment to be quite straightforward.
"""

feedback_question_3 = """
I liked the GUI, it made it very easy to test and visualize my progress.
"""
