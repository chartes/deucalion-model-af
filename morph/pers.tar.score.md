
## PERS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9872   | 0.8732    | 0.7848 | 28824   |
| known-tokens     | 0.9897   | 0.8782    | 0.7906 | 27536   |
| unknown-tokens   | 0.9325   | 0.8832    | 0.8721 | 1288    |
| ambiguous-tokens | 0.9756   | 0.8709    | 0.7839 | 8648    |


### PERS Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| PERS.=0     | 0.50      | 0.07   | 0.12     | 28      |
| PERS.=1     | 0.95      | 0.94   | 0.94     | 916     |
| PERS.=2     | 0.96      | 0.94   | 0.95     | 770     |
| PERS.=3     | 0.97      | 0.98   | 0.97     | 4979    |
| PERS.=x     | 0.99      | 0.99   | 0.99     | 22131   |
| avg / total | 0.87      | 0.78   | 0.80     | 28824   |

### PERS Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| PERS.=x  | 126          | PERS.=3     | 80              |
|          |              | PERS.=1     | 25              |
|          |              | PERS.=2     | 21              |
| PERS.=3  | 119          | PERS.=x     | 96              |
|          |              | PERS.=1     | 14              |
|          |              | PERS.=2     | 7               |
|          |              | PERS.=0     | 2               |
| PERS.=1  | 52           | PERS.=x     | 25              |
|          |              | PERS.=3     | 21              |
|          |              | PERS.=2     | 6               |
| PERS.=2  | 47           | PERS.=x     | 24              |
|          |              | PERS.=3     | 12              |
|          |              | PERS.=1     | 11              |
| PERS.=0  | 26           | PERS.=3     | 26              |
