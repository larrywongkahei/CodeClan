package Stocks;

public class DrumSticks implements ISell{
    public int price;

    public DrumSticks(int price){
        this.price = price;
    }
    @Override
    public int calculateMarkup() {
        return this.price;
    }
}
