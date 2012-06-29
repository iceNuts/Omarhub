USE imp;

INSERT INTO Organization (
	name,acronym,found_date,site_url,_type,numberOfemployees,
	phoneNumber,country_code )
	values (
	"Beihang University","buaa","1952-10-25","www.beihang.com",1,1000,
	"1234567","86");
	
INSERT INTO Users (
	first_name,last_name,age,gender,mail,org_id)
	values (
	"unActivated","zly",22,0,"zlychaos@gmail.com",1);
	
INSERT INTO Users (
	first_name,last_name,age,gender,mail,passwd,org_id)
	values (
	"Bill","Zeng",16,0,"billzeng808@gmail.com","alpine",1);
	
INSERT INTO Users (
	first_name,last_name,age,gender,mail,passwd,org_id)
	values (
	"Jadon","Wong",16,0,"clww.me@gmail.com","alpine",1);
	
INSERT INTO Admins (
	first_name,last_name,mail,passwd)
	values (
	"First","Admin","371347230@qq.com","alpine");
	
INSERT INTO Recent_Events (
	_type,typeId,_from,followed)
	values (
	"Events",1,"billzeng808@gmail.com",0);
	
INSERT INTO Recent_Events (
	_type,typeId,_from,followed)
	values (
	"Offers",1,"billzeng808@gmail.com",0);
	
INSERT INTO Recent_Events (
	_type,typeId,_from,followed)
	values (
	"Needs",1,"billzeng808@gmail.com",0);
	
INSERT INTO Events (
	mail,title,description,followed)
	values (
	"billzeng808@gmail.com","Dance","Jazz & Classical",0);
	
INSERT INTO Needs (
	mail,title,description,followed)
	values (
	"billzeng808@gmail.com","Java programmer wanted","Android Application Development",0);
	
INSERT INTO Offers (
	mail,title,description,followed)
	values (
	"billzeng808@gmail.com","Volunteer","2012 London Olympic Games",0);
