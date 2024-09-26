#!/bin/bash
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "USE $MYSQL_DATABASE; SELECT 1 FROM Censos LIMIT 1;" >/dev/null 2>&1
