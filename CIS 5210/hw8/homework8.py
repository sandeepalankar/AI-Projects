import re
import random
############################################################
# CIS 521: Homework 8
############################################################

student_name = "Sandeep Alankar"

############################################################
# Section 1: Ngram Models
############################################################


def tokenize(text):
    return re.findall(r"[\w]+|[^\s\w]", text)


def ngrams(n, tokens):
    ngrams = []
    tokens = ["<START>"] * (n - 1) + tokens + ["<END>"]
    for i in range(n - 1, len(tokens)):
        ngram = tuple(tokens[i - n + 1:i])
        next_token = tokens[i]
        ngrams.append((ngram, next_token))
    return ngrams


class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.grams = []
        self.tokens = set()

    def update(self, sentence):
        tokens = tokenize(sentence)
        # self.grams += ngrams(self.n, tokens)
        self.tokens.update(tokens)
        for i in ngrams(self.n, tokenize(sentence)):
            self.grams.append(i)

    def prob(self, context, token):
        context_count = 0
        match_count = 0

        for i, gram in enumerate(self.grams):
            if gram[0] == context:
                context_count += 1
                if gram[1] == str(token):
                    match_count += 1

        if context_count == 0:
            return 0.0
        else:
            return match_count / context_count

    def random_token(self, context):
        tokens = [gram[1] for gram in self.grams if gram[0] == context]
        tokens.sort()
        random_value = random.random()

        if tokens:
            index = min(int(random_value * len(tokens)),
                        len(tokens) - 1)
            return tokens[index]
        else:
            return " "

    def random_text(self, token_count):
        context = ["<START>" for _ in range(self.n - 1)]
        tokens = []

        for _ in range(token_count):
            current_token = self.random_token(tuple(context))
            tokens.append(current_token)

            if current_token == "<END>":
                context = ["<START>" for _ in range(self.n - 1)]
            elif self.n > 1:
                context = context[1:] + [current_token]

        return " ".join(tokens)

    def perplexity(self, sentence):
        n_grams = ngrams(self.n, tokenize(sentence))
        prod = 1
        for context, token in n_grams:
            p = self.prob(context, token)
            prod *= p
        return prod ** (-1./len(n_grams))


def create_ngram_model(n, path):
    model = NgramModel(n)
    for line in open(path):
        model.update(line)
    return model

############################################################
# Section 2: Feedback
############################################################


feedback_question_1 = 10

feedback_question_2 = """
The random_text and random_token functions were challenging.
"""

feedback_question_3 = """
I liked the difficulty and length of the assignment.
"""
