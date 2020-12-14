
## DEGRE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9842   | 0.8266    | 0.7396 | 28824   |
| known-tokens     | 0.9865   | 0.8475    | 0.7554 | 27536   |
| unknown-tokens   | 0.9356   | 0.5693    | 0.4783 | 1288    |
| ambiguous-tokens | 0.9524   | 0.8443    | 0.7695 | 5863    |


### DEGRE Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| DEGRE=-     | 0.89      | 0.93   | 0.91     | 1580    |
| DEGRE=c     | 0.78      | 0.56   | 0.65     | 52      |
| DEGRE=p     | 0.91      | 0.88   | 0.90     | 968     |
| DEGRE=s     | 0.56      | 0.33   | 0.42     | 30      |
| DEGRE=x     | 0.99      | 0.99   | 0.99     | 26194   |
| avg / total | 0.83      | 0.74   | 0.77     | 28824   |

### DEGRE Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| DEGRE=x  | 192          | DEGRE=-     | 120             |
|          |              | DEGRE=p     | 69              |
|          |              | DEGRE=c     | 2               |
|          |              | DEGRE=s     | 1               |
| DEGRE=p  | 114          | DEGRE=x     | 85              |
|          |              | DEGRE=-     | 28              |
|          |              | DEGRE=s     | 1               |
| DEGRE=-  | 107          | DEGRE=x     | 83              |
|          |              | DEGRE=p     | 13              |
|          |              | DEGRE=c     | 6               |
|          |              | DEGRE=s     | 5               |
| DEGRE=c  | 23           | DEGRE=-     | 16              |
|          |              | DEGRE=x     | 4               |
|          |              | DEGRE=p     | 2               |
|          |              | DEGRE=s     | 1               |
| DEGRE=s  | 20           | DEGRE=-     | 18              |
|          |              | DEGRE=x     | 2               |
