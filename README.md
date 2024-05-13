# Overview
An application where you choose and review a list of properties. 

# Getting started

## Running docker-compose
Navigate to the root of the repo and use the docker-compose file to start the containers.
```
docker-compose up .
```

## Running individual containers
### API
- Navigate to the root of the repo
- Build the docker image
```
docker build -t mukkund1996/property-api -f api/Dockerfile .
```
- Run the docker container
```
docker run --rm mukkund1996/property-api
```

### Client
- Navigate to the root of the repo
- Build the docker image
```
docker build -t mukkund1996/property-client -f client/Dockerfile .
```
- Run the docker container
```
docker run --rm mukkund1996/property-client
```

# Docs
## Datamodel
The datamodel of the `properties.db` can be found [here](docs/datamodel).

## Requirments
The requirements can be found [here](docs/requirements).

# Contribution



