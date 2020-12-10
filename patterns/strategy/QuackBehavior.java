package strategy;

interface QuackBehavior {
    void quack();
}

class Quack implements QuackBehavior {
    public void quack() {
        System.out.println("Quack quack!");
    }
}

class Squeak implements QuackBehavior {
    public void quack() {
        System.out.println("Squeak squeak!");
    }
}

class MechanizedQuack implements QuackBehavior {
    public void quack() {
        System.out.println("*bzzzzt* QUAAAACK.");
    }
}