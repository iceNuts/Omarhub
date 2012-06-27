USE imp;

CREATE TABLE Tags (
	tag_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	tag_domain VARCHAR(100),
	followed INT
);

CREATE TABLE UserTag (
	tag_id INT,
	user_mail VARCHAR(100),
	PRIMARY KEY(tag_id,user_mail),
	FOREIGN KEY (user_mail) REFERENCES Users(mail),
	FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);

CREATE TABLE EventTag (
	tag_id INT,
	event_id INT,
	PRIMARY KEY(tag_id,event_id),
	FOREIGN KEY (event_id) REFERENCES Events(id),
	FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);

CREATE TABLE OfferTag (
	tag_id INT,
	offer_id INT,
	PRIMARY KEY(tag_id,offer_id),
	FOREIGN KEY (offer_id) REFERENCES Offers(id),
	FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);

CREATE TABLE NeedTag (
	tag_id INT,
	need_id INT,
	PRIMARY KEY(tag_id,need_id),
	FOREIGN KEY (need_id) REFERENCES Needs(id),
	FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);
	
