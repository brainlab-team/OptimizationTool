import matplotlib.pyplot as plt
from functions import *
from predictive_models import *

print(f"extracting dataset...")
dataset = get_dataset_from_csv("dataset_norm/dataset_norm_clean.csv", [], 0.0)

value = 100
function = sklearn.feature_selection.f_classif
print(f"selecting with percentile = {value}")
selected_features = features_selection_from_score_function(dataset['Xtrain'], dataset['ytrain'], dataset['Xval'],
                                                           dataset['Xtest'], percentile=value,
                                                           function=function,
                                                           type='percentile')

features_names = selected_features['selected_features_names']
scores = selected_features['scores']

for band in ('d', 't', 'a', 'b', 'g'):
    for stat in ('m'):
        new_features_names = []
        new_scores = []
        for i in range(len(features_names) - 8):
            if (features_names[i].split("_")[1] == band and features_names[i].split("_")[2] == stat):
                new_features_names.append(features_names[i].replace(f"_{stat}","").replace(f"_{band}", ""))
                new_scores.append(scores[i])
        #for i in range(len(features_names)-8, len(features_names)):
        #    new_features_names.append(features_names[i])
        #    new_scores.append(scores[i]/max(scores) * 100)



        #for i in range(len(new_scores)):
        #    new_scores[i] = round(new_scores[i], 1)

        plt.figure(figsize=(9,3))
        plt.bar(height=new_scores, x=new_features_names)
        plt.ylim((0,11000))
        plt.title("features scores")
        plt.savefig(f"features_selection_and_optimization/features_scores_{band}_{stat}.png")

new_features_names = []
new_scores = []
for i in range(len(features_names)-8, len(features_names)):
    new_features_names.append(features_names[i])
    new_scores.append(scores[i])

    plt.figure(figsize=(5.14, 3))
    plt.bar(height=new_scores, x=new_features_names)
    plt.ylim((0, 11000))
    plt.title("features scores")
    plt.savefig(f"features_selection_and_optimization/features_scores_valence_and_arousal.png")