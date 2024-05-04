create or replace function find_word(word varchar)
	returns table (username varchar, phonenumber varchar)
language plpgsql as $$
begin
	return query
	SELECT *
	FROM phonebook
	WHERE (phonebook.username = word) or (phonebook.phonenumber = word);
	
end;
$$