#!/bin/bash
fname='conceptnet-assertions-5.7.0.csv.gz'
wget https://s3.amazonaws.com/conceptnet/downloads/2019/edges/${fname}
gzip -d $fname
rm $fname
