from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog(BaseModel):
    title: str
    detail: str
    published: bool = True
    ratings: Optional[float] = None

blog_posts = [
    {"title": "Blog 1", "detaii": "This is will serve as the first blog post", "published": True, "ratings": 4, "id": 1},
    {"title": "Blog 2", "detaii": "This is will serve as the second blog post", "published": False, "ratings": 3.5, "id": 2},
]

# Get all blog posts
@app.get("/posts")
async def get_posts():
    return {"data": blog_posts}

# Get a single blog post
@app.get("/posts/{id}")
async def get_post(id: int):
    post = blog_posts[id-1]
    return {"data": post}


# Create a new blog post
@app.post("/posts")
async def create_post(blog: Blog):
    blog_posts.append(blog.dict())
    return {"new post": blog_posts[-1]}

# Update a blog post
@app.put("/posts/{id}")
async def update_post(id: int, blog: Blog):
    blog_posts[id-1] = blog.dict()
    return {"updated post": blog_posts[id-1]}

# Delete a blog post
@app.delete("/posts/{id}")
async def delete_post(id: int):
    for post in blog_posts:
        if post["id"] == id:
            blog_posts.remove(post)
            return {"message": "Post has been deleted"}