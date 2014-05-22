export LC_ALL=C
cat Hierarchy_d2D_10000.txt | ./topdown_mapper.py | sort -t $'\t' -k3,3 -k4,4 > td_mapped

cat td_mapped | ./topdown_reducer.py | sort -t $'\t' -k1,1 > td_reduced

#cat Hierarchy_d2D_10000.txt | ./mapper.py | sort -t $'\t' -k1,1 -k2,2 | ./reducer.py | sort -t $'\t' -k1,1 > b_reduced

cat Hierarchy_d2D_10000.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive
#diff b_reduced td_reduced > df
diff naive td_reduced > df
