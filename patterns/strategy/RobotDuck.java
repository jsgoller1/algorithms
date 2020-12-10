package strategy;

public class RobotDuck extends Duck {
    public RobotDuck() {
        quackBehavior = new MechanizedQuack();
        flyBehavior = new FlyWithIonThrusters();
    }

    public void display() {
        System.out.println("This is a robotic duck.");
    }
}
