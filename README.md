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
where 'subject_index' is an integer index that associates the data to the subject/experiment that produced it.
