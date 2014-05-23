export LC_ALL=C
################### sampling ###########################
cat Hierarchy_d2D_100000.txt | python src/estimate_mapper.py | python src/estimate_reducer.py > partition_lst

################## materialize #############################
cat Hierarchy_d2D_100000.txt | src/materialize_mapper.py | sort -t $'\t' -k3,4 > td_mapped
cat td_mapped | src/materialize_reducer.py | sort -t $'\t' -k1,1 > td_reduced

################### water batch ########################
#cat Hierarchy_d2D_10000.txt | ./mapper.py | sort -t $'\t' -k1,1 -k2,2 > batch_mapped
#cat batch_map | ./reducer.py | sort -t $'\t' -k1,1 > batch_reduced

################### post processing #####################
cat td_reduced | src/post_mapper.py | sort -t $'\t' -k1,1 | src/post_reducer.py | sort -t $'\t' -k1,1 > tscube

################### naive #######################
cat Hierarchy_d2D_100000.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive

################### accounting #################
cat td_mapped | src/stats.py > accounting

################## checking correctness ##############
diff naive tscube > result
#diff naive td > result
