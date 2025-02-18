
# DOCKER BASICS

With the first project of Docker I have started wuth prinitng the hello world.
 
 First of all we create the file with name app.py

 



 


## Documentation

 1. [Docker](https://docs.docker.com/)
 2. [Docker Desktop](https://docs.docker.com/)





## Deployment

Now to reply the very basic website we will use the following commands to do so..
1. First of all we will download the Docker desktop and make the connections.
2. After that we will download the extensions of Docker and python

i) Now we will check that if docker and python is present in our or not. To check that we will run the following commands.

For Docker:
```bash
docker --version 
```
For Python:
```bash
docker --version 
```

 Now we have both the things i.e Docker and Python.

 ii) Now we will run the commands to buila our app.
```bash
docker build -t app.py .
```
iii) Then we will check if the image is build or not.
```bash
docker images
```
iv) Now in the last we will run the command to run our app and print the Hello World in console.

```bash
docker run -t app.py
```





