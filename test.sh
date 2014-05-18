cat Hierarchy_d2D_100.txt | ./mapper.py | sort -k1,1 | ./reducer.py | sort -k1,1 > batch
cat batch | ./post_mapper.py | sort -t $'\t' -k1,1 > mapped
#cat mapped | ./post_reducer.py | sort -k1,1 > tscube
cat mapped | ./post_reducer.py | sort -t $'\t' -k1,1 > tscube
cat Hierarchy_d2D_100.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 > naive_mapped
cat naive_mapped | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive
diff naive tscube > result
