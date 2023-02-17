package attractions;

import interfaces.ISecurity;
import visitors.Visitor;
import interfaces.ITicketed;

public class Rollercoaster extends Attraction implements ISecurity, ITicketed {

    public Rollercoaster(String name, int rating) {
        super(name, rating);

    }

    @Override
    public boolean isAllowTo(Visitor visitor) {
        return visitor.getAge() > 12 & visitor.getHeight() > 145;
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
        return 8.4;
    }

    @Override
    public double priceFor(Visitor visitor) {
        if (visitor.getHeight() >= 200) {
            return defaultPrice() * 2;
        }
        return defaultPrice();
    }
}
