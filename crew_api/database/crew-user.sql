-- operate with root
-- drop user 'crew-root'@'localhost';
-- drop user 'crew-leader'@'localhost';
-- drop user 'crew-member'@'localhost';
-- drop user 'crew-login'@'localhost';

create database crewmen character set utf8 collate utf8_general_ci;
create database test character set utf8 collate utf8_general_ci;

create user 'crew-root'@'localhost' identified by 'crew-root';
grant all on crewmen.* to 'crew-root'@'localhost';

create user 'test'@'localhost';
grant all on test.* to 'test'@'localhost';
