#!/usr/bin/env bash

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D mapred.reduce.tasks=1 \
-D mapred.job.name='TSCube Estimate' \
-file src/estimate_mapper.py    -mapper src/estimate_mapper.py \
-file src/estimate_reducer.py   -reducer src/estimate_reducer.py \
-input $1 -output estimate_out

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=4 \
-D num.key.fields.for.partition=1 \
-D mapred.text.key.comparator.options=-k3,4 \
-D mapred.reduce.tasks=3 \
-D mapred.map.tasks=3 \
-D mapred.job.name='TSCube Materialize' \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file src/materialize_mapper.py    -mapper src/materialize_mapper.py \
-file src/materialize_reducer.py   -reducer src/materialize_reducer.py \
-cacheFile 'estimate_out/part-00000#partition_lst' \
-input $1 -output materialize_out

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D mapred.job.name='TSCube Post Processing' \
-file src/post_mapper.py -mapper src/post_mapper.py \
-file src/post_reducer.py   -reducer src/post_reducer.py \
-input materialize_out/part-* -output $2
