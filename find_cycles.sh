touch commands
(for i in `seq 1 492`; 
do echo "python parse_inputs phase1_processed/${i}.in" >> commands; done)
perl submitter.pl commands
