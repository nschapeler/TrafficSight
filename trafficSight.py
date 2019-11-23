from flask import Flask, request, jsonify, render_template
from locFuncs import LocationHandler

global loc
global app

# TODO: Obs ne ampel gibt und welche farbe + Auto


def create_app():
    app = Flask(__name__, template_folder='FrontEnd')
    loc = LocationHandler()

    @app.route("/")
    def main():
        return render_template("MainHTML.html")

    # Returns true if user is nearing an intersection
    @app.route('/get-location-info')
    def getLocationInfo():
        location = request.args.get('location')
        crossingIncoming = loc.do_locationing(location)
        response = {"crossing": crossingIncoming}
        return jsonify(response)

    # @app.route('/get-image-data')
    # def getImageData():

    return app