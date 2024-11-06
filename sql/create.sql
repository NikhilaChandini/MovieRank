CREATE TABLE genre (
    genre_Id INTEGER    PRIMARY KEY
                        UNIQUE
                        NOT NULL,
    genre    TEXT (100) 
);

CREATE TABLE Movie_details (
    movie_id        INTEGER    PRIMARY KEY
                               UNIQUE
                               NOT NULL,
    title           TEXT (100),
    Year            NUMERIC,
    release_date    TEXT (100),
    runtime         NUMERIC,
    production_cost REAL,
    domestic_gross  REAL,
    worldwide_gross REAL,
    opening_weekend REAL
);

CREATE TABLE MPAA_Rating (
    mpaa_Id      INTEGER    PRIMARY KEY
                            UNIQUE
                            NOT NULL,
    mpaa         TEXT (100),
    mpaa_details TEXT (150) 
);

CREATE TABLE Movie_Ranking (
    Movie_Rank INTEGER PRIMARY KEY
                       UNIQUE
                       NOT NULL,
    Movie_Id   INTEGER REFERENCES Movie_details (movie_id),
    mpaa_Id    INTEGER REFERENCES MPAA_Rating (mpaa_Id),
    genre_Id   INTEGER REFERENCES Genre (genre_Id) 
);

