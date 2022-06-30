INSERT INTO auth.users (username)
VALUES ($1)
RETURNING id, username;
