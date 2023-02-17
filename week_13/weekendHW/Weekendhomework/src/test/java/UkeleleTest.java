import Stocks.Type;
import Stocks.Ukeleles;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class UkeleleTest {
    public Ukeleles ukelele;

    @Before
    public void setup(){
        ukelele = new Ukeleles("wood", "black", Type.STRINGS, 5, 1500);

    }

    @Test
    public void ukleleHasStings(){
        Assert.assertEquals(5, ukelele.getStrings());
    }

    @Test
    public void ukeleleCouldPlay(){
        Assert.assertEquals("I ~ am ~ baby ~ guitar", ukelele.play());
    }

    @Test
    public void ukeleleHasPrice(){
        Assert.assertEquals(1500, ukelele.getPrice());
    }
}
