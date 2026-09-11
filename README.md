# Forum for the Roman Republic

A simple discussion forum based on the Roman Republic. The project models users, posts, threads, and forums while enforcing ownership and access-control rules.

## Overview

The forum consists of three main concepts:

- **Post** — Content created by a user, which can be edited and upvoted.
- **Thread** — A titled collection of posts with an owner and optional tags.
- **Forum** — A collection of threads that supports searching by tag and author.

## Requirements

### Post

A `Post`:

- Has an author.
- Has content.
- Can only be edited by its author.
- Can be upvoted by any user.
- Can only be upvoted once by each user.
- Exposes its content, author, and upvote count.

### Thread

A `Thread`:

- Has a title.
- Has a first post.
- Uses the author of the first post as its owner.
- Contains a collection of posts.
- Allows any user to add a post.
- Allows users to remove only their own posts.
- Allows only the thread owner to edit the title.
- Allows only the thread owner to edit the tags.
- Can have multiple tags.

### Forum

A `Forum`:

- Contains a collection of threads.
- Allows new threads to be published.
- Allows threads to be searched by tag.
- Allows posts to be searched by author.

## Access Control

The project must enforce permissions for operations that modify existing data.

| Operation | Permission |
| --- | --- |
| Edit a post | Post author only |
| Add a post to a thread | Any user |
| Remove a post | Post author only |
| Edit thread title | Thread owner only |
| Edit thread tags | Thread owner only |
| Upvote a post | Any user, once per post |
| Search by tag | Any user |
| Search by author | Any user |

Unauthorized operations should raise a `PermissionDenied` error.

## Example Behavior

A forum can contain a thread such as:

**Battle of Zela**

> Veni, vidi, vici!

The thread is owned by **Caesar**, since he authored the first post.

Other users can contribute posts:

- Amantius — "That was quick!"
- Caesar — "Hardly broke a sweat."
- Amantius — "Any good loot?"

The forum should be able to return all posts written by Caesar when searching by author.

Caesar can edit his own post, but another user cannot.

Posts can be upvoted by multiple users, but each user may only contribute one upvote to a given post. For example, if Cleopatra attempts to upvote the same post twice, the second upvote must not increase the total.

Similarly, Cleopatra cannot change the title of Caesar's thread because she is not the thread owner. The operation should fail with `PermissionDenied`.

## Core API

The implementation should provide functionality equivalent to:

- `Forum.publish(...)`
- `Forum.search_by_author(...)`
- `Post.get_content()`
- `Post.get_author()`
- `Post.get_upvotes()`
- `Post.set_content(...)`
- `Post.upvote(...)`
- `Thread.publish_post(...)`
- `Thread.get_posts()`
- `Thread.set_title(...)`
- `Thread.set_tags(...)`

## Expected Outcome

The completed project should:

1. Model posts, threads, and forums.
2. Correctly track ownership.
3. Enforce modification permissions.
4. Prevent duplicate upvotes.
5. Support adding and removing posts according to ownership rules.
6. Support searching posts by author.
7. Support searching threads by tag.
8. Raise `PermissionDenied` when a user attempts an unauthorized operation.
