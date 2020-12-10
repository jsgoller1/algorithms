package strategy;

interface FlyBehavior {
    void fly();
}

class FlyWithWings implements FlyBehavior {
    public void fly() {
        System.out.println("I am flying using wings!");
    }
}

class RocketPoweredFlight implements FlyBehavior {
    public void fly() {
        System.out.println("I'm flying with a rocket!");

    }
}

class FlyWithIonThrusters implements FlyBehavior {
    public void fly() {
        System.out.println("Engage. (I thought this was a duck pond, not Star Trek!)");

    }
}
