from flask import Flask, request
import pickle
from flask import jsonify

app = Flask(__name__)


@app.route('/decision_tree', methods=['GET', 'POST'])
def decision_tree():
    if request.method == 'POST':
        model = pickle.load(open('../decision_tree_model.pkl', 'rb'))
        print("this is the     ", request)

        Start_Lat = request.form.get("Start_Lat")
        Start_Lng = request.form.get("Start_Lng")
        Distance = request.form.get("Distance")
        Side = request.form.get("Side")
        County = request.form.get("County")
        State = request.form.get("State")
        Timezone = request.form.get("Timezone")
        Airport_Code = request.form.get("Airport_Code")
        Temperature = request.form.get("Temperature")
        Humidity = request.form.get("Humidity")
        Pressure = request.form.get("Pressure")
        Visibility = request.form.get("Visibility")
        Wind_Direction = request.form.get("Wind_Direction")
        Wind_Speed = request.form.get("Wind_Speed")
        Weather_Condition = request.form.get("Weather_Condition")
        Amenity = request.form.get("Amenity")
        Bump = request.form.get("Bump")
        Crossing = request.form.get("Crossing")
        Give_Way = request.form.get("Give_Way")
        Junction = request.form.get("Junction")
        No_Exit = request.form.get("No_Exit")
        Railway = request.form.get("Railway")
        Roundabout = request.form.get("Roundabout")
        Station = request.form.get("Station")
        Stop = request.form.get("Stop")
        Traffic_Calming = request.form.get("Traffic_Calming")
        Traffic_Signal = request.form.get("Traffic_Signal")
        Turning_Loop = request.form.get("Turning_Loop")
        Sunrise_Sunset = request.form.get("Sunrise_Sunset")
        Civil_Twilight = request.form.get("Civil_Twilight")
        Nautical_Twilight = request.form.get("Nautical_Twilight")
        Astronomical_Twilight = request.form.get("Astronomical_Twilight")
        Year = request.form.get("Year")
        Month = request.form.get("Month")
        Hour = request.form.get("Hour")
        DelayTime = request.form.get("DelayTime")
        Day = request.form.get("Day")
        Start_Time_Month = request.form.get("Start_Time_Month")
        Start_Time_Year = request.form.get("Start_Time_Year")
        End_Time_Month = request.form.get("End_Time_Month")
        End_Time_Year = request.form.get("End_Time_Year")

        result = model.predict([[Start_Lat,
                                 Start_Lng,
                                 Distance,
                                 Side,
                                 County,
                                 State,
                                 Timezone,
                                 Airport_Code,
                                 Temperature,
                                 Humidity,
                                 Pressure,
                                 Visibility,
                                 Wind_Direction,
                                 Wind_Speed,
                                 Weather_Condition,
                                 Amenity,
                                 Bump,
                                 Crossing,
                                 Give_Way,
                                 Junction,
                                 No_Exit,
                                 Railway,
                                 Roundabout,
                                 Station,
                                 Stop,
                                 Traffic_Calming,
                                 Traffic_Signal,
                                 Turning_Loop,
                                 Sunrise_Sunset,
                                 Civil_Twilight,
                                 Nautical_Twilight,
                                 Astronomical_Twilight,
                                 Year,
                                 Month,
                                 Hour,
                                 DelayTime,
                                 Day,
                                 Start_Time_Month,
                                 Start_Time_Year,
                                 End_Time_Month,
                                 End_Time_Year, ]])

        print(result)
        print(type(result))
        print(result[0])
        result_string = (str(result[0]))
        result_json = {"severity": result_string}
        print(result_json)
        return result_json


