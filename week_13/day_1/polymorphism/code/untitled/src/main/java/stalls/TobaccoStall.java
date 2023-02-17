package stalls;

import interfaces.ISecurity;
import visitors.Visitor;

public class TobaccoStall extends Stall implements ISecurity {
    public TobaccoStall(String name, String owner, int rating, String parkingSpot) {
        super(name, owner, rating, parkingSpot);
    }

    @Override
    public boolean isAllowTo(Visitor visitor) {
        return visitor.getAge() >= 18;
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
