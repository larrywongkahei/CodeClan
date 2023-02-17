package attractions;

import interfaces.IReviewed;
import interfaces.ITicketed;
import visitors.Visitor;

public class Dodgems extends Attraction implements IReviewed, ITicketed {


    public Dodgems(String name, int rating) {
        super(name, rating);
    }

    @Override
    public int getRating() {
        return 0;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double defaultPrice() {
        return 4.5;
    }

    @Override
    public double priceFor(Visitor visitor) {
        if(visitor.getAge() < 12){
            return defaultPrice()/2;
        };
        return defaultPrice();
    }
}