@app.route('/neural_network', methods=['GET', 'POST'])
def neural_network():
    if request.method == 'POST':
        model = pickle.load(open('../neural_network_model.pkl', 'rb'))
        print("this is the     ", request)

        Start_Lat = request.form.get("Start_Lat")
        Start_Lng = request.form.get("Start_Lng")
        Distance = request.form.get("Distance")
        Side = request.form.get("Side")
        County = request.form.get("County")
        State = request.form.get("State")
        Timezone = request.form.get("Timezone")
        Airport_Code = request.form.get("Airport_Code")
        Temperature = request.form.get("Temperature")
        Humidity = request.form.get("Humidity")
        Pressure = request.form.get("Pressure")
        Visibility = request.form.get("Visibility")
        Wind_Direction = request.form.get("Wind_Direction")
        Wind_Speed = request.form.get("Wind_Speed")
        Weather_Condition = request.form.get("Weather_Condition")
        Amenity = request.form.get("Amenity")
        Bump = request.form.get("Bump")
        Crossing = request.form.get("Crossing")
        Give_Way = request.form.get("Give_Way")
        Junction = request.form.get("Junction")
        No_Exit = request.form.get("No_Exit")
        Railway = request.form.get("Railway")
        Roundabout = request.form.get("Roundabout")
        Station = request.form.get("Station")
        Stop = request.form.get("Stop")
        Traffic_Calming = request.form.get("Traffic_Calming")
        Traffic_Signal = request.form.get("Traffic_Signal")
        Turning_Loop = request.form.get("Turning_Loop")
        Sunrise_Sunset = request.form.get("Sunrise_Sunset")
        Civil_Twilight = request.form.get("Civil_Twilight")
        Nautical_Twilight = request.form.get("Nautical_Twilight")
        Astronomical_Twilight = request.form.get("Astronomical_Twilight")
        Year = request.form.get("Year")
        Month = request.form.get("Month")
        Hour = request.form.get("Hour")
        DelayTime = request.form.get("DelayTime")
        Day = request.form.get("Day")
        Start_Time_Month = request.form.get("Start_Time_Month")
        Start_Time_Year = request.form.get("Start_Time_Year")
        End_Time_Month = request.form.get("End_Time_Month")
        End_Time_Year = request.form.get("End_Time_Year")

        result = model.predict([[Start_Lat,
                                 Start_Lng,
                                 Distance,
                                 Side,
                                 County,
                                 State,
                                 Timezone,
                                 Airport_Code,
                                 Temperature,
                                 Humidity,
                                 Pressure,
                                 Visibility,
                                 Wind_Direction,
                                 Wind_Speed,
                                 Weather_Condition,
                                 Amenity,
                                 Bump,
                                 Crossing,
                                 Give_Way,
                                 Junction,
                                 No_Exit,
                                 Railway,
                                 Roundabout,
                                 Station,
                                 Stop,
                                 Traffic_Calming,
                                 Traffic_Signal,
                                 Turning_Loop,
                                 Sunrise_Sunset,
                                 Civil_Twilight,
                                 Nautical_Twilight,
                                 Astronomical_Twilight,
                                 Year,
                                 Month,
                                 Hour,
                                 DelayTime,
                                 Day,
                                 Start_Time_Month,
                                 Start_Time_Year,
                                 End_Time_Month,
                                 End_Time_Year, ]])

        print(result)
        print(type(result))
        print(result[0])
        result_string = (str(result[0]))
        result_json = {"severity": result_string}
        print(result_json)
        return result_json


@app.route('/logistic_regression', methods=['GET', 'POST'])
def logistic_regression():
    if request.method == 'POST':
        model = pickle.load(open('../logistic_regression_model.pkl', 'rb'))
        print("this is the     ", request)

        Start_Lat = request.form.get("Start_Lat")
        Start_Lng = request.form.get("Start_Lng")
        Distance = request.form.get("Distance")
        Side = request.form.get("Side")
        County = request.form.get("County")
        State = request.form.get("State")
        Timezone = request.form.get("Timezone")
        Airport_Code = request.form.get("Airport_Code")
        Temperature = request.form.get("Temperature")
        Humidity = request.form.get("Humidity")
        Pressure = request.form.get("Pressure")
        Visibility = request.form.get("Visibility")
        Wind_Direction = request.form.get("Wind_Direction")
        Wind_Speed = request.form.get("Wind_Speed")
        Weather_Condition = request.form.get("Weather_Condition")
        Amenity = request.form.get("Amenity")
        Bump = request.form.get("Bump")
        Crossing = request.form.get("Crossing")
        Give_Way = request.form.get("Give_Way")
        Junction = request.form.get("Junction")
        No_Exit = request.form.get("No_Exit")
        Railway = request.form.get("Railway")
        Roundabout = request.form.get("Roundabout")
        Station = request.form.get("Station")
        Stop = request.form.get("Stop")
        Traffic_Calming = request.form.get("Traffic_Calming")
        Traffic_Signal = request.form.get("Traffic_Signal")
        Turning_Loop = request.form.get("Turning_Loop")
        Sunrise_Sunset = request.form.get("Sunrise_Sunset")
        Civil_Twilight = request.form.get("Civil_Twilight")
        Nautical_Twilight = request.form.get("Nautical_Twilight")
        Astronomical_Twilight = request.form.get("Astronomical_Twilight")
        Year = request.form.get("Year")
        Month = request.form.get("Month")
        Hour = request.form.get("Hour")
        DelayTime = request.form.get("DelayTime")
        Day = request.form.get("Day")
        Start_Time_Month = request.form.get("Start_Time_Month")
        Start_Time_Year = request.form.get("Start_Time_Year")
        End_Time_Month = request.form.get("End_Time_Month")
        End_Time_Year = request.form.get("End_Time_Year")

        result = model.predict([[Start_Lat,
                                 Start_Lng,
                                 Distance,
                                 Side,
                                 County,
                                 State,
                                 Timezone,
                                 Airport_Code,
                                 Temperature,
                                 Humidity,
                                 Pressure,
                                 Visibility,
                                 Wind_Direction,
                                 Wind_Speed,
                                 Weather_Condition,
                                 Amenity,
                                 Bump,
                                 Crossing,
                                 Give_Way,
                                 Junction,
                                 No_Exit,
                                 Railway,
                                 Roundabout,
                                 Station,
                                 Stop,
                                 Traffic_Calming,
                                 Traffic_Signal,
                                 Turning_Loop,
                                 Sunrise_Sunset,
                                 Civil_Twilight,
                                 Nautical_Twilight,
                                 Astronomical_Twilight,
                                 Year,
                                 Month,
                                 Hour,
                                 DelayTime,
                                 Day,
                                 Start_Time_Month,
                                 Start_Time_Year,
                                 End_Time_Month,
                                 End_Time_Year, ]])

        print(result)
        print(type(result))
        print(result[0])
        result_string = (str(result[0]))
        result_json = {"severity": result_string}
        print(result_json)
        return result_json


