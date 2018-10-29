Deucalion Model Ancien Français ENC
===================================

To run, you'll need to install Docker. Then, you can simply run the following commands :


```shell
docker build -t deucalion-af:latest .
docker run -p 5001:5000 deucalion-af:latest
```

You can replace 5001 with any port you want to run the service on.

Then, simply go to http://127.0.0.1:5001/?data=SOIGNORS,or%20escoutez,que%20D%C3%A9s%20vos%20soit%20amis,.III%20.vers%20de%20bone%20estoire,se%20je%20les%20vos%20devis or post any data to the same URI with `data` parameters containing your plain text.