from src.utils import apology
from flask import flash, redirect, render_template, request, session, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from database.models import User


accounts_bp = Blueprint("accounts_bp", __name__, template_folder ="templates", static_folder="static")
  
@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        user = User.query.filter_by(username=request.form.get("username")).first()

        # Ensure username exists and password is correct
        if not user or not check_password_hash(user.hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user.id
        
        flash("Login Successful!")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@accounts_bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    
    flash("You have logged out successfully.")

    # Redirect user to login form
    return redirect("/")

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("must re enter password", 400)

        # Ensure password is same as confirmation password
        elif not (request.form.get("password") == request.form.get("confirmation")):
            return apology("passwords don't match", 400)

        # Hash the password
        hash = generate_password_hash(request.form.get("password"))

        try:
            # Check if username already exists
            existing_user = User.query.filter_by(username=request.form.get("username")).first()
            if existing_user:
                return apology("think of another username", 400)

            # Create and add user
            new_user = User(username=request.form.get("username"), hash=hash)
            db.session.add(new_user)
            db.session.commit()

            # Remember which user has logged in
            session["user_id"] = new_user.id
            
            flash("Registered!")

            # Redirect user to home page
            return redirect("/")

        except Exception as e:
            # raise CustomException(e, sys)
            # Username already exists
            return apology("think of another username", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")