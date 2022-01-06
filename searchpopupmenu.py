from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.clock import Clock
import certifi

# import os


class SearchPopupMenu(MDInputDialog):
    title = "Search by Address"
    text_button_ok = "Search"
    # api_key = os.environ["API_KEY"]

    def __init__(self):
        super().__init__()
        self.size_hint = [0.9, 0.3]
        self.events_callback = self.callback

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
        print(address)

    def geocode_get_lat_lon(self, address):
        with open("api_key.txt", "r") as f:
            api_key = f.read()
        # api_key = self.api_key
        address = parse.quote(address)
        url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey={api_key}&searchtext={address}"
        UrlRequest(
            url,
            on_success=self.success,
            on_failure=self.failure,
            on_error=self.error,
            ca_file=certifi.where(),
        )

    def success(self, urlrequest, result):
        print("Success")
        latitude = result["Response"]["View"][0]["Result"][0]["Location"][
            "NavigationPosition"
        ][0]["Latitude"]
        longitude = result["Response"]["View"][0]["Result"][0]["Location"][
            "NavigationPosition"
        ][0]["Longitude"]
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

        print(result)

    def failure(self, urlrequest, result):
        print("Failure")
        print(result)

    def error(self, urlrequest, result):
        print("Error")
        print(result)
