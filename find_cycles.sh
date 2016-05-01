rm commands
touch commands
cd phase1-processed
(for i in $(ls); 
do echo "python parse_inputs.py phase1-processed/${i}" >> ../commands; done)
cd ..
perl submitter.pl commands
