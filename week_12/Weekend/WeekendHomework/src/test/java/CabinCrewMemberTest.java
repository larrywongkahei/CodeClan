import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class CabinCrewMemberTest {

    private CabinCrewMember cabinCrewMember1;
    private CabinCrewMember cabinCrewMember2;
    private CabinCrewMember cabinCrewMember3;

    @Before
    public void setUp(){
        cabinCrewMember1 = new CabinCrewMember("Mary", "Purser");
        cabinCrewMember2 = new CabinCrewMember("Peter", "Captain");
        cabinCrewMember3 = new CabinCrewMember("Billy", "First Officer");
    }

    @Test
    public void cabinCrewMemberHasName(){
        Assert.assertEquals("Mary", cabinCrewMember1.getName());
        Assert.assertEquals("Peter", cabinCrewMember2.getName());
        Assert.assertEquals("Billy", cabinCrewMember3.getName());
    }

    @Test
    public void cabinCrewMemberHasRank(){
        Assert.assertEquals("Purser", cabinCrewMember1.getRank());
        Assert.assertEquals("Captain", cabinCrewMember2.getRank());
        Assert.assertEquals("First Officer", cabinCrewMember3.getRank());
    }

    @Test
    public void setCabinCrewMemberCouldRelayMessage(){
        Assert.assertEquals("please fasten your seatbelt", cabinCrewMember1.getMessage());
        Assert.assertEquals("please fasten your seatbelt", cabinCrewMember2.getMessage());
        Assert.assertEquals("please fasten your seatbelt", cabinCrewMember3.getMessage());
    }
}
