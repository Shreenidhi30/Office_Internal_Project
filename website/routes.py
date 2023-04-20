from flask import Flask, request, render_template,Blueprint


webs=Blueprint('website',__name__)

@webs.route('/')
def home():
    return render_template('home.html')

@webs.route('/admin/food', methods=['GET', 'POST'])
def food():
    return render_template("admin.html")


# @webs.route('/food', methods=['GET', 'POST'])
# def food():
#     if request.method == 'POST':
#         option = request.form['option']
#         if option == 'vegetarian':
#             return 'You have chosen vegetarian food for lunch!'
#         elif option == 'non-vegetarian':
#             return 'You have chosen non-vegetarian food for lunch!'
#         else:
#             return 'Invalid option selected.'
#     else:
#         return render_template('food.html')
    

