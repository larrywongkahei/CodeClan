import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import staff.techStaff.Developer;
public class DeveloperTest {
    private Developer developer;

    @Before
    public void setup(){
        developer = new Developer("Mike", "AB12321F", 31000);
    }

    @Test
    public void developerHasName(){
        Assert.assertEquals("Mike", developer.getName());
    }

    @Test
    public void developerHasNINumber(){
        Assert.assertEquals("AB12321F", developer.getNiNumber());
    }

    @Test
    public void developerHasSalary(){
        Assert.assertEquals(31000, developer.getSalary(), 0.0);
    }

    @Test
    public void developerCouldBeRaiseSalary(){
        developer.raiseSalary(500);
        Assert.assertEquals(31500, developer.getSalary(), 0.0);
    }

    @Test
    public void developerCouldNotBeRaiseNegativeSalary(){
        developer.raiseSalary(-10);
        Assert.assertEquals(31000, developer.getSalary(), 0.0);
    }

    @Test
    public void developerCouldBePaidBonus(){
        Assert.assertEquals(310, developer.payBonus(), 0.0);
    }

    @Test
    public void developerCouldChangeName(){
        developer.changeName("Joe");
        Assert.assertEquals("Joe", developer.getName());
    }

}
