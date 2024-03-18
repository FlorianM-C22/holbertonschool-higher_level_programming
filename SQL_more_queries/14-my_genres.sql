-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
