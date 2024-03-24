## Evaluation Script

# Description:
Our evaluation script takes as inputs the predicted labels for each song, the actual labels for each song, and the list of possible genres. We initialize a tracker dictionary to keep track of the true positives, false positives, and false negatives per genre and update the appropriate metric in the dictionary when checking if each predicted label matches the actual label. We also calculate the precicion, recall, and F1 score per genre and store these metric values in the all_stats dictionary. The function returns the model's prediction percent accuracy, the precision, recall and F1 score across all genres, and these same metric values for each genre. 

# How to run:
Given y_pred (which predicts the majority class (Rock) for each instance), trainY (genre labels for each song), and all_genres (set of 10 possible genres), the evaluate function call be called with the following notebook command:

evaluate(y_pred, trainY, all_genres)

which will output:

(0.4285573220104671,
 {'precision': 0.4285573220104671,
  'recall': 0.4285573220104671,
  'f1_score': 0.21427866100523354},
 {'Pop': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Hip-Hop': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Rock': {'precision': 0.4285573220104671,
   'recall': 1.0,
   'f1_score': 0.2999930877168729},
  'Electronic': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Metal': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'R&B': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Country': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Indie': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Folk': {'precision': 0, 'recall': 0.0, 'f1_score': 0},
  'Jazz': {'precision': 0, 'recall': 0.0, 'f1_score': 0}})