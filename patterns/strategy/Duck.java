package strategy;

public abstract class Duck {
  FlyBehavior flyBehavior;
  QuackBehavior quackBehavior;

  // All ducks can do quacking which is
  // implemented by their QuackBehavior interface
  // class and performQuack(); note that these
  // _have_ the interfaces, but aren't _implementing_ them
  public void performQuack() {
    quackBehavior.quack();
  }

  void performFly() {
    flyBehavior.fly();
  };

  public void setFlyBehavior(FlyBehavior fb) {
    flyBehavior = fb;
  }

  public void setQuackBehavior(QuackBehavior qb) {
    quackBehavior = qb;
  }

  void swim() {
    System.out.println("All ducks can float, even decoys!");
  };

  public abstract void display();

}
