-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
