package attractions;

import interfaces.ISecurity;
import visitors.Visitor;

public class Playground extends Attraction implements ISecurity {
    public Playground(String name, int rating) {
        super(name, rating);
    }



    @Override
    public boolean isAllowTo(Visitor visitor) {
        return visitor.getAge() <= 15;
    }

    @Override
    public int getRating() {
        return 0;
    }

    @Override
    public String getName() {
        return name;
    }
}
