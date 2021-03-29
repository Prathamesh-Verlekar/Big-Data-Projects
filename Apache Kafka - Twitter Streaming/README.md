## Apache Kafka


#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1-1_vZ54uSCF_dE2xiKPFE62VAvNE0f5cvrCtuF4NYIU#0



**Apache Kafka** is a streaming message platform. It is a publish-subscribe based durable messaging system. Kafka is designed to be high performance, highly available, and redundant. It is used to collect, process, store, and integrate data at scale. A messaging system sends messages between processes, applications, and servers. 

Use cases for Apache Kafka:
➢	Stream Processing
➢	Messaging
➢	Website Activity Tracking
➢	Log aggregation
➢	Event Sourcing
➢	Application health monitoring


These are four main parts in a Kafka system:

- **Broker:** Handles all requests from clients (producer, consumer and metadata) and keeps data replicated within the cluster. There can be one or more brokers in a cluster
- **Zookeeper:** Keeps track of status of the Kafka clusters (brokers, topics, users)
- **Producer:** Sends records to a broker
- **Consumer:** Consumes batches of records from the broker

## Requirements

1. Installing Oracle **Virtual VM Box**

**Specifications**
- Minimum 4 GB RAM
- Minimum 40 GB Hard Drive
- Downloading **ubuntu** iso file

2. Installing **Ubuntu** Guest Edition

```
sudo apt install build-essential dkms linux-headers-$(uname -r)
```

3. Installing Python on the Virtual VM

```
sudo apt install python3`
```

4. Installing AWS CLI

```
sudo apt install curl

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

/usr/local/bin/aws --version

```

5. Connecting with AWS
```
aws configure
```

6. Installing Java jdk

```
sudo apt install default-jre

sudo apt install default-jdk

```

7. Installing Pycharm in Ubuntu


#### Download & Configure Kafka
- Download Apache Kafka from [here](https://kafka.apache.org/downloads)

-Install the required pyhton libraries
```
pip3 install kafka-python
```


#### Starting Zookeeper & Kafka Broker

Navigate to the directory where the downloaded files are unzipped and start the **Zookeeper** service:
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
Additionally, start the **Kafka broker** by running:
```
bin/kafka-server-start.sh config/server.properties
```

#### Using `producer.py`
Run the script **producer.py** for generating sample events

#### Using `consumer.py`
Run the script **consumer.py** to consume the events published by the producer.

#### Using `twitter-stream.py`
Then use the **twitter-stream.py** script to  fetch tweets from Twitter's API in real-time.

#### We will have to create a twitter developer account, then create a new project on the dev console and finally generate you API keys and bearer tokens
 
Then enter your **bearer token** in the twitter-stream.py script under the **BEARER_TOKEN** parameter.

**Tweets are published to the Kafka Broker.**

On running **consumer.py** again, we can see all the published events that are collected by the consumer.





