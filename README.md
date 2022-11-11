## Homework 5 - writing scripts
Steps to run homework5:  
All scripts should be run from repository root folder  
Set up your path variable as follows:
```
export PATH_TO_LOG_FILE=setup_your_path.log
```
Then run one of these scripts like that

```
./path/script.bash <path_to_log_file>
OR
python3 ./path/script.py <path_to_log_file> --json
--json is optional
```

Copy-paste commands:
```
./task1/count_requests.bash $PATH_TO_LOG_FILE
python3 ./task1/count_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task1/count_requests.py $PATH_TO_LOG_FILE --json

./task2/count_requests_type.bash $PATH_TO_LOG_FILE
python3 ./task2/count_requests_type.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task2/count_requests_type.py $PATH_TO_LOG_FILE --json

./task3/top_frequent_requests.bash $PATH_TO_LOG_FILE
python3 ./task3/top_frequent_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task3/top_frequent_requests.py $PATH_TO_LOG_FILE --json

./task4/top_biggest_requests.bash $PATH_TO_LOG_FILE
python3 ./task4/top_biggest_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task4/top_biggest_requests.py $PATH_TO_LOG_FILE --json

./task5/top_user_requests_failed.bash $PATH_TO_LOG_FILE
python3 ./task5/top_user_requests_failed.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task5/top_user_requests_failed.py $PATH_TO_LOG_FILE --json
```


Contents:
- log requests count (task1)
  - \<number>
- requests type count (task2)
  - \<method> \<count>
- top 10 frequent requests (task3)
  - \<location>
  - \<number count>
- top 5 biggest requests with 4XX error (task4)
  - \<url>
  - \<status code>
  - \<size in bytes>
  - \<ip address>
- top 5 users with requests ended 5XX error (task5)
  - \<ip address>
  - \<requests count>
