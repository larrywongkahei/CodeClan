package stalls;

import interfaces.IReviewed;

public class CandyFlossStall extends Stall implements IReviewed {
    public CandyFlossStall(String name, String owner, int rating, String parkingSpot) {
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
