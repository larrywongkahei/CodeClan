import attractions.Dodgems;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import visitors.Visitor;

public class DodgemsTest {

    public Dodgems dodgems;
    public Visitor visitor1;
    public Visitor visitor2;

    @Before
    public void setup(){
        dodgems = new Dodgems("Cindy", 5);
        visitor1 = new Visitor(18, 210, 2000);
        visitor2 = new Visitor(11, 140, 2000);
    }

    @Test
    public void dodgemsHasStartingPrice(){
        Assert.assertEquals(4.5, dodgems.defaultPrice(), 0.0);
    }

    @Test
    public void rollerCouldChargeDifferently(){
        Assert.assertEquals(2.25, dodgems.priceFor(visitor2), 0.0);
        Assert.assertEquals(4.5, dodgems.priceFor(visitor1), 0.0);
    }
}
