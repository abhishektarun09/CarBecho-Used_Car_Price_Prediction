from src.utils import apology, login_required
from flask import Flask, flash, redirect, render_template, request, session, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from database.models import User


change_password_bp = Blueprint("change_password_bp", __name__, template_folder ="templates", static_folder="static")

@change_password_bp.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change Password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure old password was submitted
        if not request.form.get("old_password"):
            return apology("must provide old password", 400)

        # Ensure new password was submitted
        elif not request.form.get("new_password"):
            return apology("must provide new password", 400)

        # Ensure new password was reentered
        elif not request.form.get("confirmation_password"):
            return apology("must re enter password", 400)

        # Ensure new password is same as confirmation password
        elif not (request.form.get("new_password") == request.form.get("confirmation_password")):
            return apology("passwords don't match", 400)

        # Ensure new password is not same as old password
        elif not (request.form.get("new_password") != request.form.get("old_password")):
            return apology("enter new password", 400)

        # Query database for User details
        user = User.query.get(session["user_id"])

        # Ensure old password is correct
        if not user or not check_password_hash(user.hash, request.form.get("old_password")):
            return apology("must provide valid old password", 401)

        # Hash new password and update
        user.hash = generate_password_hash(request.form.get("confirmation_password"))
        db.session.commit()

        flash("Password Changed!")

        return redirect("/"), 302

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("change_password.html")