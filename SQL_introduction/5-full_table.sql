-- prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT column_name, data_type, is_nullable, column_key, column_default, extra
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
