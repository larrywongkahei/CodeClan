package Stocks;

public class Ukeleles extends Instrument implements ISell{

    public int Strings;
    public int price;

    public Ukeleles(String material, String colour, Type type, int Strings, int price) {
        super(material, colour, type);
        this.Strings = Strings;
        this.price = price;
    }

    public int getPrice() {
        return price;
    }
    public int getStrings() {
        return Strings;
    }

    @Override
    public int calculateMarkup() {
        return this.price;
    }

    @Override
    public String play(){
        return "I ~ am ~ baby ~ guitar";
    }
}
