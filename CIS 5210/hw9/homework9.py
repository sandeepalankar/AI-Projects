import homework9_data as data
############################################################
# CIS 521: Homework 9
############################################################

student_name = "Sandeep Alankar"

############################################################
# Section 1: Perceptrons
############################################################


def sign(x):
    return True if x > 0 else False


def dot(w, x):
    return sum(w.get(i, 0) * j for i, j in x.items())


class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.w = {}
        for i in range(iterations):
            for xi, yi in examples:
                y_ = sign(dot(self.w, xi))
                if y_ != yi:
                    update = 1 if yi else -1
                    self.w.update((xi, self.w.get(xi, 0) + update * vi
                                   ) for xi, vi in xi.items())

    def predict(self, x):
        return sign(dot(self.w, x))


class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.y = {label for (_, label) in examples}
        self.w = {y: {} for y in self.y}
        for i in range(iterations):
            for x, y in examples:
                y_ = max(self.y, key=lambda y_: dot(self.w[y_], x))
                if y_ != y:
                    if isinstance(x, dict):
                        for xi, vi in x.items():
                            self.w[y][xi] = self.w[y].get(xi, 0) + vi
                            self.w[y_][xi] = self.w[y_].get(xi, 0) - vi
                    elif isinstance(x, str):
                        self.w[y][x] = self.w[y].get(x, 0)
                        self.w[y_][x] = self.w[y_].get(x, 0)

    def predict(self, x):
        return max(self.y, key=lambda y: dot(self.w[y], x))

############################################################
# Section 2: Applications
############################################################


def read_data(data):
    return [({i: x for i, x in enumerate(d[0])}, d[1]) for d in data]


def format(instance):
    return {i: x for i, x in enumerate(instance)}


class IrisClassifier(object):

    def __init__(self, data):
        self.ex = read_data(data)
        self.iris = MulticlassPerceptron(self.ex, 5)

    def classify(self, instance):
        return self.iris.predict(format(instance))


class DigitClassifier(object):

    def __init__(self, data):
        self.ex = read_data(data)
        self.digit = MulticlassPerceptron(self.ex, 10)

    def classify(self, instance):
        return self.digit.predict(format(instance))


class BiasClassifier(object):

    def __init__(self, data):
        self.bias = BinaryPerceptron([({1: x, 2: 1}, y) for x, y in data], 10)

    def classify(self, instance):
        return self.bias.predict({1: instance, 2: 1})


class MysteryClassifier1(object):

    def __init__(self, data):
        self.mystery = BinaryPerceptron([({1: x[0]**2 + x[1]**2, 2: 1}, y
                                          ) for x, y in data], 10)

    def classify(self, instance):
        return self.mystery.predict({1: instance[0]**2 + instance[1]**2, 2: 1})


class MysteryClassifier2(object):

    def __init__(self, data):
        self.mystery = BinaryPerceptron([({1: x[0] * x[1] * x[2]}, y
                                          ) for x, y in data], 10)

    def classify(self, instance):
        return self.mystery.predict({1: instance[0] * instance[1] * instance[2]
                                     })

############################################################
# Section 3: Feedback
############################################################


feedback_question_1 = 5

feedback_question_2 = """
I found the mystery classifiers to be challenging yet interesting to complete.
"""

feedback_question_3 = """
I liked the application section of the assignment because it allowed me to see
how the classifiers I wrote for the first section could be used in different
scenarios.
"""
