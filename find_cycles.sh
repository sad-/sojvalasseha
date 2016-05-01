DIR=$1
rm commands
touch commands
#OLD_DIR=$(pwd);
#cd $DIR
(for i in $(ls $DIR); 
do echo "python2.7 parse_inputs.py $DIR/${i}" >> commands; done)
#cd $OLD_DIR
perl submitter.pl commands
