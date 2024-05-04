CREATE OR REPLACE FUNCTION getAll(lim INTEGER, ofs INTEGER)
    RETURNS SETOF phonebook
AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM phonebook LIMIT lim OFFSET ofs;
END;
$$ LANGUAGE plpgsql;
