

# For Flask..duh
# import Flask libraries for creating the db
from datetime import datetime
from sqlalchemy.sql import func
from flask import Flask

# For connecting to databases like MySQL, Postgres, etc.
from flask_sqlalchemy import SQLAlchemy

# template for HTML
from flask import render_template, redirect, url_for

# for handling GET and POST requests
from flask import request

from flask import jsonify, request
from flask_cors import CORS


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# creating a database in Postgres using Flash

# instantiate the a pp
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresTMA@localhost/postgres'
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
# create class. Here expeses is the name of the table in Postgres


class expenses(db.Model):

    # Defining column names
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), unique=False)
    date = db.Column(db.Date(), unique=False)
    card = db.Column(db.String(120), unique=False)
    category = db.Column(db.String(120), unique=False)
    price = db.Column(db.Float, unique=False)

    # Standard Flask syntax for DB creation
    def __init__(self, date, desc, card, cat, price):

        # LHS has to match column name. Here the column names are Description and Date
        self.description = desc
        self.date = date
        self.card = card
        self.category = cat
        self.price = price

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def __repr__(self):
    return '<User %r>' % self.username


@app.route("/")
def myfunc():

    return("hello")

# Used to add an expense into the DB
@app.route("/addExpense", methods=['POST'])
def add_item():

    # Retrieve inputs from the json request sent to the web API
    date = request.json['date']
    desc = request.json['description']
    card = request.json['card']
    cat = request.json['category']
    price = request.json['price']

    user = expenses(date, desc, card, cat, price)
    db.session.add(user)
    db.session.commit()
    return get_data()

# Used to retrieve all the expenses from the DB
@app.route("/getExpenses", methods=['GET'])
def get_data():
    import datetime
    import calendar
    month = datetime.datetime.today().month
    year = datetime.datetime.today().year

    lastDay = calendar.monthrange(year, month)[1]

    startDate = str(year) + '-' + str(month) + '-' + '01'
    endDate = str(year) + '-' + str(month) + '-' + str(lastDay)

    # retrieving input from the front end with element name tag as
    allExpenses = expenses.query.filter(expenses.date >= startDate).filter(
        expenses.date <= endDate)

    sumMonth = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumMonth')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category != 'INCOME').filter(expenses.category != 'CREDIT CARD')

    results = [
        {
            "id": Expense.id,
            "date": Expense.date.strftime("%x"),
            "price": Expense.price,
            "description": Expense.description,
            "card": Expense.card,
            "category": Expense.category
        } for Expense in allExpenses]

    for sumMonth in sumMonth:
        sumMonth = round(sumMonth.sumMonth, 2)

    return {"Count": len(results), "Expenses": results, "Sum": sumMonth}


@app.route("/getRunningTotal", methods=['GET'])
def getRunningTotal():
    import datetime
    import calendar
    month = datetime.datetime.today().month
    year = datetime.datetime.today().year

    lastDay = calendar.monthrange(year, month)[1]

    startDate = str(year) + '-' + str(month) + '-' + '01'
    endDate = str(year) + '-' + str(month) + '-' + str(lastDay)

    qryCat = "SELECT extract(day from date), extract(month from date), SUM(price) FROM public.expenses WHERE date >= '" + \
        startDate+"' and date <= '" + endDate + "' GROUP by 1,2"
    dataCat = db.engine.execute(qryCat)

    runningTotal = [
        {

            "day": int(row[0]),
            "total": round(row[2], 2)
        } for row in dataCat]

    return{"RunningTotal": runningTotal}


