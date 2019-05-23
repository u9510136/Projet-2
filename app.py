# from values.py import the function values
from values import values, category_table

# import Flask
from flask import Flask, render_template, request, redirect

# create app passing the __name__
app = Flask(__name__)

# HOME PAGE
# define what to do when the user hits the "/"
@app.route("/", methods=["GET", "POST"])
def index():

        cat_id = request.args.get('cat_id')
        cat_values = values()
        global youtube_data 
        youtube_data = {}
        if not cat_id or 0 == cat_id:
                print (f"Hello all {cat_id}")
                
                youtube_data = cat_values[0]
                        
                print(youtube_data)
                        # the left variable is what is used on the html page
                return render_template("index.html", yt_data=youtube_data, cat_table= category_table())

        else:
                
                # cat_values = values()
                print(f"Hello category {cat_id}")
                # print(cat_values)
                for d in cat_values:
                        if d["cat_id"]==int(cat_id, base=10):
                                print ("pass the if line")
                                youtube_data.update({"cat_id": d["cat_id"],\
                                "cat_desc": d["cat_desc"], "videos": d["videos"],\
                                "subscribers": d["subscribers"], "view": d["view"], "engagement": d["engagement"],\
                                "Likes": d["Likes"], "Dislikes": d["Dislikes"], "Comments": d["Comments"]})
                                print(d["cat_id"], d["cat_desc"], d["videos"], d["subscribers"], d["Likes"])
                                print(youtube_data)
                
        return render_template("index.html", yt_data=youtube_data, cat_table= category_table())


# TABLE PAGE
@app.route('/table')
def tables():
    return render_template('tables.html')


if __name__=='__main__':
    app.run(debug=True)