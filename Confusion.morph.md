Confusion tables
================

- [Cas](#cas)
- [Mode](#mode)
- [Degre](#degre)
- [Genre](#genre)
- [Temps](#temps)
- [Nombre](#nombre)
- [Personne](#personne)


# Cas

```
all
  accuracy: 0.9513
  precision: 0.9255
  recall: 0.9226
  support: 19444
ambiguous-tokens:
  accuracy: 0.9341
  precision: 0.9262
  recall: 0.9228
  support: 10451
unknown-tokens:
  accuracy: 0.8677
  precision: 0.851
  recall: 0.8555
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| r        | 426          | n           | 263             |
|          |              | _           | 110             |
|          |              | i           | 47              |
|          |              | x           | 6               |
| n        | 315          | r           | 273             |
|          |              | _           | 27              |
|          |              | i           | 8               |
|          |              | x           | 7               |
| _        | 127          | r           | 101             |
|          |              | n           | 21              |
|          |              | x           | 4               |
|          |              | i           | 1               |
| i        | 61           | r           | 42              |
|          |              | n           | 16              |
|          |              | _           | 3               |
| x        | 18           | r           | 10              |
|          |              | _           | 5               |
|          |              | n           | 3               |

# Mode

```
all
  accuracy: 0.9897
  precision: 0.8883
  recall: 0.8729
  support: 19444
ambiguous-tokens:
  accuracy: 0.9602
  precision: 0.9089
  recall: 0.9049
  support: 2162
unknown-tokens:
  accuracy: 0.9433
  precision: 0.8045
  recall: 0.7874
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| ind      | 98           | _           | 58              |
|          |              | sub         | 21              |
|          |              | imp         | 13              |
|          |              | con         | 6               |
| _        | 37           | ind         | 31              |
|          |              | imp         | 4               |
|          |              | sub         | 2               |
| sub      | 32           | ind         | 29              |
|          |              | _           | 3               |
| imp      | 31           | ind         | 24              |
|          |              | _           | 6               |
|          |              | sub         | 1               |
| con      | 3            | ind         | 2               |
|          |              | imp         | 1               |

# Degre

```
all
  accuracy: 0.9827
  precision: 0.7972
  recall: 0.7035
  support: 19444
ambiguous-tokens:
  accuracy: 0.9498
  precision: 0.7767
  recall: 0.7121
  support: 4299
unknown-tokens:
  accuracy: 0.9452
  precision: 0.6904
  recall: 0.495
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 110          | -           | 63              |
|          |              | p           | 47              |
| p        | 98           | _           | 76              |
|          |              | -           | 17              |
|          |              | s           | 3               |
|          |              | c           | 2               |
| -        | 88           | _           | 64              |
|          |              | p           | 15              |
|          |              | s           | 5               |
|          |              | c           | 4               |
| s        | 24           | -           | 17              |
|          |              | p           | 5               |
|          |              | c           | 2               |
| c        | 17           | -           | 11              |
|          |              | p           | 4               |
|          |              | _           | 2               |

# Genre

```
all
  accuracy: 0.9632
  precision: 0.9258
  recall: 0.8885
  support: 19444
ambiguous-tokens:
  accuracy: 0.9396
  precision: 0.9177
  recall: 0.8823
  support: 8625
unknown-tokens:
  accuracy: 0.8922
  precision: 0.7056
  recall: 0.7052
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| f        | 246          | m           | 194             |
|          |              | _           | 42              |
|          |              | n           | 5               |
|          |              | x           | 5               |
| m        | 222          | f           | 95              |
|          |              | _           | 89              |
|          |              | n           | 27              |
|          |              | x           | 11              |
| _        | 120          | m           | 76              |
|          |              | f           | 29              |
|          |              | n           | 12              |
|          |              | x           | 3               |
| n        | 110          | m           | 79              |
|          |              | _           | 26              |
|          |              | f           | 5               |
| x        | 18           | m           | 11              |
|          |              | _           | 5               |
|          |              | f           | 2               |

# Temps

```
all
  accuracy: 0.988
  precision: 0.9469
  recall: 0.9492
  support: 19444
ambiguous-tokens:
  accuracy: 0.9601
  precision: 0.9214
  recall: 0.9324
  support: 2404
unknown-tokens:
  accuracy: 0.9348
  precision: 0.8712
  recall: 0.8437
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| pst      | 89           | _           | 61              |
|          |              | psp         | 19              |
|          |              | ipf         | 6               |
|          |              | fut         | 3               |
| _        | 55           | pst         | 41              |
|          |              | psp         | 6               |
|          |              | ipf         | 4               |
|          |              | fut         | 4               |
| psp      | 54           | pst         | 19              |
|          |              | ipf         | 16              |
|          |              | _           | 14              |
|          |              | fut         | 5               |
| ipf      | 28           | pst         | 12              |
|          |              | psp         | 7               |
|          |              | fut         | 5               |
|          |              | _           | 4               |
| fut      | 8            | pst         | 3               |
|          |              | _           | 3               |
|          |              | psp         | 2               |

# Nombre

```
all
  accuracy: 0.9671
  precision: 0.9531
  recall: 0.95
  support: 19444
ambiguous-tokens:
  accuracy: 0.9499
  precision: 0.9457
  recall: 0.945
  support: 8994
unknown-tokens:
  accuracy: 0.9121
  precision: 0.8919
  recall: 0.8666
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| s        | 292          | p           | 173             |
|          |              | _           | 108             |
|          |              | x           | 11              |
| p        | 235          | s           | 210             |
|          |              | _           | 20              |
|          |              | x           | 5               |
| _        | 93           | s           | 77              |
|          |              | p           | 14              |
|          |              | x           | 2               |
| x        | 19           | s           | 14              |
|          |              | _           | 4               |
|          |              | p           | 1               |

# Personne

```
all
  accuracy: 0.9867
  precision: 0.9729
  recall: 0.7736
  support: 19444
ambiguous-tokens:
  accuracy: 0.9714
  precision: 0.9519
  recall: 0.749
  support: 5306
unknown-tokens:
  accuracy: 0.9471
  precision: 0.8999
  recall: 0.8617
  support: 1058

```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| 3        | 86           | _           | 65              |
|          |              | 1           | 19              |
|          |              | 2           | 2               |
| _        | 66           | 3           | 49              |
|          |              | 2           | 12              |
|          |              | 1           | 5               |
| 1        | 48           | 3           | 30              |
|          |              | _           | 10              |
|          |              | 2           | 8               |
| 2        | 38           | 3           | 15              |
|          |              | _           | 13              |
|          |              | 1           | 10              |
| 0        | 21           | 3           | 20              |
|          |              | _           | 1               |
