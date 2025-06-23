-- Lists all records of the table second_table
-- don't list rows where the name is NULL
-- Records listed in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
