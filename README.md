# example-python-redis   

## Installing docker and starting redis as a container
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
 $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker pi
sudo reboot
docker run hello-world
sudo apt install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt install python3 python3-pip
sudo pip3 install docker-compose
sudo systemctl enable docker
sudo sysctl vm.overcommit_memory=1
docker run --rm --name redis --network=host redis:6.0.6-alpine3.12
```

## Running redis-cli from a container (in another terminal)
```bash
docker exec -it redis redis-cli
127.0.0.1:6379> set test 'hello world'
OK
127.0.0.1:6379> get test
"hello world"
127.0.0.1:6379> exit
```

## Build a Python3 container with redis-py installed (in another terminal)
```bash
docker build -t mypython .
```

## Now update app.py as desired and run
```bash
docker run --rm  -it -v "$PWD":/usr/src/app --network=host mypython python app.py
```

## How it works

1. Redis is running in one Docker container and using the 'host' isolated network.
2. Python is also running in a container on that same 'host' isolated network, but the '-v' flag maps your current directly into the container at /usr/src/app and then the docker run command starts up the container, runs 'python app.py' and then stops.

## Next steps

1. Add the desired code to app.py (e.g. the code that loops forever waiting for STDIN and sending the input to redis)
2. Create another container modeled on this one which continually listens to the redis queue and on new message sends it as an HTTP POST request to the master (http://x.x.x.11/post)
3. Add a docker-compose.yml file which incorporates all three containers


