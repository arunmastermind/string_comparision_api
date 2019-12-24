# from stringFuzzer import failureMatcher
#
# s1 = "a1"
# s2 = "a"
#
# print(failureMatcher.matchPercent(s1, s2))


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<str1>/<str2>/', methods=['GET', 'POST'])
def landing_page(str1, str2):
    return render_template('test.html', str1=str1, str2=str2)

if __name__ == "__main__":
    app.run(debug=True)
