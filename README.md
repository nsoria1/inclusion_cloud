# inclusion_cloud

# Modules selected
Per the exercise requirements, module 1 and module 2 were selected to resolve.

# Requirements
In order to run this code, you should have installed Docker in your computer.

# Code structure
A high level description of the code will be:
 - pipeline.py: being entry point to the solution, it will iterate the unprocessed folder and get the files that needs to be processed.
 - file_check.py: module created to validate the file constraints based on the requirement doc.
 - data_quality.py: module created to validate the quality of the rows that are being processed.

# How to run the application
Place any files that needs to be processed in unprocessed folder.

```bash
docker build -t test .
docker run -it -v $(pwd):/app test
```

# Improvements
 - Need add unit test for each class and function
 - Need to document class and function usage
 - It is probably possible to do the cleaning and spliting files with less resources
 - `pipeline.py` could be more abstract in its implementation