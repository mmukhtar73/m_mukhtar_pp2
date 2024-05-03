CREATE FUNCTION search_phonebook(pattern VARCHAR(100))
RETURNS TABLE(user_name VARCHAR(100), phone_number VARCHAR(15))
AS
$$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE user_name LIKE '%' || pattern || '%' OR phone_number LIKE '%' || pattern || '%';
END;
$$
LANGUAGE plpgsql;
