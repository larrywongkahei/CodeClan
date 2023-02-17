import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PilotTest {

    private Pilot pilot;

    @Before
    public void setup(){
        pilot = new Pilot("LarryAgain", "Pilot", "3325498");

    }

    @Test
    public void pilotHasName(){
        Assert.assertEquals("LarryAgain", pilot.getName());
    }

    @Test
    public void pilotHasRank(){
        Assert.assertEquals("Pilot", pilot.getRank());
    }

    @Test
    public void pilotHasLicenceNumber(){
        Assert.assertEquals("3325498", pilot.getLicenseNumber());
    }

    @Test
    public void pilotCouldFlyThePlane() { Assert.assertEquals("The Flight Has Departured", pilot.flyThePlane());}
}

