package interfaces;
import visitors.Visitor;

public interface ISecurity {
    public boolean isAllowTo(Visitor visitor);
}
