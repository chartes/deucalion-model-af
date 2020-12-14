
## NOMB

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.966    | 0.9589    | 0.9576 | 28824   |
| known-tokens     | 0.9709   | 0.9635    | 0.9627 | 27536   |
| unknown-tokens   | 0.8626   | 0.8505    | 0.7935 | 1288    |
| ambiguous-tokens | 0.9538   | 0.9473    | 0.9481 | 14032   |


### NOMB Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| NOMB.=p     | 0.93      | 0.93   | 0.93     | 3953    |
| NOMB.=s     | 0.97      | 0.97   | 0.97     | 13452   |
| NOMB.=x     | 0.98      | 0.98   | 0.98     | 11419   |
| avg / total | 0.96      | 0.96   | 0.96     | 28824   |

### NOMB Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| NOMB.=s  | 448          | NOMB.=x     | 233             |
|          |              | NOMB.=p     | 215             |
| NOMB.=p  | 286          | NOMB.=s     | 241             |
|          |              | NOMB.=x     | 45              |
| NOMB.=x  | 245          | NOMB.=s     | 199             |
|          |              | NOMB.=p     | 46              |
