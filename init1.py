#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib
from datetime import datetime, timedelta

# Random and string are used to generate a ticket number
import random
import string



#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='MasterFlight',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# Ticket ID Global Variable: Need to put it where flights are being created

#Define route for Customer login
@app.route('/login')
def login():
	return render_template('login.html')

#Define route for Staff login
@app.route('/stafflogin')
def stafflogin():
	return render_template('stafflogin.html')

#Define route for Customer registration
@app.route('/register')
def register():
	return render_template('register.html')

#Define route for Staff registration
@app.route('/staffregister')
def staffregister():
	return render_template('staffregister.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
	error = None
	customer_name = None
	e_mail = request.form.get("Email")
	password = request.form.get("Password")

	cursor = conn.cursor()
	
	query = 'SELECT * FROM customer WHERE e_mail = %s and password = %s'
	name_query = 'SELECT first_name FROM customer WHERE e_mail = %s and password = %s'
	password = hashlib.md5(password.encode()).hexdigest()[0:20]
	cursor.execute(query, (e_mail, password))
	data = cursor.fetchone()

	cursor.execute(name_query,(e_mail, password))
	name_cursor = cursor.fetchone()

	if (name_cursor):
		customer_name = name_cursor["first_name"] 
	cursor.close()
	
	if(data):
		if (name_cursor):
			session['First Name'] = customer_name
			session["e_mail"] = e_mail
			return redirect(url_for('home'))
	else:
		error = 'Invalid information. Please try again'
		return render_template('login.html', error=error)
#LOL	
#Authenticates the Staff login
@app.route('/StaffLoginAuth', methods=['GET', 'POST'])
def StaffLoginAuth():
	username = request.form["Username"]
	password = request.form["Password"]
	password = hashlib.md5(password.encode()).hexdigest()[0:20]
	cursor = conn.cursor()
	query = 'SELECT * FROM airline_staff WHERE username = %s and password = %s'
	name_query = 'SELECT first_name FROM airline_staff WHERE username = %s and password = %s'

	cursor.execute(query, (username, password))
	
	#stores the results in a variable
	data = cursor.fetchone()

	cursor.execute(name_query,(username, password))

	name_cursor = cursor.fetchone()

	if (name_cursor):
		staff_name = name_cursor["first_name"] 

	session["username"] = username
	cursor.close()
	error = None
	if(data):
		session['First Name'] = staff_name
		return redirect(url_for('staffhome'))
	else:
		error = 'Invalid information. Please try again'
		return render_template('stafflogin.html', error=error)


#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():

	e_mail = request.form["Email"]
	first_name = request.form['First Name']
	last_name = request.form['Last Name']
	password = request.form['Password']
	building_num = request.form["Building Number"]
	street_name = request.form["Street Name"]
	apt_num = request.form["Apartment Number"]
	city = request.form["City"]
	state = request.form["State"]
	zip_code = request.form["Zip Code"]

	password = hashlib.md5(password.encode()).hexdigest()[0:20]


	cursor = conn.cursor()
	#executes query

	query = 'SELECT * FROM customer WHERE e_mail = %s and first_name = %s and last_name = %s and password = %s and building_num = %s and street_name = %s and apt_num = %s and city = %s and state = %s and zip_code = %s'

	cursor.execute(query, (e_mail, first_name, last_name, password, building_num, street_name, apt_num, city, state, zip_code))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This customer already exists"
		return render_template('register.html', error = error)
	else:
		ins = 'INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (e_mail, first_name, last_name, password, building_num, street_name, apt_num, city, state, zip_code))
		conn.commit()
		cursor.close()
		return render_template('index.html')
	

#Authenticates the Airline Staff
@app.route('/StaffRegisterAuth', methods=['GET', 'POST'])
def StaffRegisterAuth():

	username = request.form["Username"]
	airline_name = request.form["Airline Name"]
	password = request.form["Password"]
	first_name = request.form["First Name"]
	last_name = request.form["Last Name"]
	date_of_birth = request.form["DOB"]

	password = hashlib.md5(password.encode()).hexdigest()[0:20]

	cursor = conn.cursor()
	query = 'SELECT* FROM airline_staff WHERE username = %s and airline_name = %s and password = %s and first_name = %s and last_name = %s and date_of_birth = %s'
	cursor.execute(query, (username, airline_name, password, first_name, last_name, date_of_birth))
	data = cursor.fetchone()
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This staff already exists"
		return render_template('staffregister.html', error = error)
	else:
		ins = 'INSERT INTO airline_staff VALUES(%s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (username, airline_name, password, first_name, last_name, date_of_birth))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	flight_data = None
	return_error = None
	return_flights = None
	all_airport_data = None
	cursor = conn.cursor()
	all_airport_query =  "SELECT code FROM airport"
	cursor.execute(all_airport_query)
	all_airport_data = cursor.fetchall()

	

	if (request.method == "POST"):
		departure_airport = request.form.get("departure_airport")
		arrival_airport = request.form.get("arrival_airport")

		# Query for future flights
		flight_query = "SELECT status, airline_name, flight_num, departure_date, arrival_date FROM flight WHERE departure_airport = %s and arrival_airport = %s and departure_date > NOW()"

		cursor.execute(flight_query, (departure_airport, arrival_airport))

		flight_data = cursor.fetchall()
		return_flights = None
	
		return_query = "SELECT status, airline_name, flight_num, departure_date, arrival_date FROM flight WHERE departure_date > ALL (SELECT departure_date FROM flight WHERE departure_airport = %s and arrival_airport = %s)"
		cursor.execute(return_query, (departure_airport, arrival_airport))
		return_flights = cursor.fetchall()
		if(not return_flights):
			return_error = "No return flights were found. Please try again"

		if(not flight_data):
			error = "No flights were found. Please try again"

	return render_template("index.html", error = error, all_airport_data = all_airport_data, flight_data = flight_data, return_error = return_error, return_flights = return_flights)

generated_digits = set()
max_value = 1000
def generate_unique_digit():
	global max_value
	if len(generated_digits) == max_value:
		max_value *= 2

	unique_digit = random.randint(0, max_value)
	while unique_digit in generated_digits:
		unique_digit = random.randint(0, max_value)

	generated_digits.add(unique_digit)
	return unique_digit

@app.route("/staffhome", methods=['GET', 'POST'])
def staffhome():

	staff_name = session.get("First Name", None)
	username = session.get("username", None)

	cursor = conn.cursor()
	airline_name = None
	airline_error = None
	past_flight_error = None
	error = None

	view_flight_data = None
	past_flight_data = None
	airplane_id_data = None
	
	if username:
		airline_name_query = "SELECT airline_name FROM airline_staff WHERE username = %s"
		cursor.execute(airline_name_query, (username))
		airline_name_data = cursor.fetchone()

		if (airline_name_data):
			airline_name = airline_name_data["airline_name"]
			session["airline_name"] = airline_name
		else:
			airline_error ="No corresponding airline found"

	if airline_name:
		view_flight_query = "SELECT distinct flight_num, status, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport FROM flight natural join airline_staff WHERE airline_name = %s AND DATEDIFF(departure_date, CURDATE()) BETWEEN 0 AND 30;"
		cursor.execute(view_flight_query, (airline_name))
		view_flight_data = cursor.fetchall()
		
		airplane_id_query = "SELECT airplane_id FROM airplane WHERE airline_name = %s"
		cursor.execute(airplane_id_query, (airline_name))
		airplane_id_data = cursor.fetchall()

		# select flight num of past flight of airline company
		past_flight_query = "SELECT flight_num FROM flight WHERE airline_name = %s and arrival_date < NOW()"
		cursor.execute(past_flight_query, (airline_name))
		past_flight_data = cursor.fetchall()

		if (not past_flight_data):
			past_flight_error = "No past flights were found for your airline"
	

	if(not view_flight_data):
		error = "Flight not found within 30 days"


	airport_code = "SELECT code from airport"
	cursor.execute(airport_code)
	airport_data = cursor.fetchall()

	if request.method == "POST":
		if "Submit" in request.form:
			unique_flight_num = generate_unique_digit()
			base_price = request.form["base_price"]
			status = request.form["status"]
			departure_time = request.form["departure_time"]
			departure_date = request.form["departure_date"]
			arrival_time = request.form["arrival_time"]
			arrival_date = request.form["arrival_date"]
			departure_airport = request.form["departure_airport"]
			airplane_id = request.form["airplane_id"]
			arrival_airport = request.form["arrival_airport"]
			create_flight_query = "INSERT into flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

			cursor.execute(create_flight_query, (unique_flight_num, base_price, status, departure_time, departure_date, arrival_time, arrival_date, departure_airport, airplane_id, airline_name, arrival_airport))
			conn.commit()
			return redirect(url_for("staffhome"))

		elif "change_status" in request.form:
			new_status = request.form["new_status"]
			flight_num = request.form["flight_num"]
			update_status_query = "UPDATE flight SET status = %s WHERE flight_num = %s"
			cursor.execute(update_status_query, (new_status, flight_num))
			conn.commit()
			return redirect(url_for("staffhome"))

		elif "add_airplane" in request.form:
			airplane_id = generate_ticket_id()
			num_seats = request.form["num_seats"]
			manufact_comp = request.form["manufact_comp"]
			manufact_date = request.form["manufact_date"]

			add_airplane_query = "INSERT into airplane VALUES(%s, %s, %s, %s, %s)"
			cursor.execute(add_airplane_query, (airplane_id, num_seats, manufact_comp, manufact_date, airline_name))
			conn.commit()
			return redirect(url_for("airplane_list"))
		
		elif "add_airport" in request.form:
			code = request.form["code"]
			airport_name = request.form["airport_name"]
			city = request.form["city"]
			country = request.form["country"]
			airport_type = request.form["airport_type"]

			add_airport_query = "INSERT into airport VALUES(%s, %s, %s, %s, %s)"
			cursor.execute(add_airport_query, (code, airport_name, city, country, airport_type))
			conn.commit()
			return redirect(url_for("staffhome"))
		
		elif "view_flight_rating" in request.form:
			flight_num = request.form["flight_num"]
			session["flight_num"] = flight_num
			return redirect(url_for("flight_rating"))
		
		elif "view_freq_cus" in request.form:
			return redirect(url_for("frequent_customer"))

		elif "view_report" in request.form:
			return redirect(url_for("report"))
		
		elif "view_rev" in request.form:
			return redirect(url_for("revenue"))


	return render_template("staffhome.html", airport_data = airport_data, staff_name = staff_name, view_flight_data = view_flight_data, past_flight_data = past_flight_data, error = error, past_flight_error = past_flight_error, airline_error = airline_error, airplane_id_data = airplane_id_data)


@app.route('/airplane_list', methods=['GET', 'POST'])
def airplane_list():

	username = session["username"]

	cursor = conn.cursor()

	airline_name_query = "SELECT airline_name FROM airline_staff WHERE username = %s"
	cursor.execute(airline_name_query, (username))
	airline_name_data = cursor.fetchone()
	airline_name = airline_name_data["airline_name"]
	
	airplane_list_query = "Select airplane_id, num_seats, Manufacturing_comp, Manufacturing_date from airplane where airline_name = %s"
	cursor.execute(airplane_list_query, (airline_name))
	airplane_list_data = cursor.fetchall()

	return render_template("airplane_list.html", airplane_list_data = airplane_list_data) 

@app.route("/flight_rating", methods=["GET", "POST"])
def flight_rating():

	cursor = conn.cursor()	
	flight_num = session["flight_num"]
	view_rating_query = "SELECT rate, comments FROM review WHERE flight_num = %s"
	cursor.execute(view_rating_query, (flight_num))
	view_rating_data = cursor.fetchall()
	avg_rating_query = "SELECT AVG(rate) FROM review WHERE flight_num = %s"
	cursor.execute(avg_rating_query, (flight_num))
	avg_rating_data = cursor.fetchone()
	avg_rating = avg_rating_data["AVG(rate)"]

	error = None
	if (not view_rating_data):
		error = "No ratings available for this flight"

	return render_template("flight_rating.html", view_rating_data = view_rating_data, avg_rating = avg_rating, error = error)



@app.route("/frequent_customer", methods=["GET", "POST"])
def frequent_customer():
	airline_name = session["airline_name"]
	cursor = conn.cursor()
	freq_cus_query = "SELECT COUNT(ticket_id) as num_ticket, e_mail, first_name, last_name FROM customer natural join purchase natural join ticket natural join flight natural join airline WHERE airline_name = %s GROUP BY e_mail ORDER by COUNT(ticket_id) DESC"
	cursor.execute(freq_cus_query, (airline_name))
	freq_cus_data = cursor.fetchall()
	customer_error = None
	if (not freq_cus_data):
		customer_error = "No frequent customers were found"
	return render_template("frequent_customer.html", freq_cus_data = freq_cus_data, customer_error = customer_error)


@app.route("/report", methods=["GET", "POST"])
def report():
	report_error = None
	date_report = None
	date_diff = None
	report = None

	if (request.method == "POST"):
		date_report_str = request.form["time_range"]
		date_report = datetime.strptime(date_report_str, "%Y-%m-%d").date()
		airline_name = session["airline_name"]
		cursor = conn.cursor()

		current_date = datetime.now().date()

		date_diff = (current_date - date_report).days
		
		report_query = "SELECT COUNT(ticket_id) FROM purchase natural join ticket natural join flight WHERE airline_name = %s and purchase_date BETWEEN %s and NOW()"		
		cursor.execute(report_query, (airline_name, date_report))
		report_data = cursor.fetchone()


		if (not report_data):
			report_error = "No sold tickets were found. Please select another day"
		else:
			report = report_data["COUNT(ticket_id)"]

	return render_template("report.html", report = report, report_error = report_error, date_diff = date_diff)


@app.route("/revenue", methods=["GET", "POST"])
def revenue():
	revenue_data_30 = None
	revenue_data_365 = None
	cursor = conn.cursor()
	airline_name = session["airline_name"]
	
	revenue_query_30 = "SELECT SUM(ticket_price) FROM purchase natural join ticket natural join flight WHERE airline_name = %s and purchase_date BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW()"
	cursor.execute(revenue_query_30, (airline_name))
	revenue_data_30 = cursor.fetchone()
	revenue_data_30 = revenue_data_30["SUM(ticket_price)"]

	revenue_query_365 = "SELECT SUM(ticket_price) FROM purchase natural join ticket natural join flight WHERE airline_name = %s and purchase_date BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW()"
	cursor.execute(revenue_query_365, (airline_name))
	revenue_data_365 = cursor.fetchone()
	revenue_data_365 = revenue_data_365["SUM(ticket_price)"]

	if (not revenue_data_30):
		revenue_data_30 = 0
	if (not revenue_data_365):
		revenue_data_365 = 0

			
	return render_template("revenue.html", revenue_data_30 = revenue_data_30, revenue_data_365 = revenue_data_365)


@app.route('/home', methods=['GET', 'POST'])
def home():
	all_airport_data = None
	e_mail = session["e_mail"]


	return_error = None
	flight_num = None
	num_seats = None

	first_name = session['First Name']
	cursor = conn.cursor()
	flight_num_query = "SELECT flight_num FROM flight natural join ticket natural join purchase natural join customer WHERE customer.e_mail = %s"

	view_flight_query = "SELECT ticket.flight_num, flight.airline_name, flight.departure_time, flight.departure_date, flight.departure_airport, flight.arrival_airport, ticket.ticket_id FROM flight natural join ticket natural join purchase natural join customer WHERE e_mail = %s"
	
	cursor.execute(view_flight_query, (e_mail))
	view_flight_data = cursor.fetchall()
	
	cursor.execute(flight_num_query, (e_mail))
	flight_num_data = cursor.fetchall()

	all_airport_query =  "SELECT code FROM airport"
	cursor.execute(all_airport_query)
	all_airport_data = cursor.fetchall()
	
	if flight_num_data:
		flight_num = flight_num_data[0]["flight_num"]
		num_seat_query = "SELECT num_seats FROM airplane natural join flight where flight_num = %s"
		cursor.execute(num_seat_query, (flight_num))
		num_seat_data = cursor.fetchone()

		num_seats = num_seat_data["num_seats"]

		num_ticket_query = "SELECT COUNT(ticket_id) FROM ticket WHERE flight_num = %s"
		cursor.execute(num_ticket_query, (flight_num))

		num_ticket_data = cursor.fetchone()
		num_ticket = num_ticket_data['COUNT(ticket_id)']


	future_flight_data = None
	return_flights_data = None
	return_num_ticket = None
	return_num_seat_data = None
	error = None
	delete_error = None
	comment_error = None
	if request.method == 'POST':
		if "Submit" in request.form:
			departure_airport = request.form["departure_airport"]
			arrival_airport = request.form["arrival_airport"]
			future_flight_query = "SELECT status, airline_name, flight_num, departure_date, arrival_date, base_price FROM flight WHERE departure_airport = %s and arrival_airport = %s and departure_date > NOW()"
			cursor.execute(future_flight_query, (departure_airport, arrival_airport))
			future_flight_data = cursor.fetchall()

			session["future_flight_data"] = future_flight_data

			return_flights_query = "SELECT status, airline_name, flight_num, departure_date, arrival_date, base_price FROM flight WHERE departure_date > ALL (SELECT departure_date FROM flight WHERE departure_airport = %s and arrival_airport = %s)"
			cursor.execute(return_flights_query, (departure_airport, arrival_airport))
			return_flights_data = cursor.fetchall()


			return_num_seats = None
			if return_flights_data:
					session["return_flight_data"] = return_flights_data
					return_flight_num = return_flights_data[0]["flight_num"]
					return_num_seat_query = "SELECT num_seats FROM airplane natural join flight WHERE flight_num = %s"
					cursor.execute(return_num_seat_query, (return_flight_num))
					return_num_seat_data = cursor.fetchone()
				
					if return_num_seat_data:
						return_num_seats = return_num_seat_data["num_seats"]

						return_num_ticket_query = "SELECT COUNT(ticket_id) FROM ticket WHERE flight_num = %s"
						cursor.execute(return_num_ticket_query, (return_flight_num))

						return_num_ticket_data = cursor.fetchone()
						return_num_ticket = return_num_ticket_data['COUNT(ticket_id)']
						for i in range(len(return_flights_data)):
							if int(return_num_seats) * 0.8 < int(return_num_ticket):
								(return_flights_data[i]["base_price"]) *= 1.25
							else:
								return_flights_data[i]["base_price"] *= 1.10

			if(not return_flights_data):
				return_error = "No return flights were found."

			if num_seats:
				for i in range(len(future_flight_data)):
					if int(num_seats) * 0.8 < int(num_ticket):
						(future_flight_data[i]["base_price"]) *= 1.25
					else:
						future_flight_data[i]["base_price"] *= 1.10


			session["flight_data"] = future_flight_data

		if "Delete" in request.form:
			ticket_id = request.form["Ticket ID"]
			purchase_date_query = "SELECT purchase_date FROM purchase WHERE ticket_id = %s"
			cursor.execute(purchase_date_query, (ticket_id))
			purchase_date_data = cursor.fetchone()
			purchase_date = purchase_date_data["purchase_date"]

			purchase_time_query = "SELECT purchase_time FROM purchase WHERE ticket_id = %s"
			cursor.execute(purchase_time_query, (ticket_id))
			purchase_time_data = cursor.fetchone()
			purchase_time = purchase_time_data["purchase_time"]

			current_date = datetime.now().date()

			if (current_date - purchase_date < timedelta(days=1)):
				delete_flight_query = "DELETE FROM purchase where ticket_id = %s"
				cursor.execute(delete_flight_query, (ticket_id))
				conn.commit()

				delete_ticket_query = "DELETE FROM ticket where ticket_id = %s"
				cursor.execute(delete_ticket_query, (ticket_id))
				conn.commit()
				return redirect(url_for('home'))
			else: 
				delete_error = "Cannot delete flight because ticket has been purchased more than 24 hours ago"

		if "Review" in request.form:
			current_date = datetime.now().date()
			rate = request.form["Rate"]
			comment = request.form["commentSection"]
			e_mail = session["e_mail"]
			flight_num = request.form["Number Flight"]

			arrival_date_query = "SELECT arrival_date FROM flight WHERE flight_num = %s"
			cursor.execute(arrival_date_query, (flight_num))
			arrival_date_data = cursor.fetchone()
			arrival_date = arrival_date_data["arrival_date"]

			check_review_query = "SELECT flight_num FROM review WHERE flight_num = %s and e_mail = %s"
			cursor.execute(check_review_query, (flight_num, e_mail))
			check_review_data = cursor.fetchone()
			check_review = None

			if (check_review_data):
				check_review = check_review_data["flight_num"]

			if(not check_review):
				if(current_date - arrival_date > timedelta(days=0)):
					rating_query = "INSERT into review VALUES(%s, %s, %s, %s)"
					cursor.execute(rating_query, (e_mail, flight_num, rate, comment))
					conn.commit()
					return redirect(url_for('home'))
				else:
					comment_error = "Cannot rate flight yet. Wait for the flight to happen first"
			else:
				comment_error = "Already rated the flight."

		if "spending_submit" in request.form:
			return redirect(url_for("spending"))

	if not view_flight_data and not future_flight_data:
		error = "No flights were found. Please try again"


	return render_template("home.html", first_name = first_name, return_flights_data = return_flights_data, view_flight_data= view_flight_data, future_flight_data = future_flight_data, all_airport_data = all_airport_data, error = error, delete_error = delete_error, comment_error = comment_error, return_error = return_error)

@app.route("/spending", methods={"GET", "POST"})
def spending():
	period_data = None
	month_data = None
	year_data = None

	cursor = conn.cursor()
	period1 = request.form.get("period1")
	period2 = request.form.get("period2")
	e_mail = session["e_mail"]

	month_query =  "SELECT SUM(ticket_price) FROM customer natural join purchase natural join ticket WHERE e_mail = %s and purchase_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 180 DAY) AND CURDATE()"
	cursor.execute(month_query, (e_mail))
	month_data = cursor.fetchone()
	month_data = month_data["SUM(ticket_price)"]

	year_query = "SELECT SUM(ticket_price) FROM customer natural join purchase natural join ticket WHERE e_mail = %s and purchase_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 365 DAY) AND CURDATE()"
	cursor.execute(year_query, (e_mail))
	year_data = cursor.fetchone()
	year_data = year_data["SUM(ticket_price)"]

	if request.method == "POST":
		period_query = "SELECT SUM(ticket_price) FROM customer natural join purchase natural join ticket WHERE e_mail = %s and purchase_date BETWEEN %s and %s"
		cursor.execute(period_query, (e_mail, period1, period2))
		period_data = cursor.fetchone()
		period_data = period_data["SUM(ticket_price)"]

	if (not month_data):
		#month_error = "No spending was found during the past 6 months"
		month_data = 0

	if (not year_data):
		#year_error = "No spending was found during the past 12 months"
		year_data = 0
	if (not period_data):
		period_data = 0

	return render_template("spending.html", month_data = month_data, year_data = year_data, period_data = period_data)


def generate_ticket_id(length=8):
    characters = string.ascii_letters + string.digits
    ticket_id = ''.join(random.choice(characters) for _ in range(length))
    return ticket_id


@app.route("/buy_flights", methods=["GET", "POST"])
def buy_flightsAuth():
	
	list_of_flights = session["future_flight_data"]
	return_flights = session["return_flight_data"]

	card_type = request.form.get("Card Type")
	name_on_card = request.form.get("Name on Card")
	expiration_date = request.form.get("Expiration Date")
	card_num = request.form.get("Card Number")
	flight_num = request.form.get("Flight Number")
	cursor = conn.cursor()

	for i in range(len(return_flights)):
		list_of_flights.append(return_flights[i])

	error = None
	if flight_num:
		base_price_query = "SELECT base_price FROM flight WHERE flight_num = %s"
		cursor.execute(base_price_query, (flight_num))
		base_price_data = cursor.fetchone()

		num_seat_query = "SELECT num_seats FROM airplane natural join flight where flight_num = %s"
		cursor.execute(num_seat_query, (flight_num))

		num_seat_data = cursor.fetchone()
		num_seats = num_seat_data["num_seats"]

		num_ticket_query = "SELECT COUNT(ticket_id) FROM ticket WHERE flight_num = %s"
		cursor.execute(num_ticket_query, (flight_num))

		num_ticket_data = cursor.fetchone()
		num_ticket = num_ticket_data['COUNT(ticket_id)']
		
		# checks if 80% of the number of seats is less than number of tickets
		ticket_price = 0
		if int(num_seats) * 0.8 < int(num_ticket):
			ticket_price = base_price_data["base_price"] * 1.25
		else:
			ticket_price = base_price_data["base_price"] * 1.10

		# Randomly generate a ticket
		ticket_id = generate_ticket_id()
		current_time = datetime.now().time()
		current_date = datetime.now().date()

		e_mail = session["e_mail"]
		
		
		if (num_seats != num_ticket):
			card_info_query = "INSERT into ticket VALUES (%s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(card_info_query, (ticket_id, flight_num, ticket_price, card_type, name_on_card, expiration_date, card_num))

			purchase_query = "INSERT into purchase VALUES(%s, %s, %s, %s)"
			cursor.execute(purchase_query, (e_mail, ticket_id, current_time, current_date))
		else:
			error = "Sorry, flight is fully booked"

	

		conn.commit()


	return render_template("buy_flights.html", error = error, list_of_flights = list_of_flights)

@app.route('/logout')
def logout():
	session.pop("e_mail", None)
	session.pop("username", None)
	session.pop('First Name', None)
	return redirect('/')
		
app.secret_key = 'some key that you will never guess'

#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION

if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
