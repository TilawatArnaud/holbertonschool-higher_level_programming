-- Lists all shows contained in the database that have at least one genre linked
SELECT DISTINCT T1.id, T1.name FROM shows AS T1 JOIN genre_show AS T2 ON T1.id = T2.show_id ORDER BY T1.id ASC;
