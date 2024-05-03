CREATE PROCEDURE insert_or_update_user(IN in_user_name VARCHAR(100), IN in_phone_number VARCHAR(15))
AS
$$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = in_user_name) THEN
        UPDATE phonebook SET phone_number = in_phone_number WHERE user_name = in_user_name;
    ELSE
        INSERT INTO phonebook (user_name, phone_number) VALUES (in_user_name, in_phone_number);
    END IF;
END;
$$
LANGUAGE plpgsql;
