# OptimizationTool
Python library for models optimization and features selection
***
optimization_tool.py:
* -d -> dataset path (csv file)
* -vs -> validation size (float)
* -lo -> percentile low value (float) 
* -hi -> percentile high value (float) 
* -s -> percentile step value (float) 
* -pd -> project directory path (string) 
* -pn -> project name (string) 
* -m -> model name (string)
* -i -> cross validation interations (int) 
* -r -> retest (boolean) 
* -c -> configuration file path (json file) 
* -ps -> parameters space file path (json file)
***
The row of the dataset must have the following structure: char1, char2,.......,charN, label, subject_index.
'subject_index' is an integer index that associates the data to the subject/experiment that produced it.

you can choose between the following models: SVM_linear_svc, SVM_poly_svc, SVM_rbf_svc, SVM_linear_svc_2, 
DECISION_TREE, RANDOM_FOREST, KNN, MLP.

In the 'optimization_space.json' file you can configure the configuration space to search for optimized models.

In the 'config.json' file you can configure class labels, features labels and subjects_test_index.
