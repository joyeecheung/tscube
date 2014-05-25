export LC_ALL=C
echo "Generating naive cube..."
cat Hierarchy_d2D_1000000.txt | ../naivecube/mapper.py | sort -t $'\t' -k1,1 | ../naivecube/reducer.py | sort -t $'\t' -k1,1 > naive
echo "Pulling TSCube output..."
rm -f final_out
hadoop fs -getmerge final_out ./final_out
sort -t $'\t' -k1,1 final_out > final
echo "Checking difference..."
diff final naive > check

