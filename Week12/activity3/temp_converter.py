from flask import Flask, render_template, request

app = Flask(__name__)

# Define the conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the input temperature value and conversion type
        temp_value = float(request.form['temperature'])
        conversion_type = request.form['conversion_type']
        
        # Perform the conversion based on the enduser's selected type
        if conversion_type == 'Celsius to Fahrenheit':
            result = celsius_to_fahrenheit(temp_value)
            result_label = 'Fahrenheit'
        elif conversion_type == 'Fahrenheit to Celsius':
            result = fahrenheit_to_celsius(temp_value)
            result_label = 'Celsius'
        elif conversion_type == 'Celsius to Kelvin':
            result = celsius_to_kelvin(temp_value)
            result_label = 'Kelvin'
        elif conversion_type == 'Kelvin to Celsius':
            result = kelvin_to_celsius(temp_value)
            result_label = 'Celsius'
        elif conversion_type == 'Fahrenheit to Kelvin':
            result = fahrenheit_to_kelvin(temp_value)
            result_label = 'Kelvin'
        elif conversion_type == 'Kelvin to Fahrenheit':
            result = kelvin_to_fahrenheit(temp_value)
            result_label = 'Fahrenheit'
        else:
            result = None
            result_label = None

        return render_template('index.html', result=result, result_label=result_label, temp_value=temp_value, conversion_type=conversion_type)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
