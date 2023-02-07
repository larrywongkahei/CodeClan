import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class RiverTest {

    private River river;
    private Salmon salmon;

    @Before
    public void setup(){
        river = new River();
        salmon = new Salmon();
    }

    @Test
    public void canAddSalmon(){
        river.addFish(salmon);
        Assert.assertEquals(1, river.fishCount());
    }

    @Test
    public void canGetSalmon(){
        river.addFish(salmon);
        river.removeFish();
        Assert.assertEquals(0, river.fishCount());
    }
}
