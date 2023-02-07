import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class BearTest {

    private Bear bear;
    private Salmon salmon;
    private River river;

    @Before
    public void setup(){
        bear = new Bear("Baloo");
        salmon = new Salmon();
        river = new River();
        river.addFish(salmon);
    }

    @Test
    public void bellyStartEmpty(){
        Assert.assertEquals(0, bear.foodCount());
    }

    @Test
    public void canEatSalmon(){
        bear.eatFishFromRiver(river);
        Assert.assertEquals(1, bear.foodCount());
    }

    @Test
    public void shouldEvacuateBowels(){
        bear.eatFishFromRiver(river);
        bear.shitInTheWoods();
        Assert.assertEquals(0, bear.foodCount());
    }
}
