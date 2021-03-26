while true;
do 
date
date "+%Y/%m/%d %H:%M:%S" >> ps_record.csv;
ps -aux | awk '{ printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11);}' >> test.csv;
sleep 3600;
done; 