@app.route("/getSum", methods=['GET'])
def getSum():
    import datetime
    import calendar
    month = datetime.datetime.today().month
    year = datetime.datetime.today().year

    lastDay = calendar.monthrange(year, month)[1]

    startDate = str(year) + '-' + str(month) + '-' + '01'
    endDate = str(year) + '-' + str(month) + '-' + str(lastDay)

    qryCat = "SELECT category, SUM(price) FROM public.expenses WHERE date >= '" + \
        startDate+"' and date <= '" + endDate + "' GROUP by 1"
    dataCat = db.engine.execute(qryCat)

    qryCard = "SELECT card, SUM(price) FROM public.expenses WHERE date >= '" + \
        startDate+"' and date <= '" + endDate + "' GROUP by 1"
    dataCard = db.engine.execute(qryCard)

    qryMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE  category not like 'INCOME' and category not like 'CREDIT CARD' and date > '2018-12-31' GROUP by 1, 2 ORDER by 2, 1"
    monthTotal = db.engine.execute(qryMonthWise)

    qryCreditCardMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'CREDIT CARD' GROUP by 1, 2 ORDER by 2, 1"
    CreditCardMonthTotal = db.engine.execute(qryCreditCardMonthWise)

    qryUtilitiesMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'UTILITIES' GROUP by 1, 2 ORDER by 2, 1"
    UtilitiesMonthTotal = db.engine.execute(qryUtilitiesMonthWise)

    qryGroceriesMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'GROCERIES' GROUP by 1, 2 ORDER by 2, 1"
    GroceriesMonthTotal = db.engine.execute(qryGroceriesMonthWise)

    qryRestaurantsMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'RESTAURANTS' GROUP by 1, 2 ORDER by 2, 1"
    RestaurantsMonthTotal = db.engine.execute(qryRestaurantsMonthWise)

    qrySubscriptionsMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'SUBSCRIPTIONS' GROUP by 1, 2 ORDER by 2, 1"
    SubscriptionsMonthTotal = db.engine.execute(qrySubscriptionsMonthWise)

    qryShoppingMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'SHOPPING' GROUP by 1, 2 ORDER by 2, 1"
    ShoppingMonthTotal = db.engine.execute(qryShoppingMonthWise)

    qryEntertainmentMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'ENTERTAINMENT' GROUP by 1, 2 ORDER by 2, 1"
    EntertainmentMonthTotal = db.engine.execute(qryEntertainmentMonthWise)

    qryTravelMonthWise = "SELECT extract(month from date), extract(year from date) as yyyy, SUM(price) FROM public.expenses WHERE date > '2018-12-31' and category = 'TRAVEL' GROUP by 1, 2 ORDER by 2, 1"
    TravelMonthTotal = db.engine.execute(qryTravelMonthWise)

    monthResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in monthTotal
    ]

    monthShoppingResults = [

        {
            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in ShoppingMonthTotal
    ]

    monthCreditCardResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in CreditCardMonthTotal
    ]

    monthEntertainmentResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in EntertainmentMonthTotal
    ]

    monthTravelResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in TravelMonthTotal
    ]

    monthUtilitiesResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in UtilitiesMonthTotal
    ]

    monthRestaurantsResults = [

        {

            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in RestaurantsMonthTotal
    ]

    monthGroceriesResults = [

        {
            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in GroceriesMonthTotal
    ]

    monthSubscriptionsResults = [

        {
            "month": str("%02d" % (int(row[0])),) + "/" + str(int(row[1]))[-2:],
            "total": round(row[2], 2)
        } for row in SubscriptionsMonthTotal
    ]
    cardResults = [
        {
            "card": row[0],
            "total": round(row[1], 2)
        } for row in dataCard]

    catResults = [
        {
            "category": row[0],
            "total": round(row[1], 2)
        } for row in dataCat]

    return{"CurrentCategoryTotal": catResults, "CurrentCardTotal": cardResults, "AllMonthTotal": monthResults, "AllCreditCardTotal": monthCreditCardResults, "AllEntertainmentTotal": monthEntertainmentResults, "AllTravelTotal": monthTravelResults, "AllShoppingTotal": monthShoppingResults, "AllSubscriptionsTotal": monthSubscriptionsResults, "AllRestaurantsTotal": monthRestaurantsResults, "AllUtilitiesTotal": monthUtilitiesResults, "AllGroceriesTotal": monthGroceriesResults}


@app.route("/getBankSplits", methods=['GET'])
def get_Monthdata():
    import datetime
    import calendar
    month = datetime.datetime.today().month
    year = datetime.datetime.today().year

    lastDay = calendar.monthrange(year, month)[1]

    startDate = str(year) + '-' + str(month) + '-' + '01'
    endDate = str(year) + '-' + str(month) + '-' + str(lastDay)

    allExpenses = expenses.query.all()
    # retrieving input from the front end with element name tag as

    sumMonth = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumMonth')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category != 'INCOME').filter(expenses.category != 'CREDIT CARD')
    # Get Citi Credit Card Total
    sumCiti = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumCiti')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'CITI CREDIT CARD').filter(expenses.category != 'CREDIT CARD')

    # Get Bofa Credit Card Total
    sumBofaCr = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumBofaCr')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'BOFA CREDIT CARD').filter(expenses.category != 'CREDIT CARD')

    # Get Bofa Checking Total
    sumBofaChk = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumBofaChk')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'BOFA CHECKING')

    # Get Marriott Chase Card Total
    sumMarriottChase = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumMarriottChase')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'MARRIOTT CREDIT CARD').filter(expenses.category != 'CREDIT CARD')

    # Get Chase Credit Card Total
    sumChaseCr = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumChaseCr')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'CHASE CREDIT CARD').filter(expenses.category != 'CREDIT CARD')

    # Get Discover Credit Card Total
    sumDiscoverCr = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumDiscoverCr')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'DISCOVER CREDIT CARD').filter(expenses.category != 'CREDIT CARD')

    # Get DCU Checking Total
    sumDCUChk = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumDCUChk')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'DCU CHECKING').filter(expenses.category != 'INCOME')

    # Get Discover Savings Total
    sumDiscoverSavings = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumDiscoverSavings')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.card == 'DISCOVER SAVINGS')

    sumUtilities = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumUtilities')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'UTILITIES')

    sumRestaurants = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumRestaurants')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'RESTAURANTS')

    sumTravel = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumTravel')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'TRAVEL')

    sumGroceries = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumGroceries')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'GROCERIES')

    sumSubscriptions = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumSubscriptions')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'SUBSCRIPTIONS')

    sumShopping = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumShopping')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'SHOPPING')

    sumEntertainment = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumEntertainment')).filter(expenses.date >= startDate).filter(expenses.date <= endDate).filter(expenses.category == 'ENTERTAINMENT')

    # Get sum of previou month
    lastDayPrev = calendar.monthrange(year, month - 1)[1]
    prevMonth = month - 1
    startDatePrev = str(year) + '-' + str(prevMonth) + '-' + '01'
    endDatePrev = str(year) + '-' + str(prevMonth) + '-' + str(lastDayPrev)

    sumUtilitiesPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumUtilitiesPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'UTILITIES')

    sumRestaurantsPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumRestaurantsPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'RESTAURANTS')

    sumTravelPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumTravelPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'TRAVEL')

    sumGroceriesPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumGroceriesPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'GROCERIES')

    sumSubscriptionsPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumSubscriptionsPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'SUBSCRIPTIONS')

    sumShoppingPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumShoppingPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'SHOPPING')

    sumEntertainmentPrev = expenses.query.with_entities(func.sum(expenses.price).label(
        'sumEntertainmentPrev')).filter(expenses.date >= startDatePrev).filter(expenses.date <= endDatePrev).filter(expenses.category == 'ENTERTAINMENT')

    for sumUtilityPrev in sumUtilitiesPrev:
        sumUtilitiesPrev = sumUtilityPrev.sumUtilitiesPrev
        if sumUtilitiesPrev is None:
            sumUtilitiesPrev = 0
        else:
            sumUtilitiesPrev = round(sumUtilitiesPrev, 2)

    for sumRestaurantPrev in sumRestaurantsPrev:
        sumRestaurantsPrev = sumRestaurantPrev.sumRestaurantsPrev
        if sumRestaurantsPrev is None:
            sumRestaurantsPrev = 0
        else:
            sumRestaurantsPrev = round(sumRestaurantsPrev, 2)

    for sumTravPrev in sumTravelPrev:
        sumTravelPrev = sumTravPrev.sumTravelPrev
        if sumTravelPrev is None:
            sumTravelPrev = 0
        else:
            sumTravelPrev = round(sumTravelPrev, 2)

    for sumGroceryPrev in sumGroceriesPrev:
        sumGroceriesPrev = sumGroceryPrev.sumGroceriesPrev
        if sumGroceriesPrev is None:
            sumGroceriesPrev = 0
        else:
            sumGroceriesPrev = round(sumGroceriesPrev, 2)

    for sumSubscriptionPrev in sumSubscriptionsPrev:
        sumSubscriptionsPrev = sumSubscriptionPrev.sumSubscriptionsPrev
        if sumSubscriptionsPrev is None:
            sumSubscriptionsPrev = 0
        else:
            sumSubscriptionsPrev = round(sumSubscriptionsPrev, 2)

    for sumShopPrev in sumShoppingPrev:
        sumShoppingPrev = sumShopPrev.sumShoppingPrev
        if sumShoppingPrev is None:
            sumShoppingPrev = 0
        else:
            sumShoppingPrev = round(sumShoppingPrev, 2)

    for sumEntertain in sumEntertainmentPrev:
        sumEntertainmentPrev = sumEntertain.sumEntertainmentPrev
        if sumEntertainmentPrev is None:
            sumEntertainmentPrev = 0
        else:
            sumEntertainmentPrev = round(sumEntertainmentPrev, 2)

    for sumMonth in sumMonth:
        sumMonth = sumMonth.sumMonth
        if sumMonth is None:
            sumMonth = 0
        else:
            sumMonth = round(sumMonth, 2)

    for sumUtility in sumUtilities:
        sumUtilities = sumUtility.sumUtilities
        if sumUtilities is None:
            sumUtilities = 0
        else:
            sumUtilities = round(sumUtilities, 2)

    for sumGrocery in sumGroceries:
        sumGroceries = sumGrocery.sumGroceries
        if sumGroceries is None:
            sumGroceries = 0
        else:
            sumGroceries = round(sumGroceries, 2)

    for sumSubscription in sumSubscriptions:
        sumSubscriptions = sumSubscription.sumSubscriptions
        if sumSubscriptions is None:
            sumSubscriptions = 0
        else:
            sumSubscriptions = round(sumSubscriptions, 2)

    for sumEntertain in sumEntertainment:
        sumEntertainment = sumEntertain.sumEntertainment
        if sumEntertainment is None:
            sumEntertainment = 0
        else:
            sumEntertainment = round(sumEntertainment, 2)

    for sumShop in sumShopping:
        sumShopping = sumShop.sumShopping
        if sumShopping is None:
            sumShopping = 0
        else:
            sumShopping = round(sumShopping, 2)

    for sumTrav in sumTravel:
        sumTravel = sumTrav.sumTravel
        if sumTravel is None:
            sumTravel = 0
        else:
            sumTravel = round(sumTravel, 2)

    for sumRestaurant in sumRestaurants:
        sumRestaurants = sumRestaurant.sumRestaurants
        if sumRestaurants is None:
            sumRestaurants = 0
        else:
            sumRestaurants = round(sumRestaurants, 2)

    for citi in sumCiti:
        sumCity = citi.sumCiti
        if sumCity is None:
            sumCity = 0
        else:
            sumCity = round(sumCity, 2)
    for DCUChk in sumDCUChk:
        sumDCUChk = DCUChk.sumDCUChk
        if sumDCUChk is None:
            sumDCUChk = 0
        else:
            sumDCUChk = round(sumDCUChk, 2)
    for BofaCr in sumBofaCr:
        sumBofaCr = BofaCr.sumBofaCr
        if sumBofaCr is None:
            sumBofaCr = 0
        else:
            sumBofaCr = round(sumBofaCr, 2)
    for BofaChk in sumBofaChk:
        sumBofaChk = BofaChk.sumBofaChk
        if sumBofaChk is None:
            sumBofaChk = 0
        else:
            sumBofaChk = round(sumBofaChk, 2)
    for MarriottChase in sumMarriottChase:
        sumMarriottChase = MarriottChase.sumMarriottChase
        if sumMarriottChase is None:
            sumMarriottChase = 0
        else:
            sumMarriottChase = round(sumMarriottChase, 2)
    for ChaseCredit in sumChaseCr:
        sumChaseCr = ChaseCredit.sumChaseCr
        if sumChaseCr is None:
            sumChaseCr = 0
        else:
            sumChaseCr = round(sumChaseCr, 2)
    for DiscoverSavings in sumDiscoverSavings:
        sumDiscoverSavings = DiscoverSavings.sumDiscoverSavings
        if sumDiscoverSavings is None:
            sumDiscoverSavings = 0
        else:
            sumDiscoverSavings = round(sumDiscoverSavings, 2)
    for DiscoverCr in sumDiscoverCr:
        sumDiscoverCr = DiscoverCr.sumDiscoverCr
        if sumDiscoverCr is None:
            sumDiscoverCr = 0
        else:
            sumDiscoverCr = round(DiscoverCr.sumDiscoverCr, 2)

    # resultsDisocverSavings,:
    return {"PrevMonthTotal": [{"UtilitiesPrev": sumUtilitiesPrev,
                                "RestaurantsPrev": sumRestaurantsPrev,
                                "GroceriesPrev": sumGroceriesPrev,
                                "TravelPrev": sumTravelPrev,
                                "EntertainmentPrev": sumEntertainmentPrev,
                                "ShoppingPrev": sumShoppingPrev,
                                "SubscriptionsPrev": sumSubscriptionsPrev}],

            "Total": [{"MonthlyTotal": sumMonth}],
            "TotalCard": [{"CitiCreditCard": sumCity,
                           "DCUChecking": sumDCUChk,
                           "BofaCreditCard": sumBofaCr,
                           "BofaCheckingAccount": sumBofaChk,
                           "MarriottCreditCard": sumMarriottChase,
                           "ChaseCreditCard": sumChaseCr,
                           "DiscoverSavings": sumDiscoverSavings,
                           "DiscoverCreditCard": sumDiscoverCr
                           }],
            "TotalCategory": [{"Utilities": sumUtilities,
                               "Entertainment": sumEntertainment,
                               "Groceries": sumGroceries,
                               "Subscriptions": sumSubscriptions,
                               "Travel": sumTravel,
                               "Shopping": sumShopping,
                               "Restaurants": sumRestaurants
                               }]

            }


if __name__ == '__main__':
    app.run()
