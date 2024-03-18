-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT show.title, genre.name
FROM tv_shows AS show
LEFT JOIN tv_show_genres AS show_genre
ON show.id = show_genre.show_id
LEFT JOIN tv_genres AS genre
ON show_genre.genre_id = genre.id
ORDER BY show.title, genre.name ASC;
