create table media (
	media_id int auto_increment primary key,
	id int not NULL,
    title varchar(200),
    rate varchar(16),
    url varchar(300),
    classify varchar(16),
    index media_real_id ( id )
);

create table media_detail (
	media_detail_id int auto_increment primary key,
	id int not NULL,
    title varchar(200),
    title_long varchar(300),
    m_year varchar(10),
    classify varchar(16),
    m_type varchar(200),
    country varchar(200),
    m_language varchar(100),
    release_date varchar(100),
    runtime varchar(10),
    season varchar(10),
    episodes varchar(10),
    along_run_time varchar(10),
    alias varchar(200),
    imdb_id varchar(16),
    score varchar(10),
    stars5 varchar(20),
    stars4 varchar(20),
    stars3 varchar(20),
    stars2 varchar(20),
    stars1 varchar(20),
    people_num varchar(10),
    tags varchar(300),
    index media_detail_real_id (id)
);

create table media_recommend (
	media_recommend_id int auto_increment primary key,
	id int not NULL,
    title varchar(200),
    recommend_id int,
    recomment_title varchar(200),
    index media_recommend_real_id (id)
);

create table media_attender (
	media_attender_id int auto_increment primary key,
	id int not NULL,
    title varchar(200),
    attender_id int,
    attender_name varchar(240),
    attender_type varchar(16),
    index media_attender_real_id (id)
)
