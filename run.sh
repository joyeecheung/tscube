#hadoop fs -rmr sampleout batchout
#hadoop fs -rm partition_lst

#hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
#-file sample_mapper.py    -mapper sample_mapper.py \
#-file sample_reducer.py   -reducer sample_reducer.py \
#-input Hierarchy_d2D_10000.txt -output sampleout

#hadoop fs -getmerge sampleout ./partition_lst

#hadoop fs -put partition_lst ./

hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.4.jar \
-D stream.num.map.output.key.fields=2 \
-D num.key.fields.for.partition=2 \
-file mapper.py    -mapper mapper.py \
-file reducer.py   -reducer reducer.py \
-cacheFile 'partition_lst#partition_lst' \
-input Hierarchy_d2D_10000.txt -output batchout
