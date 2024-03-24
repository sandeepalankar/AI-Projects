import numpy as np
import nltk
from nltk.corpus import stopwords
############################################################
# CIS 521: Homework 1
############################################################

student_name = "Sandeep Alankar"

# This is where your grade report will be sent.
student_email = "salankar@seas.upenn.edu"

#######################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """Strongly typed means that every variable has a
                                fixed type and is checked at runtime. For
                                example, you can't add together a float and a
                                string, you would need to convert one of them
                                to the same type as the other.
                                Dynamically typed means that you don't need to
                                declare a variable's type when you initialize
                                it. The variable's type is determined at
                                runtime based on whatever type that variable
                                holds. For example, if you initialize a
                                variable num = 5, but then declare, in the
                                next line, num = "name", then the value of num
                                at runtime would be a string."""

python_concepts_question_2 = """The type error comes from the fact that you
                                are trying to use a list for the dictionary
                                keys. Dictionary key types must be immutable,
                                or not able to be changed. Lists are mutable
                                objects, so they cannot be used as dictionary
                                keys. However, you could use tuples for the
                                keys instead, as they are immutable."""

python_concepts_question_3 = """The function concatenate2 will be much faster
                                than concatenate1 for larger inputs. This is
                                because in the first function, when you want
                                to concatenate a new string to 'result', it
                                copies the whole previous 'result' string first
                                into a new object and then adds the new
                                character(s) to the end."""

############################################################
# Section 2: Working with Lists
############################################################


def extract_and_apply(lst, p, f):
    return [f(x) for x in lst if p(x)]


def concatenate(seqs):
    return [j for i in seqs for j in i]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

############################################################
# Section 3: Sequence Slicing
############################################################


def copy(seq):
    return seq[:]


def all_but_last(seq):
    return seq[:-1]


def every_other(seq):
    return seq[0::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################


def prefixes(seq):
    yield from (seq[:i] for i in range(len(seq) + 1))


def suffixes(seq):
    yield from (seq[i:] for i in range(len(seq) + 1))


def slices(seq):
    yield from (seq[i:j] for i in range(len(seq) + 1) for j in
                range(i + 1, len(seq) + 1))

############################################################
# Section 5: Text Processing
############################################################


def normalize(text):
    words = text.lower().split()
    return ' '.join(words)


def no_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(letter for letter in text if letter not in vowels)


def digits_to_words(text):
    num = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
           '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    digit = [letter for letter in text if letter.isdigit()]
    spell = [num[index] for index in digit]
    return ' '.join(spell)


def to_mixed_case(name):
    upper = name.strip('_').split('_')
    return upper[0].lower() + ''.join(word.title() for word in upper[1:])

############################################################
# Section 6: Polynomials
############################################################


class Polynomial(object):

    def __init__(self, polynomial):
        self.poly = tuple(polynomial)

    def get_polynomial(self):
        return self.poly

    def __neg__(self):
        neg_poly = [(-coeff, exp) for coeff, exp in self.poly]
        return Polynomial(neg_poly)

    def __add__(self, other):
        return Polynomial(list(self.poly) + list(other.poly))

    def __sub__(self, other):
        return Polynomial(list(self.poly) + [(-coeff, exp) for coeff, exp
                          in list(other.poly)])

    def __mul__(self, other):
        return Polynomial([(coeff1 * coeff2, exp1 + exp2) for coeff1,
                          exp1 in self.poly for coeff2, exp2 in other.poly])

    def __call__(self, x):
        return sum(coeff * (x ** exp) for coeff, exp in self.poly)

    def simplify(self):
        combined = {}
        for (coeff, exp) in self.poly:
            if exp in combined:
                combined[exp] += coeff
            else:
                combined[exp] = coeff
        self.poly = ((coeff, exp) for exp, coeff in combined.items() if
                     coeff != 0)
        self.poly = sorted(list(self.poly), key=lambda x: x[1], reverse=True)

        if not self.poly:
            self.poly = ((0, 0),)

        self.poly = tuple(self.poly)

    def __str__(self):
        result = []
        if not self.poly:
            return ''

        coeff, exp = self.poly[0]
        if coeff >= 0:
            result.append('')
        else:
            result.append('-')
        coeff = abs(coeff)

        if len(self.poly) == 1:
            if exp == 0:
                result.append(str(coeff))
            elif exp == 1 and coeff == 1:
                result.append("x")
            elif exp == 1 and coeff != 1:
                result.append(f"{coeff}x")
            elif coeff == 1 and exp != 1:
                result.append(f"x^{exp}")
            else:
                result.append(f"{coeff}x^{exp}")
        else:
            if exp == 0:
                result.append(str(coeff))
            if coeff == 1 and exp == 1:
                result.append("x")
            elif coeff == 1:
                result.append(f"x^{exp}")
            elif exp == 1:
                result.append(f"{coeff}x")
            else:
                result.append(f"{coeff}x^{exp}")

            for (coeff, exp) in self.poly[1:]:
                if coeff >= 0:
                    sign = " + "
                else:
                    sign = " - "
                coeff = abs(coeff)

                term = str(coeff) if (exp == 0) else (f"{coeff}x"
                                                      if exp == 1 else
                                                      f"{coeff}x^{exp}")

                result.append(sign + term)
        return ''.join(result)

############################################################
# Section 7: Python Packages
############################################################


def sort_array(list_of_matrices):
    arr = np.concatenate([mat.flatten() for mat in list_of_matrices])
    sorted_arr = np.sort(arr)[::-1]
    return sorted_arr


def POS_tag(sentence):
    punkt = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    tokenized_sent = nltk.word_tokenize(sentence.lower())
    stop_words = stopwords.words('english')

    tokenized_without_stopwords = [word for word in tokenized_sent if word not
                                   in stop_words and word not in punkt]
    tagged_sent = nltk.pos_tag(tokenized_without_stopwords)
    return tagged_sent

############################################################
# Section 8: Feedback
############################################################


feedback_question_1 = """
I would estimate this assignment took me approximately 15-20hrs to complete.
"""

feedback_question_2 = """
The most challenging part of the assignment to me was learning how to
effectively use list comprehension and accounting for all the possible
polynomial term coefficients in the __str__ method.
"""

feedback_question_3 = """
I liked how for each sub-problem, there was code output shown so I knew
what my methods were supposed to return, which made my local testing easier.
"""
