SELECT id, username
FROM auth.users
LIMIT $limit
OFFSET $offset;
