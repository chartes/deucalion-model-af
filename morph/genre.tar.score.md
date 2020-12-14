
## GENRE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9608   | 0.9276    | 0.8738 | 28824   |
| known-tokens     | 0.9671   | 0.9332    | 0.8815 | 27536   |
| unknown-tokens   | 0.8245   | 0.6139    | 0.6159 | 1288    |
| ambiguous-tokens | 0.9428   | 0.9156    | 0.863  | 13608   |


### GENRE Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| GENRE=f     | 0.94      | 0.92   | 0.93     | 3696    |
| GENRE=m     | 0.94      | 0.96   | 0.95     | 9413    |
| GENRE=n     | 0.85      | 0.64   | 0.73     | 464     |
| GENRE=x     | 0.98      | 0.98   | 0.98     | 15251   |
| avg / total | 0.93      | 0.87   | 0.90     | 28824   |

### GENRE Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| GENRE=m  | 372          | GENRE=x     | 201             |
|          |              | GENRE=f     | 140             |
|          |              | GENRE=n     | 31              |
| GENRE=f  | 314          | GENRE=m     | 245             |
|          |              | GENRE=x     | 62              |
|          |              | GENRE=n     | 7               |
| GENRE=x  | 277          | GENRE=m     | 187             |
|          |              | GENRE=f     | 76              |
|          |              | GENRE=n     | 14              |
| GENRE=n  | 168          | GENRE=m     | 111             |
|          |              | GENRE=x     | 43              |
|          |              | GENRE=f     | 14              |
