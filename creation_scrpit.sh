for day in $(seq -f "%02g" 1 25)
do
	mkdir "day_$day"
	cd ./"day_$day"
	touch input.txt
	touch part_1.py
	touch part_2.py
	cd ..
done