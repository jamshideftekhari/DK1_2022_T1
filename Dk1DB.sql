create database dk12021;
use dk12021;

create table person(
Personid int not null auto_increment,
LastName varchar(30) not null,
FirstName varchar(30) not null,
Age int,
FavoritChips varchar(20),
primary key (Personid) 
); 

insert into person (LastName, FirstName, Age, FavoritChips) values ("eftekhari", "Jamshid", 57, "havSalt")
-- nvarchar() for unicode