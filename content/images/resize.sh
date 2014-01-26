#/bin/bash
for i in `ls *.jpg`
do
echo $i
convert $i -resize 500x $i
done

