# MAC_address_Lookup
# I have pushed the code under this location along with Docket file
# First clone the repo to your local machine
# Then chnage the sorce location of files as per your system in Docker file
# Then build image from that docker file
$ docker build -t macaddr .

# Then Run the container using below command
$docker run -itd --name surya -P macaddr:latest /bin/bash

# Then enter into the docker container using below commnad
$ docker exec -it Container_ID bash
# Once Entered into docker container then below command to get the out put
$ python AddressLookup.py --mac_address=44:38:39:ff:ef:57
