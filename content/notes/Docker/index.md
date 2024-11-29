# Docker

WIP

## PC vs VM vs Containers

VM you split up resources and is quite heavy
Containers shares the resources but has environments set up

## Docker

Uses an image to create a container

- An image can be made up of a few programs. Lets say your application needs python, mySQL. That image will contain those.

```
docker [OPTIONS] command
docker help
docker run -d -p 80:80 docker/getting-started:latest
docker ps - shows what dockers are running
docker stop CONTAINER_ID
docker kill CONTAINER_ID
docker images
docker exec CONTAINER_ID ls
	list dirs in that container
```

docker run -d -e NODE_ENV=development -e url=http://localhost:3001 -p 3001:2368 -v ghost-vol:/var/lib/ghost/content ghost
![718f5bff3f593718fbddd8bffe88c52c.png](:/71d8dfa2862d480ebb4cff572ac2f53a)

```
docker rm CONTAINER_ID
docker volume rm VOLUME_NAME
```

Need to stop then remove container before you're allowed to remove volume.

## Isolating container via offline mode

Example: if you want students to run code on machines. Auditing a malware in a container. Running sussy program that you dont want access to network.

## Load balancing

We don't want server(s) to get overwealmed. So we have something to balance the load. So we split traffic to different servers. Many different ways.

- **Round Robin** is one of them. Client 1 -> Server 1. Client 2 -> Server 2. Client 3 -> Server 3. Client 4 -> Server 1.

`docker run -p 8001:80 -v $PWD/index1.html:/usr/share/caddy/index.html caddy`

## CI/CD pipeline

Code -> Commit -> Push -> Pull Request -> Merged ->
builds -> Image built -> Pushed to DockerHub ->
K8s docker pull -> restart containers

The 2nd and 3rd pieces should be automated. To help deploy the latest software. All backend work.
