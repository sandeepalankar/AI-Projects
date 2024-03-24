## Simple Baseline

# Description
For our simple basline, we decided to predict the majority class for every input of lyrics. Through our initial data evaluation, we found that out of the 212,667 songs in our train data, approximately 43% of them were Rock, 35% of them were Pop, and the other 8 genres made up the remaining 22%. Therefore, we utilized a simple majority class baseline to serve as a minimal performance expectation to which we can compare our later baselines and model improvements. 

# How to run
The genre predictions can be obtained through a simple function that predicts the majority class (Rock), for every input:

def all_majority(input):
    y_pred = [majority_class] * len(input)
    return y_pred

y_pred = all_majority(trainX)

The evaluate function can then be called on the trainY, valY, and testY data to determine the model's accuracy in predicting the majority class for these three datasets. For example, we can obtain the model's training accuracy by running the following commands:

y_pred = all_majority(trainX)
evaluate(y_pred, trainY, all_genres)

which will output:

(0.428359830157006,
 {'Indie': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Jazz': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Metal': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'R&B': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Hip-Hop': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Pop': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Electronic': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Folk': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Country': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Rock': {'precision': 0.9999890229310969,
   'recall': 1.0,
   'f1_score': 0.4999972557177122}})