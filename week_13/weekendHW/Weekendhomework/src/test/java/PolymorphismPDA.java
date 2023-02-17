import Stocks.Guitars;
import Stocks.Pianos;
import Stocks.Type;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PolymorphismPDA {
    Guitars guitars;
    Pianos pianos;

    @Before
    public void setup(){
        guitars = new Guitars("wood", "brown", Type.STRINGS, 6, 3000);
        pianos = new Pianos("wood", "gray", Type.KEYBOARD, 88, 4500);
    }

    @Test
    public void playDifferently(){
        Assert.assertTrue(guitars.play() != pianos.play());
        System.out.println(guitars.play());
        System.out.println(pianos.play());
    }
}
