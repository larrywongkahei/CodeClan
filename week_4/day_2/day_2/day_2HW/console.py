import repository.albums_repository as albums
import repository.artists_repository as artists
from models.albums import Albums
from models.artists import Artist


artist1 = Artist('larry')
artists.save(artist1)
artist2 = Artist('Tim')
artists.save(artist1)

album1 = Albums('First year', 'First year', 'romance', artist1)
albums.save(album1)
album2 = Albums('First', 'year', 'romance', artist2)
albums.save(album2)
album3 = Albums('3', 'Firs', 'romance', artist2)
albums.save(album3)
album5 = Albums('5', 'Firs', 'romance', artist1)
albums.save(album5)

album6 = Albums('6', 'Firs', 'romance', artist2)
albums.save(album6)
album7 = Albums('7', 'Firs', 'romance', artist2)
albums.save(album7)


# artists.list_all_album(artist2)

# albums.delete_all()
# artists.delete_all() 