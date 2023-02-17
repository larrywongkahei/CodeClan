package Stocks;

public class Instrument implements IPlay{
    public String material;
    public String colour;
    public Type type;
    public Instrument(String material, String colour, Type type){
        this.material = material;
        this.colour = colour;
        this.type = type;
    }

    @Override
    public String play(){return "";
    }
}
