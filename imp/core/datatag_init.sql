USE imp;

INSERT INTO Tags (
	name,tag_domain,followed )
	values (
	"sb","freetag",1);
	
INSERT INTO Tags (
	name,tag_domain,followed )
	values (
	"America","location",0);

INSERT INTO Tags (
	name,tag_domain,followed )
	values (
	"Software","work_field",0);
	
INSERT INTO Tags (
	name,tag_domain,followed )
	values (
	"single man","target",0);
	
INSERT INTO UserTag (
	tag_id,user_mail )
	values (
	1,"billzeng808@gmail.com");
	
INSERT INTO EventTag (
	tag_id,event_id )
	values (
	2,1);
	
INSERT INTO OfferTag (
	tag_id,offer_id )
	values (
	3,1);
	
INSERT INTO NeedTag (
	tag_id,need_id )
	values (
	4,1);
