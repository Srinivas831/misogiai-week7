# ---------------- Movie ----------------
class Movie(MediaContent):
    def __init__(self, title, duration, resolution, genre, director, premium=False):
        super().__init__(title, premium)
        self.duration = duration
        self.resolution = resolution
        self.genre = genre
        self.director = director

    def play(self):
        print(f"Now playing movie: {self.title}")

    def get_duration(self):
        return self.duration

    def get_file_size(self):
        return self.duration * 5  # MB/min

    def calculate_streaming_cost(self):
        return 0.05 * self.duration

# ---------------- TVShow ----------------
class TVShow(MediaContent):
    def __init__(self, title, episodes, seasons, current_episode=1, premium=False):
        super().__init__(title, premium)
        self.episodes = episodes
        self.seasons = seasons
        self.current_episode = current_episode

    def play(self):
        print(f"Playing TV Show: {self.title} - Episode {self.current_episode}")

    def get_duration(self):
        return self.episodes * 25  # avg 25 min per episode

    def get_file_size(self):
        return self.episodes * 100

    def calculate_streaming_cost(self):
        return 0.03 * self.episodes

# ---------------- Podcast ----------------
class Podcast(MediaContent):
    def __init__(self, title, episode_number, transcript_available=False, premium=False):
        super().__init__(title, premium)
        self.episode_number = episode_number
        self.transcript_available = transcript_available

    def play(self):
        print(f"Listening to podcast: {self.title}, Episode {self.episode_number}")

    def get_duration(self):
        return 40  # avg 40 mins

    def get_file_size(self):
        return 30  # MB

    def calculate_streaming_cost(self):
        return 1.0

# ---------------- Music ----------------
class Music(MediaContent):
    def __init__(self, title, artist, album, lyrics_available=True, premium=False):
        super().__init__(title, premium)
        self.artist = artist
        self.album = album
        self.lyrics_available = lyrics_available

    def play(self):
        print(f"Playing music: {self.title} by {self.artist}")

    def get_duration(self):
        return 4  # minutes

    def get_file_size(self):
        return 8  # MB

    def calculate_streaming_cost(self):
        return 0.10
