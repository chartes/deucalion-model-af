
## TEMPS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9854   | 0.945     | 0.9408 | 28824   |
| known-tokens     | 0.9886   | 0.9584    | 0.9585 | 27536   |
| unknown-tokens   | 0.9169   | 0.8372    | 0.8109 | 1288    |
| ambiguous-tokens | 0.9644   | 0.9331    | 0.9527 | 4638    |


### TEMPS Classification report

| target      | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|---------|
| TEMPS=fut   | 0.90      | 0.93   | 0.92     | 224     |
| TEMPS=ipf   | 0.96      | 0.94   | 0.95     | 687     |
| TEMPS=psp   | 0.94      | 0.94   | 0.94     | 1020    |
| TEMPS=pst   | 0.92      | 0.90   | 0.91     | 1702    |
| TEMPS=x     | 0.99      | 0.99   | 0.99     | 25191   |
| avg / total | 0.94      | 0.94   | 0.94     | 28824   |

### TEMPS Confusion Matrix

| Expected  | Total Errors | Predictions | Predicted times |
|-----------|--------------|-------------|-----------------|
| TEMPS=pst | 174          | TEMPS=x     | 136             |
|           |              | TEMPS=psp   | 27              |
|           |              | TEMPS=ipf   | 6               |
|           |              | TEMPS=fut   | 5               |
| TEMPS=x   | 128          | TEMPS=pst   | 84              |
|           |              | TEMPS=psp   | 29              |
|           |              | TEMPS=fut   | 9               |
|           |              | TEMPS=ipf   | 6               |
| TEMPS=psp | 66           | TEMPS=x     | 26              |
|           |              | TEMPS=pst   | 22              |
|           |              | TEMPS=ipf   | 12              |
|           |              | TEMPS=fut   | 6               |
| TEMPS=ipf | 39           | TEMPS=pst   | 19              |
|           |              | TEMPS=x     | 13              |
|           |              | TEMPS=psp   | 5               |
|           |              | TEMPS=fut   | 2               |
| TEMPS=fut | 15           | TEMPS=x     | 14              |
|           |              | TEMPS=psp   | 1               |