@app.route('/random_forest', methods=['GET', 'POST'])
def random_forest():
    if request.method == 'POST':
        model = pickle.load(open('../random_forest_model.pkl', 'rb'))
        print("this is the     ", request)

        Start_Lat = request.form.get("Start_Lat")
        Start_Lng = request.form.get("Start_Lng")
        Distance = request.form.get("Distance")
        Side = request.form.get("Side")
        County = request.form.get("County")
        State = request.form.get("State")
        Timezone = request.form.get("Timezone")
        Airport_Code = request.form.get("Airport_Code")
        Temperature = request.form.get("Temperature")
        Humidity = request.form.get("Humidity")
        Pressure = request.form.get("Pressure")
        Visibility = request.form.get("Visibility")
        Wind_Direction = request.form.get("Wind_Direction")
        Wind_Speed = request.form.get("Wind_Speed")
        Weather_Condition = request.form.get("Weather_Condition")
        Amenity = request.form.get("Amenity")
        Bump = request.form.get("Bump")
        Crossing = request.form.get("Crossing")
        Give_Way = request.form.get("Give_Way")
        Junction = request.form.get("Junction")
        No_Exit = request.form.get("No_Exit")
        Railway = request.form.get("Railway")
        Roundabout = request.form.get("Roundabout")
        Station = request.form.get("Station")
        Stop = request.form.get("Stop")
        Traffic_Calming = request.form.get("Traffic_Calming")
        Traffic_Signal = request.form.get("Traffic_Signal")
        Turning_Loop = request.form.get("Turning_Loop")
        Sunrise_Sunset = request.form.get("Sunrise_Sunset")
        Civil_Twilight = request.form.get("Civil_Twilight")
        Nautical_Twilight = request.form.get("Nautical_Twilight")
        Astronomical_Twilight = request.form.get("Astronomical_Twilight")
        Year = request.form.get("Year")
        Month = request.form.get("Month")
        Hour = request.form.get("Hour")
        DelayTime = request.form.get("DelayTime")
        Day = request.form.get("Day")
        Start_Time_Month = request.form.get("Start_Time_Month")
        Start_Time_Year = request.form.get("Start_Time_Year")
        End_Time_Month = request.form.get("End_Time_Month")
        End_Time_Year = request.form.get("End_Time_Year")

        result = model.predict([[Start_Lat,
                                 Start_Lng,
                                 Distance,
                                 Side,
                                 County,
                                 State,
                                 Timezone,
                                 Airport_Code,
                                 Temperature,
                                 Humidity,
                                 Pressure,
                                 Visibility,
                                 Wind_Direction,
                                 Wind_Speed,
                                 Weather_Condition,
                                 Amenity,
                                 Bump,
                                 Crossing,
                                 Give_Way,
                                 Junction,
                                 No_Exit,
                                 Railway,
                                 Roundabout,
                                 Station,
                                 Stop,
                                 Traffic_Calming,
                                 Traffic_Signal,
                                 Turning_Loop,
                                 Sunrise_Sunset,
                                 Civil_Twilight,
                                 Nautical_Twilight,
                                 Astronomical_Twilight,
                                 Year,
                                 Month,
                                 Hour,
                                 DelayTime,
                                 Day,
                                 Start_Time_Month,
                                 Start_Time_Year,
                                 End_Time_Month,
                                 End_Time_Year, ]])

        print(result)
        print(type(result))
        print(result[0])
        result_string = (str(result[0]))
        result_json = {"severity": result_string}
        print(result_json)
        return result_json


if __name__ == '__main__':
    app.run(debug=True)
