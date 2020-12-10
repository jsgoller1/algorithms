# strategy

According to _Head First Design Patterns_:
> The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.  Strategy lets the algorithm vary independently from clients that use it.

Examples
- `ducks` - from HFDP, this family of objects represents a duck pond simulator game with several different kinds of ducks. The Strategy pattern represents programming to an interface rather than to an implementation, and allows each duck subclass to remain unchanged when new behavior is introduce. Code likely to change a lot (duck behaviors) is implemented via behavior classes that are composable and reusable. See chapter 1 of HFDP for a full explanation and requirements (my implementation deviates slightly).