--Selecting the table to check the data:
select * from Genre;
select * from Movie_details;
select * from Movie_Ranking;
select * from MPAA_Rating;

--Updating the rank of the 3rd movie id:
Update Movie_Ranking set Movie_Rank = 10 where Movie_Id = 3;

--Deleting the record from the table:
Delete from Movie_Ranking where Movie_Id = 3;

--Deleting all records from the table:
Delete from Movie_Ranking;

--Joining the tables to retrive the movie details and its rank:
select a.Movie_Rank,b.*,c.*,d.* from Movie_Ranking a join 
Movie_details b join 
Genre c join 
MPAA_Rating d on 
a.Movie_Id = b.movie_id and a.genre_Id = c.genre_Id and a.mpaa_Id = d.mpaa_Id;