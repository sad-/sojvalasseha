if [ "$#" -ne 4 ]; then
	  echo "Usage: spark-launcher-custom [PEM-absolute-path] [PEM-name] [num-slaves] [cluster-name]"
	  exit
fi

PEM=$1
PEM_NAME=$2
NUM_SLAVES=$3
CLUSTER_NAME=$4


cd ~/spark-1.6.1*/ec2/ # CHANGE THIS TO YOUR SPARK DIR / EC2
./spark-ec2 \
	-i $PEM \
	-k $PEM_NAME \
	-r us-west-2 \
	--no-ganglia \
	--delete-groups \
	--hadoop-major-version 2 \
	-s $NUM_SLAVES \
	-t c4.xlarge \
	--spot-price=2 launch $CLUSTER_NAME 
