from flask import Flask,jsonify,request 
import csv

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
 
liked_articles=[]
disliked_articles=[]

app= Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    }) 

@app.route("/liked-articles",methods=["POST"])  
def get_liked_article():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"success"
    }) 

@app.route("/disliked-articles",methods=["POST"])
def get_disliked_article():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(articles)
    return jsonify({
        "status":"success" 
    })

if __name__=="__main__":
    app.run() 