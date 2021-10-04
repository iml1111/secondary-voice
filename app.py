from flask import Flask, render_template


app = Flask(
    import_name=__name__,
    instance_relative_config=True,
    static_url_path="/",
    static_folder='client/',
    template_folder='client/'
)


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)