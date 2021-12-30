from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class MarketMarker(MapMarkerPopup):
    market_data = []

    def on_release(self, *args):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [0.8, 0.9]
        menu.open()
