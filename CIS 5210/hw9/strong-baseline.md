## Strong Baseline

# Description
For our strong baseline, we decided to use the base distillBERT model over vanilla BERT due to its smaller size and faster runtime (using Colab GPUs). We converted the genres to numerical labels, employed batch tokenization (batch size of 100) to tokenize the input data, and then conducted the training process over 3 epochs, printing the loss every 5000 batches and adding checkpoints every 5000 steps to save our progress in case of a session crash.

# How to run
Our step-by-step approach is outlined in our Colab notebook and we imported classification_report from sklearn to display the precision, recall, and F1 score for each genre for our datasets; these screenshots are included in the appendix of our report.