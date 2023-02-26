Student Answer #1:

A)
Training: Normally the largest set. This is the set the model is trained on to be "fitted" / learn the optimal parameters by some optimization procedure that aims to minimize the error of the model on the training set, or optimize some objective function with respect to the data in the general case.

Validation: This is a held out set, not seen by the model in training. We use this set to optimize hyperparameters. Using techniques like grid or random search, we fit models using different hyperparameter values given to the learning algorithm. We then score the accuracy of each model on the validation set and normally pick the combination of hyperparameters that scored best on the val set.

Test: This is also a held out set, not seen in fitting the model nor optimizing the hyperparameters. We use the test set as the final performance metric / accuracy test of our model, following training and hyperparameter tuning. The idea is that we may have "overfit" our hyperparameters to the validation set, or gotten lucky, hence we use the test set to serve as the ultimate performance test of our model to predict how likely it is to generalize.

B)
An overfit model is effectively a model that has "memorized" the training data it was given, and at some point even learned the noise in the training set. As such, overfit models perform very well on the train set but very poorly on novel data such as the test set (i.e., they have low bias but high variance). The real goal of a model is to fit the distribution of a broader population, to generalize and predict labels for that population. We already know the labels for the training set, but want to use the model to predict labels for novel examples. If the model can't do that with decent accuracy, and overfit models can't, then there's no use to the model - it has no "real" predictive power so it's basically useless. In short, overfit models memorized some values but didn't really learn a general trend that can be applied in the wild so they're of limited practical use.

Student Answer #2:

A) 
A training set is used to learn the model parameters (e.g., weights) through the use of gradient descent. Gradient descent adjusts model parameters such that it minimizes the chosen cost function (e.g., MSE).

A validation set is used to find the best hyperparameter values and learning algorithm (e.g., SVM, ID3, kNN, etc.) by comparing a selected performance metric (e.g., precision, recall, accuracy, etc.) between multiple models that were trained using different sets of hyperparameters. One may use methods such as cross-validation when a validation set is not possible (e.g., there's not enough data).

A testing set is used to assess the predictability (correctness) of a trained model. The testing set should not be used to train (learn parameters) nor to validate (learn hyperparameters and algorithm) the model.

B)
Although an overfitted model will perform well on the training set, it will make many errors when being assessed by the testing set. Overfitting may occur due to high variance between the training set and testing sets. We aim to generalize the training model instead of overfitting so that it is able to better predict future data.
