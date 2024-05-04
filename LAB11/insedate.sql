CREATE OR REPLACE PROCEDURE add_update_user(
    usname VARCHAR,
    phonumber VARCHAR
)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook_lab11 WHERE usname = $1) THEN
        UPDATE phonebook_lab11
        SET phone_number = $2
        WHERE usname = $1;
    ELSE
        INSERT INTO phonebook_lab11(usname, phone_number)
        VALUES ($1, $2);
    END IF;
END;
$$ LANGUAGE plpgsql;
