CREATE TABLE melons (
	id SERIAL PRIMARY KEY, 
	melon_type VARCHAR(30),
	common_name VARCHAR(30),
	price NUMERIC(8, 2), 
	imgurl VARCHAR(200),
	seedless BOOLEAN
);

INSERT INTO melons VALUES(1,'Musk','Honeydew',1,'/static/1.jpg',False);
INSERT INTO melons VALUES(2,'Hybrid','Crenshaw',2,'/static/2.jpg',False);
INSERT INTO melons VALUES(3,'Hybrid','Crane',2.5,'/static/3.jpg',False);
INSERT INTO melons VALUES(4,'Musk','Casaba',2.5,'/static/4.jpg',False);
INSERT INTO melons VALUES(5,'Musk','Cantaloupe',0.99,'/static/5.jpg',False);
INSERT INTO melons VALUES(6,'Musk','Persian Melon',3,'/static/6.jpg',False);
INSERT INTO melons VALUES(7,'Musk','Christmas Melon',5.5,'/static/7.jpg',False);
INSERT INTO melons VALUES(8,'Musk','Armenian Cucumber',4.5,'/static/8.jpg',False);
INSERT INTO melons VALUES(9,'Hybrid','Galia',3.75,'/static/9.jpg',False);
INSERT INTO melons VALUES(10,'Winter','Winter Melon',0.99,'/static/10.jpg',True);
INSERT INTO melons VALUES(11,'Musk','Canary',1.5,'/static/11.jpg',False);
INSERT INTO melons VALUES(12,'Musk','Hami',2.75,'/static/12.jpg',True);
INSERT INTO melons VALUES(13,'Watermelon','Densuke',250,'/static/13.jpg',False);
INSERT INTO melons VALUES(14,'Watermelon','Ali Baba',2.5,'/static/14.jpg',False);
INSERT INTO melons VALUES(15,'Watermelon','Ancient',3,'/static/15.jpg',False);
INSERT INTO melons VALUES(16,'Watermelon','Arkansas Black',4,'/static/16.jpg',False);
INSERT INTO melons VALUES(17,'Watermelon','Dixie Queen',2,'/static/28.jpg',False);
INSERT INTO melons VALUES(18,'Watermelon','Blacktail Mountain',2.75,'/static/18.jpg',True);
INSERT INTO melons VALUES(19,'Watermelon','Carolina Cross 180',4.25,'/static/19.jpg',False);
INSERT INTO melons VALUES(20,'Watermelon','Charleston Gray',2,'/static/20.jpg',False);
INSERT INTO melons VALUES(21,'Watermelon','Chris Cross',2.5,'/static/21.jpg',False);
INSERT INTO melons VALUES(22,'Watermelon','Desert King',2,'/static/27.jpg',False);
INSERT INTO melons VALUES(23,'Watermelon','Congo',2,'/static/23.jpg',False);
INSERT INTO melons VALUES(24,'Watermelon','Crimson Sweet',1.75,'/static/25.jpg',False);

-- CREATE TABLE melon_colors (
-- 	id SERIAL PRIMARY KEY, 
-- 	melon_name VARCHAR(30),
-- 	color VARCHAR(30),
-- 	price NUMERIC(8, 2)
-- );