package Stocks;

public class GuitarStrings implements ISell{
    public int price;

    public GuitarStrings(int price){
        this.price = price;
    }

    @Override
    public int calculateMarkup() {
        return this.price;
    }
}
