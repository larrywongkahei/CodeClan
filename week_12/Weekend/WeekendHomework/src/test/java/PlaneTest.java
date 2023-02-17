import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PlaneTest {

    private Plane plane1;
    private Plane plane2;

    @Before
    public void setup(){
        plane1 = new Plane(PlaneType.BOEING747);
        plane2 = new Plane(PlaneType.BOEING777);
    }

    @Test
    public void planeHasCapacity(){
        Assert.assertEquals(38, plane1.getCapacity());
        Assert.assertEquals(56, plane2.getCapacity());
    }

    @Test
    public void planeHasTotalWeight(){
        Assert.assertEquals(2000, plane1.getTotalWeight(), 0.0);
        Assert.assertEquals(2500, plane2.getTotalWeight(), 0.0);
    }
}
