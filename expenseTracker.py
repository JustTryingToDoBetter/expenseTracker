## Application should run from the command line and should have the following features:
## Users can add an expense with a description and amount.
## Users can update an expense.
## Users can delete an expense.
## Users can view all expenses.
## Users can view a summary of all expenses.
## Users can view a summary of expenses for a specific month (of current year).

import json
import argparse
from datetime import datetime 

expense_file = "expenseTracker.json"

def load_expenses():
    try:
        with open(expense_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expense(expense):
    with open(expense_file, "w") as file:
        json.dump(expense, file,indent=4)

def addExpense(item, amount):
    expenses = load_expenses()
    expenses.append({
        "id" : len(expenses) + 1,
        "expense" : item,
        "date" : datetime.now().strftime("%Y-%m-%d"),
        "amount" : float(amount)
    })
    save_expense(expenses)
    print("Expense has been successfully added!")

def updateExpense(id, expense, amount):
    expenses = load_expenses()
    for exp in expenses:
        if exp["id"] == int(id):
            if expense:
                exp["expense"] = expense
            if amount:
                exp["amount"] = amount
            print("expense update!")
    save_expense(expenses)

def deleteExpense(id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != int(id)]
    save_expense(expenses)
    print("Expense has been deleted!")
        
    
    save_expense(expenses)

def viewAll():
    expenses = load_expenses()
    for exp in expenses:
           print(exp)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["add", "viewAll", "update", "delete"], help="command to execute")
    parser.add_argument("--expense", type=str, help="expense to add/delete/update")
    parser.add_argument("--amount", type=str, help="expense to add/delete/update")
    parser.add_argument("--id", type=int, help="expense ID to update/delete")

    args = parser.parse_args()

    if args.command == "add":
        if not args.expense:
            print("Error: --expense is required for adding expense")
        else:
            addExpense(args.expense, args.amount)

    elif args.command == "viewAll":
        viewAll()
    
    elif args.command == "update":
        if not args.expense:
            print("Error: --expense is required for updating expense")
        else:
            updateExpense(args.expense, args.amount)

    elif args.command == "delete":
        if not args.expense:
            print("Error: --expense is required for deleting expense")
        else:
            deleteExpense(args.expense)


if __name__ == "__main__":
    main()







