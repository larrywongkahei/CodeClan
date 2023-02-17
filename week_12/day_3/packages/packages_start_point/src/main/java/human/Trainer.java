package human;


import animal.Dog;
import animal.air.Bird;


public class Trainer {
    public String teach(Dog dog) {
        return dog.bark();
    }

    public String trainBird(Bird bird){
        return bird.speak();
    }
}
