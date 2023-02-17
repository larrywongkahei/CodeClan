package Stocks;

public class Pianos extends Instrument implements ISell{

    public int Keys;
    public int price;

    public int getPrice() {
        return price;
    }

    public Pianos(String material, String colour, Type type, int Keys, int price) {
        super(material, colour, type);
        this.Keys = Keys;
        this.price = price;
    }

    @Override
    public int calculateMarkup() {
        return this.price;
    }

    @Override
    public String play(){
        return "I ~ am ~ Pi ~ Pi ~ Pi ~ an ~ no";
    }

    public int getKeys() {
        return Keys;
    }
}
