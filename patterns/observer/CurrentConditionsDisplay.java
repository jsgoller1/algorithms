package observer;

public class CurrentConditionsDisplay implements DisplayElement, Observer {
    Metric currentMetric;

    public void update(Metric m) {
        currentMetric = m;
    }

    public void display() {
        System.out.println("Current temp:");
        System.out.println("Current humidity:");
        System.out.println("Current pressure:");
    }

}
