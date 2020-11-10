class Track():
  def __init__ (self, name=" ", duration=0):
    self.name = name
    self.duration = duration
  def show(self):
    return f"<{self.name} - {self.duration}>"

  def track_name(self, name):
    self.name = name

  def track_duration(self, duration):
    self.duration = duration

class Album():
  def __init__(self, name=" ", group=" "):
    self.name = name
    self.group = group
    self.tracks = []

  def get_tracks(self):
    return [track.show() for track in self.tracks]


  def get_duration(self):
    return sum([track.duration for track in self.tracks])

  def get_add_track(self, track):
    if not isinstance(track, Track):
      raise NotImplementedError("Невозможно добавить")
    self.tracks.append(track)


albums = []
album = Album("The Fame Monster","Lady Gaga")
album.get_add_track(Track("Just Dance",3))
album.get_add_track(Track("Teeth",4))
album.get_add_track(Track("Paparazzi",5))
albums.append(album)

album = Album("Artpop","Lady Gaga")
album.get_add_track(Track("Artpop",4))
album.get_add_track(Track("Swine",4))
album.get_add_track(Track("Donatella",7))
albums.append(album)

for album in albums:
  print(f"Альбом {album.name} группы {album.group}:")
  for track in enumerate(album.get_tracks(), 1):
    print(f"{track[0]}. {track[1]}")
  print(f"Общая длительность альбома: {album.get_duration()} минут\n")
