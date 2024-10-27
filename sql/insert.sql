INSERT INTO genre (genre_Id, genre) VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Musical'),
(4, 'Western'),
(5, 'Drama'),
(6, 'Thriller/Suspense'),
(7, 'Comedy'),
(8, 'Horror'),
(9, 'Black Comedy'),
(10, 'Romantic Comedy');


INSERT INTO Movie_details (movie_id, title, Year, release_date, runtime, production_cost, domestic_gross, worldwide_gross, opening_weekend) VALUES
(1, 'Avengers: Endgame', 2019, '4/23/2019', 181, 400000000, 858373000, 2797800564, 357115007),
(2, 'Pirates of the Caribbean: On Stranger Tides', 2010, '5/20/2011', 136, 379000000, 241071802, 1045713802, 90151958),
(3, 'The Campaign', 2012, '8/10/2012', 85, 95000000, 86907746, 104907746, 26588460),
(4, 'The Lovely Bones', 2009, '12/11/2009', 135, 95000000, 81562942, 165720921, 22688457),
(5, 'Tangled', 2010, '11/24/2010', 101, 260000000, 200821936, 583777242, 48767052),
(6, 'Titanic', 1997, '12/18/1997', 194, 200000000, 659363944, 2207986545, 28638131),
(7, 'Django Unchained', 2012, '12/25/2012', 165, 100000000, 162805434, 449841566, 30122888),
(8, 'Gravity', 2013, '10/3/2013', 91, 110000000, 274092705, 688214291, 55785112),
(9, 'I am Legend', 2007, '12/14/2007', 100, 150000000, 256393010, 585532684, 77211321),
(10, 'The Wolf of Wall Street', 2013, '12/25/2013', 165, 100000000, 116949183, 389918903, 18410067),
(11, 'How Do You Know?', 2010, '12/17/2010', 121, 120000000, 30212620, 49628177, 7484696),
(12, 'Tarzan', 1999, '6/16/1999', 88, 145000000, 171091819, 448191819, 34221968),
(13, 'Olympiques', 2008, '7/4/2008', 102, 113500000, 999811, 132999811, 132999811),
(14, 'Harry Potter and the Half-Blood Prince', 2009, '7/15/2009', 153, 250000000, 302089278, 929411069, 77835727),
(15, 'The Hobbit: The Desolation of Smaug', 2013, '12/12/2013', 201, 250000000, 258241522, 959358436, 73645197),
(16, 'The Hobbit: The Battle of the Five Armies', 2014, '12/10/2014', 144, 250000000, 255119788, 940389558, 54724334),
(17, 'The Fate of the Furious', 2017, '4/7/2017', 136, 250000000, 225764765, 1236703796, 98786705),
(18, 'No Time to Die', 2021, '9/29/2021', 163, 250000000, 160891007, 760008036, 55225007),
(19, 'Avatar', 2009, '12/17/2009', 162, 237000000, 785221649, 2910370905, 77025481),
(20, 'Superman Returns', 2006, '6/28/2006', 150, 232000000, 200120000, 391081192, 52535096);

INSERT INTO MPAA_Rating (mpaa_Id, mpaa, mpaa_details) VALUES
(1, 'PG-13', 'Not recommended for children (preteens) under age of 13 in the United States.'),
(2, 'PG', 'PARENTAL GUIDANCE SUGGESTED'),
(3, 'G', 'Appropriate for people of all ages.'),
(4, 'R', 'Requires accompanying parent or adult guardian'),
(5, 'Unrated', 'Not Rated');

INSERT INTO Movie_Ranking (Movie_Rank, Movie_Id, mpaa_Id, genre_Id) VALUES
(1, 1, 1, 1),
(2, 2, 1, 2),
(3, 3, 4, 7),
(4, 4, 1, 5),
(5, 5, 2, 3),
(6, 6, 1, 5),
(7, 7, 4, 4),
(8, 8, 1, 6),
(9, 9, 1, 8),
(10, 10, 4, 9),
(11, 11, 4, 10),
(12, 12, 3, 2),
(13, 13, 5, 1),
(14, 14, 1, 1),
(15, 15, 2, 2),
(16, 16, 2, 1),
(17, 17, 1, 2),
(18, 18, 1, 1),
(19, 19, 2, 2),
(20, 20, 1, 1);