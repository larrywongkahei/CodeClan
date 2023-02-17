package stalls;

import interfaces.IReviewed;

public class IceCreamStall extends Stall implements IReviewed {
    public IceCreamStall(String name, String owner, int rating, String parkingSpot) {
        super(name, owner, rating, parkingSpot);
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
