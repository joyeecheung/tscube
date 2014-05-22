head Hierarchy_d2D_100.txt | ./topdown_mapper.py | sort -t $'\t' -k3,3 -k4,4 > td_mapped
cat td_mapped | ./topdown_reducer.py | sort -t $'\t' -k1,1 > td_reduced

head Hierarchy_d2D_100.txt | ./mapper.py | sort -t $'\t' -k1,1 -k2,2 | ./reducer.py | sort -t $'\t' -k1,1 > b_reduced

diff b_reduced td_reduced -y > df
