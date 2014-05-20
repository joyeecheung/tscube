#cat Hierarchy_d2D_10000.txt | python sample_mapper.py | python sample_reducer.py > partition_lst
cat Hierarchy_d2D_100.txt | python sample_mapper.py | python sample_reducer.py > partition_lst
cat Hierarchy_d2D_100.txt | ./topdown_mapper.py | sort -t $'\t' -k1,1 -k2,2 > td_map
#cat batch_map | ./reducer.py | sort -t $'\t' -k1,1 > batch
cat td_map | ./topdown_reducer.py | sort -t $'\t' -k1,1 > td
#cat batch | ./post_mapper.py | sort -t $'\t' -k1,1 | ./post_reducer.py | sort -t $'\t' -k1,1 > tscube
#cat Hierarchy_d2D_10000.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 > naive_mapped
cat Hierarchy_d2D_100.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 > naive_mapped
#cat naive_mapped | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive
cat naive_mapped | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive
#diff naive tscube > result
diff naive td > result
