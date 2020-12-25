package observer;

/*
    Metric is a read-only class I came up with; Subjects and Objects
    have nothing to do with temperature, humidity, and pressure,
    so they shouldn't reference those details in their interfaces.
    This object handles interaction with meaningful data.
*/

public class Metric {
    private float temp;
    private float humidity;
    private float presssure;

    public float getTemp() {
        return this.temp;
    }

    public float getHumidity() {
        return this.humidity;
    }

    public float getPresssure() {
        return this.presssure;
    }

    public Metric(float temp, float humidity, float pressure) {
        this.temp = temp;
        this.humidity = humidity;
        this.presssure = pressure;
    }

}
