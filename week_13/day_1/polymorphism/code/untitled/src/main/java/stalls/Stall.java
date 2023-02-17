package stalls;

import interfaces.IReviewed;

public abstract class Stall implements IReviewed {

    public String name;
    public String owner;
    public int rating;
    public String parkingSpot;

    public Stall(String name, String owner, int rating, String parkingSpot){
        this.name = name;
        this.owner = owner;
        this.rating = rating;
        this.parkingSpot = parkingSpot;
    }
}
