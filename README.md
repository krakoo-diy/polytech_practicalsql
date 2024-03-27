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
1. SQL script needed to create the SQL schema of the metadata.
2. Python scripts needed produce benchmark
    1. to populate the DB (perform the INSERT) 
    2. to retrieve data (perform the SELECT)

In order to run the benchmark, we use and Postgres instance located in google cloud.
See https://cloud.google.com/sql/docs/postgres/connect-instance-cloud-shell

