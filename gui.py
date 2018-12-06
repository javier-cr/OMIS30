from flask import Flask, request
from game_for_gui import do_calculation
from game_for_gui import pick_user_case

app = Flask(__name__)
app.config["DEBUG"] = True #remove later

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        user_case_num = None
        try:
            user_case_num = int(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        
        if user_case_num is not None:
            ########
            result = pick_user_case(user_case_num)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
    
    
    return '''
        <html>
            <body>
                {errors}
                <h1>Welcome to Deal or No Deal!</h1>
                <h2>Created by Chris, Javi, Lily, and Tanner.</h2>
                <p>Choose a personal case. You may select a case numbered 1-26.
                <form method="post" action="/pickcase">
                    <p><input name="number1" /></p>
                    <p><input type="submit" value="Submit Case" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

@app.route("/pickcase", methods=["GET", "POST"])
def pickcase():
    return '''
        <html>
            <body>
                <h1>Great! You have selected your case.</h1>
                <h2> Your options are {options}.
                <p>Which case should be #xxxxx to eliminate?
                <form method="post" action="/pickcase">
                    <p><input name="number1" /></p>
                    <p><input type="submit" value="Submit Case" /></p>
                </form>
            </body>
        </html>
    '''