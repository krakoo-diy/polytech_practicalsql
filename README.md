# Polytech_PracticalSQL



## purpose of the Project

The goal of the project is to create a skeleton of the DB required by CTA (Cherenkov Telescope Array) in order to store Metadata.  
And produce some benchmark in order to compare different implementation
They are 3 possible implementations : 
SQL (Posgres)
No-SQL (MongoDB)
Mix using json type within a SQL database (Postgres)

Specification are defined in a draft docuement "DataProducts Data Model Specification"

## Specification
The directory 'spec' contains spefications defined by CTA stakeholders.

## SQL schema

The directory 'SQL' contains 
1. SQL scripts to connect and run SQL query against PostgresSQL DB.


In order to run the benchmark, we use and Postgres instance.


## install the PostgreSQL DB : 
###Installation with Docker

####Prerequisite:
Ensure Docker is running on the host machine.

####Deploying PostgreSQL:
Run the following command to start a PostgreSQL container:

'docker run --name my_postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=mydb -p 15433:5432 -d postgres'
