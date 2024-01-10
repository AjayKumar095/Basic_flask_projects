from flask import Blueprint as bp, render_template , request, redirect, url_for
import bcrypt
import json

module8_bp=bp("module8", __name__)

@module8_bp.route("/task8", methods=["POST","GET"])
def task8():
    return render_template("intermediate/module8_result.html")