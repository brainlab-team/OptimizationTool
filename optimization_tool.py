#############################################################################################
from predictive_models import *
import argparse
##############################################################################################

# python3 optimization_tool.py -d dataset_norm/dataset.csv -vs 0.0 -lo 5 -hi 15 -s 5 -pd features_selection_and_optimization -pn SVM_linear_svc -m SVM_linear_svc -i 2 -r True -c config.json -ps optimization_space.json
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, required=True,
	help="path to input dataset")
ap.add_argument("-vs", "--validation_size", type=float, required=True,
	help="low percentile value")
ap.add_argument("-lo", "--low", type=float, required=True,
	help="low percentile value")
ap.add_argument("-hi", "--high", type=float, required=True,
	help="high percentile value")
ap.add_argument("-s", "--step", type=float, required=True,
	help="step percentile value")
ap.add_argument("-pd", "--project_directory", type=str, required=True,
	help="path to project directory")
ap.add_argument("-pn", "--project_name", type=str, required=True,
	help="project name")
ap.add_argument("-m", "--model", type=str, required=True,
	help="model type")
ap.add_argument("-i", "--iterations", type=int, required=True,
	help="train and test iterations")
ap.add_argument("-r", "--retest", type=bool, required=True,
	help="retest the models")
ap.add_argument("-c", "--config", type=str, required=True,
	help="path to configuration json file")
ap.add_argument("-ps", "--parameters_space", type=str, required=True,
	help="path to parameters space json file")

args = vars(ap.parse_args())
parameters_file = open(args["parameters_space"], "r")
parameters = json.load(parameters_file)
parameters = parameters[args["model"]]

config_file = open(args["config"], "r")
config = json.load(config_file)
class_labels = config["class_labels"]
test_subjects = config["test_subjects_index"]

try:
    os.mkdir(f"{args['project_directory']}")
except FileExistsError:
    pass
try:
    os.mkdir(f"{args['project_directory']}/all_models")
except FileExistsError:
    pass

##############################################################################################
# select the best models and graph the test accuracy value as the number of characteristics changes

result = features_selection_and_model_optimization(csv_file_path=args["dataset"],
                                                   test_subjects=test_subjects, validation_size=args["validation_size"],
                                                   low_value=args["low"], high_value=args["high"], step=args["step"],
                                                   project_dir=args["project_directory"],
                                                   project_name=args["project_name"], feature_selection_type='from_score_func',
                                                   model_type=args["model"], train_and_test_n_iteration=args["iterations"],
                                                   retest=args["retest"], class_labels=class_labels,parameters=parameters)
