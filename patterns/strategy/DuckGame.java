package strategy;

public class DuckGame {
    public static void main(String args[]) {
        Duck mallard = new MallardDuck();
        Duck robot = new RobotDuck();

        mallard.performQuack();
        robot.performQuack();

        // The Strategy pattern allows us to duck behavior at runtime
        mallard.setQuackBehavior(new Squeak());
        mallard.performQuack();

        robot.setFlyBehavior(new RocketPoweredFlight());
        robot.performFly();
    }
}