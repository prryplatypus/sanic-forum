SELECT id, username
FROM auth.users
WHERE username = $1
LIMIT 1;
