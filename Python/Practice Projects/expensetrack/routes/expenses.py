from flask import Blueprint, render_template
from models import Expense

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@expenses_bp.route('/')
def dashboard():
    all_expenses = Expense.query.all()
    return render_template('dashboard.html', expenses=all_expenses)
