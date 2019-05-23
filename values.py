import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from pprint import pprint

from config import config

import pymysql
pymysql.install_as_MySQLdb()

# FUNCTION TO CREATE THE DROPDOWN MENU OF CATEGORIES
def category_table():
    engine = create_engine(f'mysql://root:{config}@localhost:3306/youtube_db')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query('youtube')
    category_list= []

    category_list.append({'cat_id': 0, 'cat_desc': 'all categories'})
    with engine.connect() as con:
        records=  con.execute('select category_id, category_desc from youtube group by category_desc')
        for record in records:
            category_list.append({'cat_id':record[0], 'cat_desc': record[1]})


        session.close
        # print(category_list)
        return category_list

# FUNCTION TO POPULATE FOR ALL CATEGORIES
def values():
    engine = create_engine(f'mysql://root:{config}@localhost:3306/youtube_db')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query('youtube')

    with engine.connect() as con:
        
        # total videos
        videos = con.execute('SELECT count(*) FROM youtube')
        for video in videos:
            print(video[0])
        # total subscribera
        subs = con.execute("select format(sum(subscriber), 0) from youtube")
        for sub in subs:
            print(sub[0])
        # total views
        views = con.execute("select format(sum(views), 0) from youtube")
        for view in views:
            print(view[0])
        # total engagement
        engages = con.execute("select format(sum(likes + dislikes + comment_count), 0) as engagement from youtube")
        for engage in engages:
            print(engage[0])
        
        ### Breakdown of Engagement metrics for bar graph
        likes = con.execute("select sum(likes) from youtube")
        for like in likes:
            print(like[0])
        dislikes =con.execute("select sum(dislikes) from youtube")
        for dislike in dislikes:
            print(dislike[0])
        comments =con.execute("select sum(comment_count) from youtube")
        for comment in comments:
            print(comment[0])

        values_dict = [{"cat_id": 0, "cat_desc": "all categories", "videos": video[0], "subscribers": sub[0], "view": view[0],
        "engagement": engage[0], "Likes": like[0], "Dislikes": dislike[0], "Comments": comment[0]}]
        # print(values_dict)

        categories= con.execute('select category_id, category_desc, count(*) as videos, format(subscriber, 0), \
            format(views, 0), likes, dislikes, comment_count,\
            format(sum(likes + dislikes + comment_count), 0) as engagement\
            from youtube group by category_id')
    
    session.close

    for cat in categories:
        values_dict.append({"cat_id": cat[0], "cat_desc": cat[1], "videos": cat[2], "subscribers": cat[3], \
        "view": cat[4], "engagement": cat[8], "Likes": cat[5], "Dislikes": cat[6], "Comments": cat[7]})
    
    # print(values_dict)
    return(values_dict)


