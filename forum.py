from post import Post
from thread import Thread


class Forum:
  def __init__(self):
    """
    Perform initialisation of a new Forum object, as needed.
    """
    self.threads = []
  
  def get_threads(self):
    """
    Returns a list of Threads in the Forum, in the order that they were published.
    """
    return self.threads
  
  def publish(self, title, content, author):
    """
    Creates a new Thread with the given title and adds it to the Forum.
    The content and author are provided to allow you to create the first Post object.
    Threads are stored in the order that they are published.
    Returns the new Thread object.
    """
    thread = Thread(title, content, author)

    self.threads.append(thread)
    return thread
  
  def search_by_tag(self, tag):
    """
    Searches all forum Threads for any that contain the given tag.
    Returns a list of matching Thread objects in the order they were published.
    """
    matching = []

    for thread in threads:
      if tag in tread.get_tags():
        matching.append(thread)

    return matching
  
  def search_by_author(self, author):
    """
    Searches all forum Threads for Posts by the given author.
    Returns a list of matching Post objects in any order you like.
    """
    matching = []

    for thread in threads:
      if author == tread.get_owner():
        matching.append(thread)

    return matching