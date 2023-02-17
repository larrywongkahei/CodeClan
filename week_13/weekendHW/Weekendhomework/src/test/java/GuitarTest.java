import Stocks.Guitars;
import Stocks.Type;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class GuitarTest {
    public Guitars guitars;

    @Before
    public void setup(){
        guitars = new Guitars("wood", "yellow", Type.STRINGS, 6, 2000);
    }

    @Test
    public void guitarsHasStrings(){
        Assert.assertEquals(6, guitars.getStrings());
    }

    @Test
    public void guitarsCouldPlay(){
        Assert.assertEquals("I ~ am ~ Guitar ~", guitars.play());
    }

    @Test
    public void guitarsHasPrice(){
        Assert.assertEquals(2000, guitars.getPrice());
    }
}
