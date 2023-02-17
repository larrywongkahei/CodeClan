import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import staff.management.Director;


public class DirectorTest {

    private Director director;


    @Before
    public void setup(){
        director = new Director ("Cindy", "AB13444C", 50000, "Finance", 300000);
    }

    @Test
    public void directorHasName(){
        Assert.assertEquals("Cindy", director.getName());
    }

    @Test
    public void directorHasNINumber(){
        Assert.assertEquals("AB13444C", director.getNiNumber());
    }

    @Test
    public void directorHasSalary(){
        Assert.assertEquals(50000, director.getSalary(), 0.0);
    }

    @Test
    public void directorHasDeptName(){
        Assert.assertEquals("Finance", director.getDeptName());
    }

    @Test
    public void directorCouldBeRaiseSalary(){
        director.raiseSalary(30);
        Assert.assertEquals(50030, director.getSalary(), 0.0);
    }

    @Test
    public void directorCouldNotBeRaiseNegativeSalary(){
        director.raiseSalary(-10);
        Assert.assertEquals(50000, director.getSalary(), 0.0);
    }

    @Test
    public void directorCouldBePaidBonus(){
        Assert.assertEquals(1000, director.payBonus(), 0.0);
    }

    @Test
    public void directorHasBudget(){
        Assert.assertEquals(300000, director.getBudget(), 0.0);
    }

    @Test
    public void directorCouldChangeName(){
        director.changeName("Joey");
        Assert.assertEquals("Joey", director.getName());
    }

}
