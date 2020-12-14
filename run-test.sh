#!/bin/sh

PIE=~/dev/pie/env/bin/pie
ROOT_CORPORA=../corpora-old-french
#$PIE eval --train_path $ROOT_CORPORA/tagged/no-morph/train.tsv lemma/lemma-pos.tar $ROOT_CORPORA/tagged/no-morph/test.tsv --markdown --report --confusion > lemma-pos.score.md
for file in morph/*.tar
   do $PIE eval $file $ROOT_CORPORA/tagged/morph/test.tsv --train_path $ROOT_CORPORA/tagged/morph/train.tsv --markdown --report --confusion > $file.score.md;
done
