#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER agent WITH PASSWORD 'agent';
    ALTER USER agent WITH SUPERUSER;
EOSQL