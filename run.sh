#hadoop fs -rmr sampleout batchout
#hadoop fs -rm partition_lst

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D mapred.reduce.tasks=1 \
-file sample_mapper.py    -mapper sample_mapper.py \
-file sample_reducer.py   -reducer sample_reducer.py \
-input Hierarchy_d2D_10000.txt -output sampleout

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=4 \
-D num.key.fields.for.partition=1 \
-D mapred.text.key.comparator.options=-k3,4 \
-D mapred.reduce.tasks=4 \
-D mapred.map.tasks=4 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file topdown_mapper.py    -mapper topdown_mapper.py \
-file topdown_reducer.py   -reducer topdown_reducer.py \
-cacheFile 'sampleout/part-00000#partition_lst' \
-input Hierarchy_d2D_10000.txt -output batchout

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-file post_mapper.py -mapper post_mapper.py \
-file post_reducer.py   -reducer post_reducer.py \
-input batchout/part-* -output final
