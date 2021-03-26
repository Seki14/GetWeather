while true;
do 
date
ps -aux | awk '{ printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11);}' > ps_record_`date +%Y%m%d_%H%M%S`.csv;
sleep 3600;
done; 