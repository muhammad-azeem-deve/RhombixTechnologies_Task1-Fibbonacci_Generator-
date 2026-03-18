from flask import Flask, render_template, request

app = Flask(__name__)

def generate_fibonacci(n):
    if n <= 0:
        return []
    fib = [0] * n
    if n >= 1:
        fib[0] = 0
    if n >= 2:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


@app.route('/', methods=['GET', 'POST'])
def index():
    sequence = None
    error = None
    n = None

    if request.method == 'POST':
        try:
            n = int(request.form.get('terms', '').strip())
            if n <= 0:
                raise ValueError
            sequence = generate_fibonacci(n)
        except ValueError:
            error = "Please enter a positive whole number (e.g. 15)"
        except Exception:
            error = "Something went wrong — please try again!"

    return render_template('index.html', 
                          sequence=sequence, 
                          error=error, 
                          n=n)


if __name__ == '__main__':
    app.run(debug=True)