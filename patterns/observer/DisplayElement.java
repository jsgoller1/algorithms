package observer;

/*
    Display elements show observed data in some way. Depending on how many different
    ways there are to do displaying, a Strategy could be called for here but
    at present isn't needed. 
*/

interface DisplayElement {
    public void display();
}
