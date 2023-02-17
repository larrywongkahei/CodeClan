package interfaces;
import visitors.Visitor;

public interface ITicketed {
    public double defaultPrice();
    public double priceFor(Visitor visitor);
}
