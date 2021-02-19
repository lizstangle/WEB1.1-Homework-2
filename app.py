from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_toppings = request.args.get('toppings')

    context = {
            'users_froyo_flavor': users_froyo_flavor,
            'users_toppings': users_toppings
        }

    return render_template('froyo_results.html', **context)
    
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')
    return f"Wow, I didn't know {users_favorite_color} {users_favorite_animal} lived in {users_favorite_city}."

@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        What is your secret message? <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""

@app.route('/message_results', methods=['POST'])
def message_results():
    users_secret_message = request.form.get('message')
    new_message = sort_letters(users_secret_message)
    """Shows the user their message, with the letters in sorted order."""
    return(f"{new_message}")

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')
    

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    users_num_1 = int(request.args.get('operand1')) 
    users_operation = request.args.get('operation')   
    users_num_2 = int(request.args.get('operand2')) 
    if users_operation == 'add':
        result = int(users_num_1 ) + int(users_num_2)
    elif users_operation == 'subtract':
        result = int(users_num_1 ) - int(users_num_2)
    elif users_operation == 'multiply':
        result = int(users_num_1 ) * int(users_num_2)
    else:
        result = int(users_num_1 ) / int(users_num_2)
    context = {
        'users_num_1': users_num_1,
        'users_num_2': users_num_2,
        'users_operation': users_operation,
        'result': result
    }
    return render_template('calculator_results.html', **context)

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]
    
    users_name = request.args.get('users_name')

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
