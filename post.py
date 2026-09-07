from exceptions import PermissionDenied


class Post:
  def __init__(self, content, author):
    """
    Creates a new Post by the author with the given content.
    You will need to track up votes more cleverly than previously because
    a user is only allowed to vote *once*.
    """
    pass
  
  def get_author(self):
    """
    Returns the author of the Post.
    """
    pass
  
  def get_content(self):
    """
    Returns the content of the Post.
    """
    pass
  
  def get_upvotes(self):
    """
    Returns a non-negative integer representing the total number of upvotes.
    """
    pass
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    pass
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    pass