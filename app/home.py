from flask import Blueprint, render_template
from flask import session

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home_blueprint.route("/")
def home():
    session['ui_version'] = 1  # to set the version to have on each template the good base_1 or 2.....
    return render_template("/homes/home.html")

@home_blueprint.route("/2")
def home_2():
    session['ui_version'] = 2  
    return render_template("/homes/home_2.html")

@home_blueprint.route("/3")
def home_3():
    session['ui_version'] = 3  
    return render_template("/homes/home_3.html")

# @home_blueprint.route("/4")
# def home_4():
#     session['ui_version'] = 4  
#     return render_template("/homes/home_4.html")


# @home_blueprint.route("/3")
# def home_3():
#     session['ui_version'] = 3  
#     return render_template("home_3.html") if you want to add a 3rd version....