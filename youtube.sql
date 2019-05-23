-- create database youtube_db;

use youtube_db;

select * from usvideos_modified;

/* create new table with selected columns */
create table youtube (
video_id varchar(20) not null,
last_trending_date date not null,
publish_date date not null,
category_id int not null,
channel_title varchar(50) not null,
views int not null,
likes int not null,
dislikes int not null,
comment_count int not null,
title varchar(200) not null,
trend_day_count int not null,
tags_count int not null,
subscriber int not null 
);

desc youtube;

/* insert values from original table*/
insert into youtube select video_id, 
		last_trending_date,
        publish_date,
        category_id,
        channel_title,
        views,
        likes,
        dislikes,
        comment_count,
        title,
        trend_day_count,
        tags_count,
        subscriber
from usvideos_modified;

select * from youtube;
/* create table for category description*/
create table category (
category_id int not null,
category_des varchar(100)
);

/* insert the values from the github siurce*/
insert into category (category_id, category_des)
values
	(1, "Film and Animation"),
    (2, "Autos and Vehicles"),
    (10, "Music"),
    (15, "Pets and Animals"),
    (17, "Sports"),
    (18, "Short Movies"),
    (19, "Travel & Events"),
	(20,  "Gaming"),
	(21,  "Videoblogging"),
	(22,  "People & Blogs"),
	(23,  "Comedy"),
	(24,  "Entertainment"),
	(25,  "News & Politics"),
	(26,  "How to & Style"),
	(27,  "Education"),
	(28, "Science & Technology"),
	(29, "Nonprofits & Activism"),
	(30, "Movies"),
	(31, "Anime/Animation"),
	(32, "Action/Adventure"),
	(33, "Classics"),
	(34, "Comedy"),
	(35, "Documentary"),
	(36, "Drama"),
	(37, "Family"),
	(38, "Foreign"),
	(39, "Horror"),
	(40, "Sci-Fi/Fantasy"),
	(41, "Thriller"),
	(42,  "Shorts"),
	(43, "Shows"),
	(44, "Trailers");

select * from category;

/* add a category description column to the the youtube table */
ALTER TABLE youtube ADD COLUMN
	category_desc varchar(100);

/* update the category desc column with the category desc from the category table*/
update youtube y
left join category c
on y.category_id = c.category_id
set y.category_desc = c.category_des;

SELECT 
    category_desc, COUNT(*)
FROM
    youtube
GROUP BY category_desc;

Delete from youtube
where category_desc = "Autos and Vehicles";

Delete from youtube
where category_desc = "Education";

Delete from youtube
where category_desc = "Gaming";

Delete from youtube
where category_desc = "Nonprofits & Activism";

Delete from youtube
where category_desc = "Pets and Animals";

Delete from youtube
where category_desc = "Shows";

Delete from youtube
where category_desc = "Travel & Events";

SELECT 
    category_desc, COUNT(*)
FROM
    youtube
GROUP BY category_desc;

select count(*) from youtube;


select * from youtube;

select format(sum(subscriber), 2)
from youtube;

select format(sum(views), 2)
from youtube;

select format(sum(likes + dislikes + comment_count), 2) as engagement from youtube;

-- for specific categories
select count(*) from youtube
where category_desc="Comedy";

select format(sum(subscriber), 2)
from youtube
where category_desc="Comedy";

select format(sum(views), 2)
from youtube
where category_desc="Comedy";

select format(sum(likes + dislikes + comment_count), 2) as engagement
from youtube
where category_desc="Comedy";

SELECT count(*) FROM youtube where category_desc = "Sports";

select * from category;

select category_id, category_desc, count(*) as videos, format(subscriber, 2) as subscriber, 
format(views, 2) as views, format(likes,2) as likes, format(dislikes, 2) as dislikes, comment_count, 
sum(likes + dislikes + comment_count) as engagement
from youtube
group by category_id;

select count(*) as videos, sum(subscriber), 
sum(views), sum(likes), sum(dislikes), sum(comment_count), 
sum(likes + dislikes + comment_count) as engagement
from youtube
;
