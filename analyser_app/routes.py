from flask import render_template, url_for, request, flash, redirect
from analyser_app.forms import UploadLogForm
from analyser_app.dummy_data import dummy_data
from analyser_app import app, db

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = UploadLogForm()
    if form.validate_on_submit():
        flash_msg = f"Success! Uploaded: {form.file.data}"
        # TODO: actually upload the physical file and feed into analyser
        flash(flash_msg, 'success')
        # TODO: fetch confluence table data and compare to analyser output - update web app i.e. redirect to home with analyser table filled out
        # dummy data
    return render_template("home.html", title="Log Analyser", form=form, data=dummy_data)

@app.route("/documentation")
def documentation():
    return render_template("documentation.html", title="Documentation")

@app.route("/settings")
def settings():
    return render_template("settings.html", title="Settings")

@app.route("/source_code")
def source_code():
    return render_template("source_code.html", title="Source Code")