import os
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Get all stocks the user owns and their remaining shares
    rows = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM(shares) > 0",
        id=user_id
    )

    total_value = 0
    for row in rows:
        total_value += row["shares"] * row["price"]

    # Get user cash
    user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
    user_cash = user_cash_db[0]["cash"]

    return render_template("index.html", database=rows, cash=user_cash, total_value=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Get form data
        symbol = request.form.get("symbol")
        shares_input = request.form.get("shares")

        # Validate symbol input
        if not symbol:
            return apology("Must provide symbol")

        # Lookup the stock price
        stock = lookup(symbol.upper())
        if stock is None:
            return apology("Symbol doesn't exist")

        # Validate and convert shares input
        try:
            shares = float(shares_input)  # Allow fractional shares, change to int if not allowed
        except ValueError:
            return apology("Shares must be a number")

        # Check for negative or zero shares
        if shares <= 0:
            return apology("Shares must be a positive number")

        # If you only want whole numbers of shares, use `int(shares)` instead of `float(shares)`
        if shares % 1 != 0:
            # If fractional shares aren't allowed
            return apology("Fractional shares are not allowed")

        shares = int(shares)  # Convert to integer if you're allowing only whole shares

        # Calculate transaction value
        transaction_value = shares * stock["price"]

        # Get user cash balance from the database
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        # Check if the user has enough cash to buy the shares
        if user_cash < transaction_value:
            return apology("You don't have enough cash to complete the purchase")

        # Update user's cash balance and record the transaction
        uptd_cash = user_cash - transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", uptd_cash, user_id)
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?,?,?,?,?)",
                   user_id, stock["symbol"], shares, stock["price"], date)

        flash("Purchase successful!")
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT * FROM transactions WHERE user_id = :id", id=user_id)
    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:

        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Most give symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol dosent exist")
        return render_template("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":  # Correct indentation here
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

    if not username:
        return apology("Must give username")  # Corrected "Most" to "Must"

    if not password:
        return apology("Must give password")  # Corrected "Most" to "Must"

    if not confirmation:
        return apology("Must give confirmation")  # Added closing quotation mark

    if password != confirmation:
        return apology("Passwords don't match")  # Corrected "Passwors" to "Passwords"

    hash = generate_password_hash(password)

    try:
        new_user = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
    except:
        return apology("username already taken")

    session["user_id"] = new_user

    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        # Fetch the symbols where the user has positive shares
        symbols_user = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM(shares) > 0",
            id=user_id
        )
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_user])
    else:
        symbol = request.form.get("symbol")
        shares = float(request.form.get("shares"))  # Allow fractional shares, ensure it's float

        if not symbol:
            return apology("Must provide symbol")

        stock = lookup(symbol.upper())

        if stock is None:
            return apology("Symbol doesn't exist")

        if shares <= 0:
            return apology("Shares must be positive")

        transaction_value = shares * stock["price"]
        user_id = session["user_id"]

        # Check if the user has enough shares to sell by summing up the shares for that symbol
        user_shares = db.execute(
            "SELECT SUM(shares) AS total_shares FROM transactions WHERE user_id = :id AND symbol = :symbol",
            id=user_id, symbol=symbol
        )
        if not user_shares or user_shares[0]["total_shares"] <= 0:
            return apology("You don't have any shares of this symbol")

        user_shares_real = user_shares[0]["total_shares"]
        if shares > user_shares_real:
            return apology("Not enough shares")

        # Update user's cash
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]
        updated_cash = user_cash + transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

        # Record the transaction (selling shares)
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                   user_id, stock["symbol"], -shares, stock["price"], date)

        flash("Sold shares!")
        return redirect("/")  # Redirect to the index page after the sale is completed


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow users to change their password"""
    if request.method == "GET":
        return render_template("change_password.html")

    else:  # POST request
        # Get form data
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        # Validate form data
        if not old_password or not new_password or not confirm_password:
            return apology("All fields are required")

        if new_password != confirm_password:
            return apology("New passwords do not match")

        # Get the current user's ID
        user_id = session["user_id"]

        # Fetch user's current password hash from the database
        user_data = db.execute("SELECT hash FROM users WHERE id = ?", user_id)
        if len(user_data) != 1:
            return apology("User not found")

        current_hash = user_data[0]["hash"]

        # Verify the old password
        if not check_password_hash(current_hash, old_password):
            return apology("Incorrect old password")

        # Check if the new password is sufficiently strong
        if len(new_password) < 8:
            return apology("New password must be at least 8 characters long")

        # Hash the new password
        new_hash = generate_password_hash(new_password)

        # Update the password in the database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, user_id)

        # Provide feedback
        flash("Yei cambiaste tu contraseña!")
        return redirect("/")
