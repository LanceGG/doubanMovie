use mediadb;

create table mediadb.history_data (
	id int auto_increment primary key,
	target_num int default 0,
    num int default 0
);
insert into mediadb.history_data (id, target_num, num) values (1, 0, 0);

drop table mediadb.media_simple;
create table mediadb.media_simple (
	media_id int auto_increment primary key,
	id int not NULL,
    title varchar(200),
    rate varchar(16),
    url varchar(300),
    classify varchar(16),
    index media_real_id ( id )
);

drop table mediadb.media_detail;
create table mediadb.media_detail (
	media_detail_id int auto_increment primary key,
	id int not NULL,
    title varchar(300),
    title_long varchar(400),
    m_year varchar(100),
    classify varchar(16),
    m_type varchar(200),
    country varchar(200),
    m_language varchar(100),
    release_date varchar(100),
    runtime varchar(100),
    season varchar(100),
    episodes varchar(100),
    along_run_time varchar(100),
    alias varchar(200),
    imdb_id varchar(50),
    score varchar(50),
    stars5 varchar(50),
    stars4 varchar(50),
    stars3 varchar(50),
    stars2 varchar(50),
    stars1 varchar(50),
    report varchar(6000),
    people_num varchar(50),
    tags varchar(400),
    index media_detail_real_id (id)
);
drop table mediadb.media_recommend;
create table mediadb.media_recommend (
	media_recommend_id int auto_increment primary key,
	id int not NULL,
    title varchar(300),
    recommend_id int,
    recommend_title varchar(300),
    index media_recommend_real_id (id)
);
drop table mediadb.media_attender;
create table mediadb.media_attender (
	media_attender_id int auto_increment primary key,
	id int not NULL,
    title varchar(300),
    attender_id varchar(240),
    attender_name varchar(240),
    attender_type varchar(16),
    index media_attender_real_id (id)
);

create table mediadb.query_history_data (
	type varchar(10),
    num int
);
insert into mediadb.query_history_data (type, num) values ('DETAIL', 0);
insert into mediadb.query_history_data (type, num) values ('ACTOR', 0);
insert into mediadb.query_history_data (type, num) values ('AWARD', 0);
insert into mediadb.query_history_data (type, num) values ('PIC', 0);

create table mediadb.media_actor (
	media_actor_id int auto_increment primary key,
    id int not NULL,
    sex varchar(10),
    birthday varchar(20),
    address varchar(100),
    occupation varchar(500),
    en_name varchar(200),
    cn_name varchar(200),
    members varchar(200),
    imdb_id varchar(32)
);

create table mediadb.media_award (
	media_award_id int auto_increment primary key,
    id int not NULL,
    title varchar(300),
    award_name varchar(200),
    award_year varchar(50),
    award_type varchar(200),
    award_user_id varchar(240),
    award_user_name varchar(240)
);
