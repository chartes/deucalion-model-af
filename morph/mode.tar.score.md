
## MODE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9897   | 0.9086    | 0.8815 | 28824   |
| known-tokens     | 0.9932   | 0.9284    | 0.9066 | 27536   |
| unknown-tokens   | 0.9146   | 0.7783    | 0.7381 | 1288    |
| ambiguous-tokens | 0.9722   | 0.8739    | 0.9003 | 4603    |


### MODE Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| MODE=con    | 0.89      | 0.92   | 0.90     | 61      |
| MODE=imp    | 0.82      | 0.70   | 0.75     | 120     |
| MODE=ind    | 0.96      | 0.96   | 0.96     | 3320    |
| MODE=sub    | 0.88      | 0.83   | 0.86     | 313     |
| MODE=x      | 1.00      | 1.00   | 1.00     | 25010   |
| avg / total | 0.91      | 0.88   | 0.89     | 28824   |

### MODE Confusion Matrix

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| MODE=ind | 127          | MODE=x      | 78              |
|          |              | MODE=sub    | 29              |
|          |              | MODE=imp    | 13              |
|          |              | MODE=con    | 7               |
| MODE=x   | 77           | MODE=ind    | 71              |
|          |              | MODE=imp    | 4               |
|          |              | MODE=sub    | 2               |
| MODE=sub | 53           | MODE=ind    | 42              |
|          |              | MODE=x      | 9               |
|          |              | MODE=imp    | 2               |
| MODE=imp | 36           | MODE=ind    | 21              |
|          |              | MODE=x      | 12              |
|          |              | MODE=sub    | 3               |
| MODE=con | 5            | MODE=ind    | 5               |
