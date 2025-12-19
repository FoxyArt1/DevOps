param(
    [string]$ServiceName = "db"
)

$DB_NAME = "devops7"
$DB_USER = "devops_user"

docker compose exec -T $ServiceName psql `
  -U $DB_USER `
  -d $DB_NAME `
  -f /docker-entrypoint-initdb.d/init.sql
