package attractions;

import interfaces.IReviewed;

public class Park extends Attraction implements IReviewed {
    public Park(String name, int rating) {
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
}
