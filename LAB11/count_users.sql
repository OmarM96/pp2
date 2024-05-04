CREATE OR REPLACE FUNCTION totalusers(PhoneContacts text)
returns integer 
as 
$$
declare 
	total integer;
BEGIN 
   SELECT count(*) into total 
   FROM PhoneContacts;   
   RETURN total; 
END; 
$$
language plpgsql
--Select totalusers());  
