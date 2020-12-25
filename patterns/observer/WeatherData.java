package observer;

import java.util.HashSet;
import java.util.Random;

/*
    WeatherData is a subject that will be observed by several displays. If 
    we wanted to get super GoF-y here, we could implement observer behavior
    using Strategies, but since we only have one type of Pub/Sub interaction,
    that's not useful.
*/

public class WeatherData implements Subject {
    private HashSet<Observer> observers;

    public void registerObserver(Observer obs) {
        this.observers.add(obs);
    }

    public void removeObserver(Observer obs) {
        this.observers.remove(obs);
    }

    public void notifyObservers(Metric m) {
        for (Observer obs : this.observers) {
            obs.update(m);
        }
    }

    public void measurementsChanged() {
        Random rand = new Random();
        float temp = rand.nextFloat() * (float) 100.0;
        float humidity = rand.nextFloat() * (float) 100.0;
        float pressure = rand.nextFloat() * (float) 100.0;
        Metric m = new Metric(temp, humidity, pressure);
        this.notifyObservers(m);
    }

    public WeatherData() {
        this.observers = new HashSet<Observer>();
    }
}
