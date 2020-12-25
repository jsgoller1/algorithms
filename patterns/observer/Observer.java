package observer;

/*
    Observers watch Subjects for updates. 
*/

interface Observer {
    public void update(Metric me);
}
