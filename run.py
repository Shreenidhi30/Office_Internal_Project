from website import create_app


app=create_app()
#app.config['SECRET_KEY']='656546546544465464'



if __name__=="__main__":
    app.run(debug=True,port=8000)