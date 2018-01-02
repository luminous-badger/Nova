
# Doesn't work with float. Use seq command instead.
xmin=1.6
xmax=1.9
offs=0.01

for i in $( seq $xmin $offs $xmax )
do
	echo $i
	./arg_nov5.py $i
done

