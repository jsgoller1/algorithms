package observer;

/*
Subject's job is to allow for publication and subscription;
it registers Observers and then notifys them of updates.
*/
interface Subject {
    public void registerObserver(Observer obs);

    public void removeObserver(Observer obs);

    public void notifyObservers(Metric m);
}
