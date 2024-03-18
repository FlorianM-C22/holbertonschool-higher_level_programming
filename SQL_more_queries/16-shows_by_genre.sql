-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT shows.title AS show_title, genres.name AS genre_name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
ON shows.id = show_genres.show_id
LEFT JOIN tv_genres AS genres
ON show_genres.genre_id = genres.id
ORDER BY show_title ASC, genre_name ASC;
