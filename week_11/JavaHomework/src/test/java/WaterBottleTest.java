import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class WaterBottleTest {
    private WaterBottle bottle;

    @Before
    public void setup(){
        bottle = new WaterBottle();
    }

    @Test
    public void checkIfBottleHasVolume(){
        Assert.assertEquals(100, bottle.getVolume());
    }

    @Test
    public void checkIfAbleToDrink(){
        bottle.drink();
        Assert.assertEquals(90, bottle.getVolume());
    }

    @Test
    public void checkIfAbleToDrink2(){
        bottle.drink();
        Assert.assertEquals(90, bottle.getVolume());
        bottle.drink();
        Assert.assertEquals(80, bottle.getVolume());
    }

    @Test
    public void checkIfAbleToEmpty(){
        Assert.assertEquals(100, bottle.getVolume());
        bottle.empty();
        Assert.assertEquals(0, bottle.getVolume());
    }

    @Test
    public void checkIfAbleToFill(){
        bottle.empty();
        Assert.assertEquals(0, bottle.getVolume());
        bottle.fill();
        Assert.assertEquals(100, bottle.getVolume());

    }


}
