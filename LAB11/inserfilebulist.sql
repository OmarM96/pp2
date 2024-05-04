create type person as (name text, number text);

create or replace procedure insertlist(person) as $$
declare
	nid int;
	Var	person;
begin
	foreach Var in array arr loop
		insert into phonebook (username, phonenumber)
		values (Var[0], Var[1])
		returning id into nid;
	end loop;
end;
$$ language plpgsql