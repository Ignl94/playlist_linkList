from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

    def add_song(self, title):
        song = Song(title)
        if self.__first_song == None:
            self.__first_song = song
        else:
            song.set_next_song(self.__first_song)
            self.__first_song = song
        print(song.get_title())
        if song.get_next_song() is not None:
            print(song.get_next_song().get_title())

    # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
    # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

    def find_song(self, title):
        count = 0
        current_node = self.__first_song
        while current_node:
            if current_node.get_title() == title:
                return count
            current_node = current_node.get_next_song()
            count += 1
        return -1

    # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed.

    def remove_song(self, title):
        if self.__first_song == title:
            self.__first_song = self.__first_song.get_next_song()
            return True
        current_node = self.__first_song
        while current_node:
            if current_node.get_next_song() == title:
                current_node.set_next_song(
                    current_node.get_next_song().get_next_song())
                return True
        return False

    # TODO: Create a method called length, which returns the number of songs in the playlist.

    def length(self):
        count = 0
        current_node = self.__first_song
        while current_node:  # while current node is not None
            current_node = current_node.get_next_song()
            count += 1
        return count

    # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

    # Example:
    # 1. Song Title 1
    # 2. Song Title 2
    # 3. Song Title 3

    def print_songs(self):
        current_node = self.__first_song
        while current_node:
            print(current_node.get_title())
            current_node = current_node.get_next_song()
