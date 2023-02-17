import attractions.Rollercoaster;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import visitors.Visitor;

public class RollercoasterTest {

    public Rollercoaster rollercoaster;
    public Visitor visitor1;
    public Visitor visitor2;

    @Before
    public void setup(){
        rollercoaster = new Rollercoaster("LarryFunRoller", 5);
        visitor1 = new Visitor(18, 210, 2000);
        visitor2 = new Visitor(12, 140, 2000);

    }

    @Test
    public void rollerHasStartingPrice(){
        Assert.assertEquals(8.4, rollercoaster.defaultPrice(), 0.0);
    }

    @Test
    public void rollerCouldChargeDifferently(){
        Assert.assertEquals(8.4, rollercoaster.priceFor(visitor2), 0.0);
        Assert.assertEquals(16.8, rollercoaster.priceFor(visitor1), 0.0);
    }
}
