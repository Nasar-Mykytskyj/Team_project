from kivy_garden.mapview import MapView, MapMarker


class Map(MapView):

    def on_touch_down(self, touch):
        global xList
        global yList
        m1 = MapMarker(lat=67, lon=42)
        self.add_marker(m1)
        print(xList)
        print(yList)
        for i in range(len(xList)):
            m=MapMarker(lat=xList[i],lon=yList[i])
            self.add_marker(m)


