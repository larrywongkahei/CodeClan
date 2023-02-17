import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PassengerTest {

    private Passenger passenger1;
    private Passenger passenger2;
    private Passenger passenger3;
    private Passenger passenger4;
    private Passenger passenger5;


    @Before
    public void setup(){
        passenger1 = new Passenger("Larry", 3);
        passenger2 = new Passenger("Brian", 1);
        passenger3 = new Passenger("Joe", 2);
        passenger4 = new Passenger("Cindy", 1);
        passenger5 = new Passenger("Kerry", 4);
    }

    @Test
    public void passengerHasName(){
        Assert.assertEquals("Larry", passenger1.getName());
        Assert.assertEquals("Brian", passenger2.getName());
        Assert.assertEquals("Joe", passenger3.getName());
        Assert.assertEquals("Cindy", passenger4.getName());
        Assert.assertEquals("Kerry", passenger5.getName());
    }

    @Test
    public void passengerHasBags(){
        Assert.assertEquals(3, passenger1.getBags());
        Assert.assertEquals(1, passenger2.getBags());
        Assert.assertEquals(2, passenger3.getBags());
        Assert.assertEquals(1, passenger4.getBags());
        Assert.assertEquals(4, passenger5.getBags());
    }
}
