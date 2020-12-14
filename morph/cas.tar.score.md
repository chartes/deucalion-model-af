
## CAS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9457   | 0.9057    | 0.9052 | 28824   |
| known-tokens     | 0.9514   | 0.9105    | 0.9106 | 27536   |
| unknown-tokens   | 0.8238   | 0.6096    | 0.605  | 1288    |
| ambiguous-tokens | 0.9301   | 0.9036    | 0.9054 | 16647   |


### CAS Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| CAS=i       | 0.82      | 0.83   | 0.83     | 588     |
| CAS=n       | 0.90      | 0.88   | 0.89     | 4693    |
| CAS=r       | 0.92      | 0.92   | 0.92     | 8310    |
| CAS=x       | 0.98      | 0.98   | 0.98     | 15233   |
| avg / total | 0.91      | 0.91   | 0.91     | 28824   |

### CAS Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| CAS=r    | 673          | CAS=n       | 364             |
|          |              | CAS=x       | 236             |
|          |              | CAS=i       | 73              |
| CAS=n    | 540          | CAS=r       | 443             |
|          |              | CAS=x       | 84              |
|          |              | CAS=i       | 13              |
| CAS=x    | 254          | CAS=r       | 175             |
|          |              | CAS=n       | 60              |
|          |              | CAS=i       | 19              |
| CAS=i    | 98           | CAS=r       | 71              |
|          |              | CAS=n       | 21              |
|          |              | CAS=x       | 6               |
