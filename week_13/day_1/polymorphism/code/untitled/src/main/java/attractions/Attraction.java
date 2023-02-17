package attractions;

import interfaces.IReviewed;

public abstract class Attraction implements IReviewed {

    public String name;
    public int rating;
    public int visitCount;

    public Attraction(String name, int rating){
        this.name = name;
        this.rating = rating;
        this.visitCount = 0;
    }
}
