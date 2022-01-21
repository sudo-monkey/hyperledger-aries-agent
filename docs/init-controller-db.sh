#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER agent;
    CREATE DATABASE aries;
    GRANT ALL PRIVILEGES ON DATABASE aries TO agent;
EOSQL