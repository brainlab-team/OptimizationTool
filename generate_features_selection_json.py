from utility.predictive_models import *
import sklearn

print(f"extracting dataset...")
dataset = get_dataset_from_csv("dataset_norm/dataset.csv", [], 0.0)

for function, function_name in zip((sklearn.feature_selection.f_classif,),("f_classif",)):

    selected_features = features_selection_from_score_function(dataset['Xtrain'], dataset['ytrain'], dataset['Xval'],
                                                               dataset['Xtest'], percentile=100,
                                                               function=function,
                                                               type='percentile')

    experiment = dict()
    experiment[function_name] = {'selected_features_names': dict(), 'features_names': list(), 'scores': list(), 'pvalues': list()}

    experiment[function_name]['features_names'] = list(selected_features['selected_features_names'])
    experiment[function_name]['scores'] = list(selected_features['scores'])
    experiment[function_name]['pvalues'] = list(selected_features['pvalues'])

    for value in range(5, 105, 5):

        experiment[function_name]['selected_features_names'][f"best_{value}%"] = list()

        print(f"selecting with percentile = {value}")
        selected_features = features_selection_from_score_function(dataset['Xtrain'], dataset['ytrain'], dataset['Xval'],
                                                                   dataset['Xtest'], percentile=value,
                                                                   function=function,
                                                                   type='percentile')

        print(list(selected_features['selected_features_names']))

        experiment[function_name]['selected_features_names'][f"best_{value}%"] = list(selected_features['selected_features_names'])

try:
    os.mkdir("features_selection_and_optimization/all_models")
except FileExistsError:
    pass

with open(f"features_selection_and_optimization/features_selection_output.json", "w") as outfile:
    json.dump(experiment, outfile)


